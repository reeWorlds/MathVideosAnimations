from manim import *

class CosTheorem(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		pa = Dot([4, -0.5, 0], radius = 0.05, color = BLACK)
		pb = Dot([-1, 3.5, 0], radius = 0.05, color = BLACK)
		pc = Dot([-4, 0, 0], radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		la = Line(pb.get_center(), pc.get_center(), color = GREEN, stroke_width = 4)
		lb = Line(pc.get_center(), pa.get_center(), color = BLUE, stroke_width = 4)
		lc = Line(pa.get_center(), pb.get_center(), color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		la_t = MathTex("a", color = GREEN, font_size = 80).next_to(la, LEFT).shift(RIGHT * 1.3)
		lb_t = MathTex("b", color = BLUE, font_size = 80).next_to(lb, DOWN).shift(UP * 0.25)
		lc_t = MathTex("c", color = RED, font_size = 80).next_to(lc, RIGHT).shift(LEFT * 2.3)
		lines_t = VGroup(la_t, lb_t, lc_t)

		alpha = Angle(Line(pc, pa), Line(pc, pb), radius = 0.5, color = BLACK)
		alpha_t = MathTex("\\alpha", color = BLACK, font_size = 60).next_to(alpha, RIGHT)\
			.shift(LEFT * 0.1 + UP * 0.1)

		formula = MathTex(r"\textcolor{red}{c}^2 = \textcolor{green}{a}^2 + \textcolor{blue}{b}^2 - "
					r"2\textcolor{green}{a}\textcolor{blue}{b}\cos(\alpha)",
					tex_template = myTemplate, color = BLACK, font_size = 100).shift(DOWN * 2)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(lines_t, lag_ratio = 0), run_time = 2)
		self.play(Create(alpha), Write(alpha_t), run_time = 2)

		self.wait(2)
		self.play(Write(formula), run_time = 3)
		self.wait(2)

	def showa2(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		pa = Dot([-1, -2, 0], radius = 0.06, color = BLACK)
		pb = Dot([-5.5, 2, 0], radius = 0.06, color = BLACK)
		pc = Dot([-6.8, -1.5, 0], radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		la = Line(pb.get_center(), pc.get_center(), color = GREEN, stroke_width = 4)
		lb = Line(pc.get_center(), pa.get_center(), color = BLUE, stroke_width = 4)
		lc = Line(pa.get_center(), pb.get_center(), color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		la_t = MathTex("8", color = GREEN, font_size = 60).next_to(la, LEFT).shift(RIGHT * 1.3)
		lb_t = MathTex("15", color = BLUE, font_size = 60).next_to(lb, DOWN).shift(UP * 0.25)
		lc_t = MathTex("c = ?", color = RED, font_size = 60).next_to(lc, RIGHT).shift(LEFT * 2)
		lines_t = VGroup(la_t, lb_t, lc_t)

		alpha = Angle(Line(pc, pa), Line(pc, pb), radius = 0.5, color = BLACK)
		alpha_t = MathTex("\\alpha = 60^\circ", color = BLACK, font_size = 60).next_to(alpha, RIGHT)\
			.shift(LEFT * 0.1 + UP * 0.1)

		f1 = MathTex(r"\textcolor{red}{c}^2 = \textcolor{green}{8}^2 + \textcolor{blue}{15}^2 - "
					r"2\cdot\textcolor{green}{8}\cdot\textcolor{blue}{15}\cos(60^{\circ})",
					tex_template = myTemplate, color = BLACK, font_size = 60).shift(2 * UP + 2.5 * RIGHT)
		f2 = MathTex(r"\textcolor{red}{c}^2 = 289 - 2\cdot\textcolor{green}{8}\cdot\textcolor{blue}{15}"
			   r"\cdot\tfrac{1}{2}", tex_template = myTemplate, color = BLACK, font_size = 60)\
				   .next_to(f1, DOWN)
		f3 = MathTex(r"\textcolor{red}{c}^2 = 289 - 120", tex_template = myTemplate, color = BLACK,
			  font_size = 60).next_to(f2, DOWN)
		f4 = MathTex(r"\textcolor{red}{c}^2 = 169", tex_template = myTemplate, color = BLACK, font_size = 60)\
			.next_to(f3, DOWN)
		f5 = MathTex(r"\textcolor{red}{c} = 13", tex_template = myTemplate, color = BLACK, font_size = 60)\
			.next_to(f4, DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(lines_t, lag_ratio = 0), run_time = 2)
		self.play(Create(alpha), Write(alpha_t), run_time = 2)

		self.wait(2)
		self.play(Write(f1), run_time = 2)
		self.wait(2)
		self.play(Write(f2), run_time = 2)
		self.wait(2)
		self.play(Write(f3), run_time = 2)
		self.wait(2)
		self.play(Write(f4), run_time = 2)
		self.wait(2)
		self.play(Write(f5), run_time = 2)

		self.wait(2)

	def showa3(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		pa = Dot([-1, -2, 0], radius = 0.06, color = BLACK)
		pb = Dot([-4, 2, 0], radius = 0.06, color = BLACK)
		pc = Dot([-6.6, -1.5, 0], radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK, font_size = 60).next_to(pa, DOWN)
		pb_t = MathTex("B", color = BLACK, font_size = 60).next_to(pb, UP)
		pc_t = MathTex("C", color = BLACK, font_size = 60).next_to(pc, LEFT).shift(RIGHT * 0.5 + DOWN * 0.5)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = GREEN, stroke_width = 4)
		lb = Line(pc.get_center(), pa.get_center(), color = BLUE, stroke_width = 4)
		lc = Line(pa.get_center(), pb.get_center(), color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		la_t = MathTex("a", color = GREEN, font_size = 60).next_to(la, LEFT).shift(RIGHT * 1.3)
		lb_t = MathTex("b", color = BLUE, font_size = 60).next_to(lb, DOWN).shift(UP * 0.25 + RIGHT * 0.5)
		lc_t = MathTex("c", color = RED, font_size = 60).next_to(lc, RIGHT).shift(LEFT * 1.5)
		lines_t = VGroup(la_t, lb_t, lc_t)

		alpha = Angle(Line(pc, pa), Line(pc, pb), radius = 0.5, color = BLACK)
		alpha_t = MathTex("\\alpha", color = BLACK, font_size = 50).next_to(alpha, RIGHT)\
			.shift(LEFT * 0.2 + UP * 0.1)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(lines_t, lag_ratio = 0), run_time = 2)
		self.play(Create(alpha), Write(alpha_t), run_time = 2)
		
		foot = Dot(lb.get_projection(pb.get_center()), radius = 0.06, color = BLACK)
		foot_t = MathTex("H", color = BLACK, font_size = 60).next_to(foot, DOWN)
		foot_l = Line(pb.get_center(), foot.get_center(), color = BLACK, stroke_width = 4)
		foot_l_t = MathTex("h", color = BLACK, font_size = 60).next_to(foot_l, RIGHT).shift(LEFT * 0.3)
		foot_r_a = RightAngle(Line(foot.get_center(), pa.get_center()),
					   Line(foot.get_center(), pb.get_center()), length = 0.3, color = BLACK)

		self.wait(2)
		self.play(Create(foot), Write(foot_t), Create(foot_l), Write(foot_l_t), Create(foot_r_a), run_time = 2)

		txt1 = MathTex(r"\textcolor{green}{a}^2 = h^2 + CH^2", tex_template = myTemplate, color = BLACK,
				font_size = 50).shift(3 * UP + 2.9 * RIGHT)
		txt2 = MathTex(r"\textcolor{green}{a}^2 = h^2 + \textcolor{green}{a}^2\cos^2(\alpha)", 
				tex_template = myTemplate, color = BLACK, font_size = 50).next_to(txt1, DOWN)
		txt2_sur = SurroundingRectangle(txt2, color = YELLOW, buff = 0.1, stroke_width = 2)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.play(Create(txt2_sur), run_time = 2)

		txt3 = MathTex(r"\textcolor{red}{c}^2=h^2+(\textcolor{blue}{b}-\textcolor{green}{a}\cos(\alpha))^2", 
				 tex_template = myTemplate, color = BLACK, font_size = 50).next_to(txt2, DOWN)\
					 .shift(DOWN * 0.4)
		txt3_sur = SurroundingRectangle(txt3, color = YELLOW, buff = 0.1, stroke_width = 2)

		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.play(Create(txt3_sur), run_time = 2)

		txt4 = MathTex(r"\textcolor{red}{c}^2 - \textcolor{green}{a}^2 = h^2 + (\textcolor{blue}{b}-"
				 r"\textcolor{green}{a}\cos(\alpha))^2 - h^2 - \textcolor{green}{a}^2\cos^2(\alpha)", 
				tex_template = myTemplate, color = BLACK, font_size = 35).next_to(txt3, DOWN).shift(DOWN * 0.4)

		self.wait(2)
		self.play(Write(txt4), run_time = 2)

		cross1 = Cross(stroke_width = 3).scale(0.18).move_to([0.92, -0.18, 0])
		cross2 = Cross(stroke_width = 3).scale(0.18).move_to([4.44, -0.18, 0])

		self.wait(2)
		self.play(Create(cross1), Create(cross2), run_time = 2)

		txt5 = MathTex(r"\textcolor{red}{c}^2 - \textcolor{green}{a}^2 = \textcolor{blue}{b}^2 - "
				 r"2\textcolor{green}{a}\textcolor{blue}{b}\cos(\alpha) + \textcolor{green}{a}^2\cos^2(\alpha)"
				 r" - \textcolor{green}{a}^2\cos^2(\alpha)", tex_template = myTemplate, color = BLACK,
				font_size = 35).next_to(txt4, DOWN)

		self.wait(2)
		self.play(Write(txt5), run_time = 2)

		cross3 = Cross(stroke_width = 3).scale(0.18).stretch(4.2, dim = 0).move_to([4.1, -0.85, 0])
		cross4 = Cross(stroke_width = 3).scale(0.18).stretch(4.2, dim = 0).move_to([6.1, -0.85, 0])

		self.wait(2)
		self.play(Create(cross3), Create(cross4), run_time = 2)

		txt6 = MathTex(r"\textcolor{red}{c}^2 - \textcolor{green}{a}^2 = \textcolor{blue}{b}^2 - "
				r"2\textcolor{green}{a}\textcolor{blue}{b}\cos(\alpha)", tex_template = myTemplate,
				color = BLACK, font_size = 50).next_to(txt5, DOWN)

		self.wait(2)
		self.play(Write(txt6), run_time = 2)

		txt7 = MathTex(r"\textcolor{red}{c}^2 = \textcolor{green}{a}^2 + \textcolor{blue}{b}^2 - "
				r"2\textcolor{green}{a}\textcolor{blue}{b}\cos(\alpha)", tex_template = myTemplate,
				color = BLACK, font_size = 60).next_to(txt6, DOWN).shift(0.3 * DOWN)
		res_sur = SurroundingRectangle(txt7).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(Write(txt7), run_time = 2)
		self.play(Create(res_sur), run_time = 2)

		self.wait(2)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()