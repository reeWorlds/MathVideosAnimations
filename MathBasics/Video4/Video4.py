from manim import *
import math

class TrigDef(MovingCameraScene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		pa = Dot(np.array([0, -2, 0]), color = BLACK, radius = 0.06)
		pb = Dot(np.array([-6, 2, 0]), color = BLACK, radius = 0.06)
		pc = Dot(np.array([-6, -2, 0]), color = BLACK, radius = 0.06)
		points = VGroup(pa, pb, pc)

		tpa = MathTex("A", color = BLACK).next_to(pa, DOWN)
		tpb = MathTex("B", color = BLACK).next_to(pb, UP)
		tpc = MathTex("C", color = BLACK).next_to(pc, DOWN)
		t_points = VGroup(tpa, tpb, tpc)

		la_width = ValueTracker(4)
		lb_width = ValueTracker(4)
		lc_width = ValueTracker(4)

		la = always_redraw(lambda : Line(pb.get_center(), pc.get_center(), color = GREEN,
								   stroke_width = la_width.get_value()))
		lb = always_redraw(lambda : Line(pc.get_center(), pa.get_center(), color = BLUE,
								   stroke_width = lb_width.get_value()))
		lc = always_redraw(lambda : Line(pa.get_center(), pb.get_center(), color = RED,
								   stroke_width = lc_width.get_value()))
		lines = VGroup(la, lb, lc)

		r_a = RightAngle(Line(pc.get_center(), pa.get_center()), Line(pc.get_center(), pb.get_center()),
				  length = 0.3, other_angle = False, color=BLACK, stroke_width = 4.0)

		tla = MathTex("a", color = GREEN, font_size = 80).next_to(la, LEFT)
		tlb = MathTex("b", color = BLUE, font_size = 80).next_to(lb, DOWN)
		tlc = MathTex("c", color = RED, font_size = 80).next_to(lc, UP).shift(2.0 * DOWN)
		t_lines = VGroup(tla, tlb, tlc)

		a_alpha = Angle(Line(pa.get_center(), pb.get_center()), Line(pa.get_center(), pc.get_center()),
				  radius = 1, other_angle = False, color = BLACK, stroke_width = 4.0)
		t_a_alpha = MathTex(r"\alpha", color = BLACK, font_size = 60).next_to(a_alpha, LEFT)\
			.shift(0.1 * RIGHT + 0.1 * UP)

		self.wait(3)
		self.play(Create(points, lag_ratio = 0), run_time = 2)
		self.play(Write(t_points), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Create(r_a), run_time = 2)
		self.play(Write(t_lines), run_time = 2)
		self.play(Create(a_alpha), Write(t_a_alpha), run_time = 2)
		self.wait(2)

		self.play(lc_width.animate.set_value(12), run_time = 2)
		self.wait(2)
		self.play(lc_width.animate.set_value(4), run_time = 2)
		self.wait(2)

		self.play(la_width.animate.set_value(12), run_time = 2)
		self.wait(2)
		self.play(la_width.animate.set_value(4), run_time = 2)
		self.wait(2)

		self.play(lb_width.animate.set_value(12), run_time = 2)
		self.wait(2)
		self.play(lb_width.animate.set_value(4), run_time = 2)
		self.wait(2)

		sin_def = MathTex(r"\sin(\alpha) = \frac{\textcolor{green}{a}}{\textcolor{red}{c}}", color = BLACK,
				   font_size = 50, tex_template = myTemplate).shift(1.9 * RIGHT + 2 * UP)

		self.play(la_width.animate.set_value(10), lc_width.animate.set_value(10), run_time = 2)
		self.play(Write(sin_def), run_time = 2)
		self.play(la_width.animate.set_value(4), lc_width.animate.set_value(4), run_time = 2)
		self.wait(2)

		cos_def = MathTex(r"\cos(\alpha) = \frac{\textcolor{blue}{b}}{\textcolor{red}{c}}", color = BLACK, 
					font_size = 50, tex_template = myTemplate).next_to(sin_def, DOWN)

		self.play(lb_width.animate.set_value(10), lc_width.animate.set_value(10), run_time = 2)
		self.play(Write(cos_def), run_time = 2)
		self.play(lb_width.animate.set_value(4), lc_width.animate.set_value(4), run_time = 2)
		self.wait(2)

		tan_def = MathTex(r"\tan(\alpha) = \frac{\textcolor{green}{a}}{\textcolor{blue}{b}}", color = BLACK, 
					font_size = 50, tex_template = myTemplate).next_to(cos_def, DOWN)

		self.play(la_width.animate.set_value(10), lb_width.animate.set_value(10), run_time = 2)
		self.play(Write(tan_def), run_time = 2)
		self.play(la_width.animate.set_value(4), lb_width.animate.set_value(4), run_time = 2)
		self.wait(2)

		cot_def = MathTex(r"\cot(\alpha) = \frac{\textcolor{blue}{b}}{\textcolor{green}{a}}", color = BLACK,
					font_size = 50, tex_template = myTemplate).next_to(tan_def, DOWN)

		self.play(la_width.animate.set_value(10), lb_width.animate.set_value(10), run_time = 2)
		self.play(Write(cot_def), run_time = 2)
		self.play(la_width.animate.set_value(4), lb_width.animate.set_value(4), run_time = 2)
		self.wait(2)
		
		t_tg = MathTex(r" = tg(\alpha)", color = BLACK, font_size = 50).next_to(tan_def, RIGHT)
		t_ctg = MathTex(r" = ctg(\alpha)", color = BLACK, font_size = 50).next_to(cot_def, RIGHT)
		tg_cross = Cross(t_tg, stroke_width = 4.0, color = RED)
		ctg_cross = Cross(t_ctg, stroke_width = 4.0, color = RED)

		self.play(Write(t_tg), Write(t_ctg), run_time = 2)
		self.wait(2)
		self.play(Create(tg_cross), Create(ctg_cross), run_time = 2)
		self.wait(2)
		self.play(FadeOut(tg_cross), FadeOut(ctg_cross), FadeOut(t_tg), FadeOut(t_ctg), run_time = 2)
		self.wait(2)

		tan_extr1 = MathTex(r" = \frac{\textcolor{green}{a} / \textcolor{red}{c}}"\
					  r"{\textcolor{blue}{b} / \textcolor{red}{c}}", color = BLACK, font_size = 50,
					  tex_template = myTemplate).next_to(tan_def, RIGHT)
		tan_extr2 = MathTex(r" = \frac{\sin(\alpha)}{\cos(\alpha)}", color = BLACK, font_size = 50,
					 tex_template = myTemplate).next_to(tan_extr1, RIGHT)
		tan_extr2.generate_target()
		tan_extr2.target.next_to(tan_def, RIGHT)
		cot_extr = MathTex(r" = \frac{\cos(\alpha)}{\sin(\alpha)}", color = BLACK, font_size = 50)\
			.next_to(cot_def, RIGHT)

		self.play(Write(tan_extr1), run_time = 2)
		self.wait(2)
		self.play(Write(tan_extr2), run_time = 2)
		self.wait(2)
		self.play(MoveToTarget(tan_extr2), FadeOut(tan_extr1), run_time = 2)
		self.wait(2)
		self.play(Write(cot_extr), run_time = 2)

		self.wait(3)

	def showa2(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		pa = Dot(np.array([0, -2, 0]), color = BLACK, radius = 0.06)
		pb = Dot(np.array([-6, 2, 0]), color = BLACK, radius = 0.06)
		pc = Dot(np.array([-6, -2, 0]), color = BLACK, radius = 0.06)
		points = VGroup(pa, pb, pc)

		la = Line(pb.get_center(), pc.get_center(), color = GREEN, stroke_width = 4)
		lb = Line(pc.get_center(), pa.get_center(), color = BLUE, stroke_width = 4)
		lc = Line(pa.get_center(), pb.get_center(), color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		r_a = RightAngle(Line(pc.get_center(), pa.get_center()), Line(pc.get_center(), pb.get_center()),
				  length = 0.3, other_angle = False, color=BLACK, stroke_width = 4.0)

		tla = MathTex("3", color = GREEN, font_size = 80).next_to(la, LEFT)
		tlb = MathTex("4", color = BLUE, font_size = 80).next_to(lb, DOWN)
		tlc = MathTex("5", color = RED, font_size = 80).next_to(lc, UP).shift(2.0 * DOWN)
		t_lines = VGroup(tla, tlb, tlc)

		a_alpha = Angle(Line(pa.get_center(), pb.get_center()), Line(pa.get_center(), pc.get_center()),
				  radius = 1, other_angle = False, color = BLACK, stroke_width = 4.0)
		t_a_alpha = MathTex(r"\alpha", color = BLACK, font_size = 60).next_to(a_alpha, LEFT)\
			.shift(0.1 * RIGHT + 0.1 * UP)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Create(lines, lag_ratio = 0), Create(r_a), Write(t_lines),
		   Create(a_alpha), Write(t_a_alpha), run_time = 3)
		self.wait(2)

		sin_def = MathTex(r"\sin(\alpha) = \frac{\textcolor{green}{3}}{\textcolor{red}{5}} = 0.6",
				   color = BLACK, font_size = 50, tex_template = myTemplate).shift(3 * RIGHT + 2 * UP)

		self.play(Write(sin_def), run_time = 2)
		self.wait(2)

		cos_def = MathTex(r"\cos(\alpha) = \frac{\textcolor{blue}{4}}{\textcolor{red}{5}} = 0.8", 
					color = BLACK, font_size = 50, tex_template = myTemplate).next_to(sin_def, DOWN)

		self.play(Write(cos_def), run_time = 2)
		self.wait(2)

		tan_def = MathTex(r"\tan(\alpha) = \frac{\textcolor{green}{3}}{\textcolor{blue}{4}} = 0.75", 
					color = BLACK, font_size = 50, tex_template = myTemplate).next_to(cos_def, DOWN)

		self.play(Write(tan_def), run_time = 2)
		self.wait(2)

		cot_def = MathTex(r"\cot(\alpha) = \frac{\textcolor{blue}{4}}{\textcolor{green}{3}} \approx 1.333", 
					color = BLACK, font_size = 50, tex_template = myTemplate).next_to(tan_def, DOWN)

		self.play(Write(cot_def), run_time = 2)
		self.wait(2)

	def showa3(self):
		self.camera.frame.scale(0.5)

		arrowX = Arrow(3 * LEFT, 3 * RIGHT, buff = 0, color = BLACK, stroke_width = 2,
				 max_tip_length_to_length_ratio = 0.025)
		arrowY = Arrow(1.8 * DOWN, 1.8 * UP, buff = 0, color = BLACK, stroke_width = 2,
				max_tip_length_to_length_ratio = 0.04)
		
		labelX = MathTex(r"X", color = BLACK, font_size = 30).next_to(arrowX, RIGHT)\
			.shift(0.5 * LEFT + 0.25 * DOWN)
		labelY = MathTex(r"Y", color = BLACK, font_size = 30).next_to(arrowY, UP)\
			.shift(0.25 * LEFT + 0.45 * DOWN)

		unit_x_l = Line(RIGHT + 0.08 * DOWN, RIGHT + 0.08 * UP, stroke_width = 2, color = BLACK)
		unit_y_l = Line(UP + 0.08 * LEFT, UP + 0.08 * RIGHT, stroke_width = 2, color = BLACK)

		self.wait(2)
		self.play(Create(arrowX), Create(arrowY), Write(labelX), Write(labelY), Create(unit_x_l),
		   Create(unit_y_l), run_time = 2)
		self.wait(2)

		circle = Circle(radius = 1, color = BLACK, stroke_width = 2)
		alpha = ValueTracker(PI / 6)

		main_l = always_redraw(lambda : Line(ORIGIN, math.cos(alpha.get_value()) * RIGHT + 
									   math.sin(alpha.get_value()) * UP, stroke_width = 3, color = BLACK))

		dot = always_redraw(lambda : Dot([math.cos(alpha.get_value()), math.sin(alpha.get_value()), 0], 
								   radius = 0.03, color = BLACK))

		ang = always_redraw(lambda : Angle(Line(ORIGIN, RIGHT),
									 Line(ORIGIN, math.cos(alpha.get_value()) * RIGHT +
			  math.sin(alpha.get_value()) * UP), stroke_width = 1.5, color = BLUE_E))

		alpha_t = MathTex(r"\alpha", color = BLACK, font_size = 20).shift(0.55 * RIGHT + 0.15 * UP)

		self.play(Create(circle), run_time = 2)
		self.play(Create(main_l), Create(ang), Create(dot), Write(alpha_t), run_time = 2)
		self.wait(2)

		cos_l = always_redraw(lambda : DashedLine(dot.get_center(), math.cos(alpha.get_value()) * RIGHT,
									 stroke_width = 3, color = ORANGE))
		cos_p = always_redraw(lambda : Dot([math.cos(alpha.get_value()), 0, 0], radius = 0.02, color = BLACK))
		cos_t = always_redraw(lambda : MathTex(r"\mathbf{cos(\alpha)}", color = BLUE, font_size = 20)\
			.next_to(cos_p, DOWN).shift(0.2 * UP))

		self.play(Create(cos_l), Create(cos_p), Write(cos_t), run_time = 2)
		self.wait(2)

		sin_l = always_redraw(lambda : DashedLine(dot.get_center(), math.sin(alpha.get_value()) * UP,
									 stroke_width = 3, color = ORANGE))
		sin_p = always_redraw(lambda : Dot([0, math.sin(alpha.get_value()), 0], radius = 0.02, color = BLACK))
		sin_t = always_redraw(lambda : MathTex(r"\mathbf{sin(\alpha)}", color = BLUE, font_size = 20)\
			.next_to(sin_p, LEFT).shift(0.2 * RIGHT))

		self.play(Create(sin_l), Create(sin_p), Write(sin_t), run_time = 2)
		self.wait(2)

		tan_axs = always_redraw(lambda : Line(RIGHT + 3 * DOWN, RIGHT + 3 * UP, stroke_width = 2,
									   color = BLACK).set_z_index(-1))
		tan_p = always_redraw(lambda : Dot([1, math.tan(alpha.get_value()), 0], radius = 0.03, color = BLACK))
		tan_l = always_redraw(lambda : DashedLine(tan_p.get_center(), math.tan(alpha.get_value()) * UP,
									 stroke_width = 2, color = GREEN))
		tan_t = always_redraw(lambda : MathTex(r"\mathbf{tan(\alpha)}", color = BLUE, font_size = 20)\
			.next_to(tan_p, RIGHT).shift(0.2 * LEFT))
		tan_extr_l = always_redraw(lambda : Line(ORIGIN, tan_p.get_center(), stroke_width = 1, color = BLACK)\
			.set_z_index(-1))

		cot_axs = always_redraw(lambda : Line(UP + 4 * LEFT, UP + 4 * RIGHT, stroke_width = 2,
									   color = BLACK).set_z_index(-1))
		cot_p = always_redraw(lambda : Dot([1.0 / math.tan(alpha.get_value()), 1, 0], radius = 0.03,
									color = BLACK))
		cot_l = always_redraw(lambda : DashedLine(cot_p.get_center(), 1 / math.tan(alpha.get_value()) * RIGHT,
									 stroke_width = 2, color = GREEN))
		cot_t = always_redraw(lambda : MathTex(r"\mathbf{cot(\alpha)}", color = BLUE, font_size = 20)\
			.next_to(cot_p, UP).shift(0.2 * DOWN))
		cot_extr_l = always_redraw(lambda : Line(ORIGIN, cot_p.get_center(), stroke_width = 1, color = BLACK)\
			.set_z_index(-1))

		self.play(Create(tan_axs), Create(tan_p), Create(tan_l), Write(tan_t), Create(tan_extr_l), run_time = 2)
		self.wait(2)
		self.play(Create(cot_axs), Create(cot_p), Create(cot_l), Write(cot_t), Create(cot_extr_l), run_time = 2)
		self.wait(2)

		self.play(alpha.animate(rate_func = linear).set_value(PI * 1.85), run_time = 7)
		self.wait(2)
		self.play(alpha.animate(rate_func = linear).set_value(PI * 0.2), run_time = 5)

		self.wait(2)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()
