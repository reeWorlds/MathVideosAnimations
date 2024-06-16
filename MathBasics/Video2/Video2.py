from manim import *

def build_vgroup_angles(p1, p2, p3, num, r_min, r_max):
	angles = VGroup()

	def create_angle(i):
		r = r_min + (r_max - r_min) * i / num
		return always_redraw(
			lambda: Angle(
				Line(p1.get_center(), p2.get_center()),
				Line(p1.get_center(), p3.get_center()),
				radius=r,
				color=BLACK
			)
		)

	for i in range(num):
		angle = create_angle(i)
		angles.add(angle)

	return angles

class TriangleAngleSum(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		ax = ValueTracker(-4.5)
		ay = ValueTracker(-1)
		bx = ValueTracker(0)
		by = ValueTracker(3)
		cx = ValueTracker(1.5)
		cy = ValueTracker(-0.5)

		pa = always_redraw(lambda: Dot(np.array([ax.get_value(), ay.get_value(), 0]), color=BLACK,
								 radius = 0.11))
		pb = always_redraw(lambda: Dot(np.array([bx.get_value(), by.get_value(), 0]), color=BLACK,
								 radius = 0.11))
		pc = always_redraw(lambda: Dot(np.array([cx.get_value(), cy.get_value(), 0]), color=BLACK,
								 radius = 0.11))
		points = VGroup(pa, pb, pc)

		textA = always_redraw(lambda: MathTex("A", color=BLACK).next_to(pa, UP))
		textB = always_redraw(lambda: MathTex("B", color=BLACK).next_to(pb, UP).shift(0.1 * UP + 0.1 * RIGHT))
		textC = always_redraw(lambda: MathTex("C", color=BLACK).next_to(pc, UP).shift(0.1 * RIGHT))
		text_points = VGroup(textA, textB, textC)

		la = always_redraw(lambda: Line(pb.get_center(), pc.get_center(), color=BLACK, stroke_width = 4.0))
		lb = always_redraw(lambda: Line(pc.get_center(), pa.get_center(), color=BLACK, stroke_width = 4.0))
		lc = always_redraw(lambda: Line(pa.get_center(), pb.get_center(), color=BLACK, stroke_width = 4.0))
		lines = VGroup(la, lb, lc)

		anga = build_vgroup_angles(pa, pc, pb, 1, 0.5, 0.5)
		angb = build_vgroup_angles(pb, pa, pc, 2, 0.4, 0.55)
		angc = build_vgroup_angles(pc, pb, pa, 3, 0.4, 0.65)
		angles_m = VGroup(anga, angb, angc)

		anga_t = always_redraw(lambda: MathTex("\\alpha", color=BLACK).next_to(anga, RIGHT)\
			.shift(0.15 * UP - 0.15 * RIGHT))
		angb_t = always_redraw(lambda: MathTex("\\beta", color=BLACK).next_to(angb, DOWN)\
			.shift(0.1 * LEFT + 0.15 * UP))
		angc_t = always_redraw(lambda: MathTex("\\gamma", color=BLACK).next_to(angc, LEFT)\
			.shift(0.2 * RIGHT + 0.1 * UP))
		angles_m_t = VGroup(anga_t, angb_t, angc_t)

		ext_AB_stroke = ValueTracker(4)
		ext_AC_stroke = ValueTracker(4)
		ext_BC_stroke = ValueTracker(4)
		
		extended_AB = always_redraw(lambda: Line(pa.get_center() * 1.4 - pb.get_center() * 0.4,
										  pb.get_center() * 1.4 - pa.get_center() * 0.4, color=BLACK,
										  stroke_width = ext_AB_stroke.get_value()))
		extended_AC = always_redraw(lambda: Line(pa.get_center() * 1.4 - pc.get_center() * 0.4,
										  pc.get_center() * 1.4 - pa.get_center() * 0.4, color=BLACK,
										  stroke_width = ext_AC_stroke.get_value()))
		extended_BC = always_redraw(lambda: Line(pb.get_center() * 1.4 - pc.get_center() * 0.4,
										  pc.get_center() * 1.6 - pb.get_center() * 0.6, color=BLACK,
										  stroke_width = ext_BC_stroke.get_value()))
		lines_extd = VGroup(extended_AB, extended_AC, extended_BC)

		orange_stroke = ValueTracker(4)
		line_orange = always_redraw(lambda: Line(pc.get_center() + pa.get_center() - pb.get_center(),
										  pc.get_center() + pb.get_center() - pa.get_center(), color=ORANGE,
										 stroke_width = orange_stroke.get_value()))
		
		extra_a_alpha = always_redraw(lambda: Angle(
			Line(pc.get_center(), pc.get_center() * 2 - pa.get_center()),
			Line(pc.get_center(), pc.get_center() + pb.get_center() - pa.get_center()),
			radius = 0.75, color = RED))
		extra_a_t = always_redraw(lambda: MathTex("\\alpha", color=RED).next_to(extra_a_alpha, RIGHT)\
			.shift(0.15 * UP - 0.15 * RIGHT))

		extra_a_beta = always_redraw(lambda: Angle(
			Line(pc.get_center(), pc.get_center() + pa.get_center() - pb.get_center()),
			Line(pc.get_center(), pc.get_center() * 2 - pb.get_center()),
			radius = 0.75, color = GREEN))
		extra_b_t = always_redraw(lambda: MathTex("\\beta", color=GREEN).next_to(extra_a_beta, DOWN)\
			.shift(0.15 * UP - 0.15 * RIGHT))

		extra_a_gamma = always_redraw(lambda: Angle(
			Line(pc.get_center(), pc.get_center() * 2 - pb.get_center()),
			Line(pc.get_center(), pc.get_center() * 2 - pa.get_center()),
			radius = 0.75, color = BLUE))
		extra_c_t = always_redraw(lambda: MathTex("\\gamma", color=BLUE).next_to(extra_a_gamma, RIGHT)\
			.shift(0.3 * DOWN + 0.3 * LEFT))

		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		final_text = MathTex(r"\textcolor{red}{\alpha} + \textcolor{green}{\beta} + \textcolor{blue}{\gamma}"\
			" = 180^\circ", tex_template = myTemplate, color = BLACK).shift(3 * UP + 4 * LEFT)
		sur_rec = SurroundingRectangle(final_text, buff=0.1)
		sur_rec.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(text_points, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(angles_m, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Write(angles_m_t, lag_ratio = 0), run_time = 2)
		self.wait(3)
		self.play(Create(lines_extd, lag_ratio = 0), run_time = 2)
		self.wait(3)
		
		self.play(ReplacementTransform(extended_AB.copy(), line_orange), run_time = 2)
		self.wait(3)
		
		self.play(ext_AB_stroke.animate.set_value(8), orange_stroke.animate.set_value(8), run_time = 2)
		self.play(ext_AC_stroke.animate.set_value(8), run_time = 2)
		self.wait(2)
		self.play(Create(extra_a_alpha), run_time = 2)
		self.wait(2)
		self.play(Write(extra_a_t), run_time = 2)
		self.wait(2)
		self.play(ext_AB_stroke.animate.set_value(4), orange_stroke.animate.set_value(4),
			ext_AC_stroke.animate.set_value(4), run_time = 2)
		self.wait(3)
		
		self.play(ext_AB_stroke.animate.set_value(8), orange_stroke.animate.set_value(8), run_time = 2)
		self.play(ext_BC_stroke.animate.set_value(8), run_time = 2)
		self.wait(2)
		self.play(Create(extra_a_beta), run_time = 2)
		self.wait(2)
		self.play(Write(extra_b_t), run_time = 2)
		self.wait(2)
		self.play(ext_AB_stroke.animate.set_value(4), orange_stroke.animate.set_value(4),
			ext_BC_stroke.animate.set_value(4), run_time = 2)
		self.wait(3)
		
		self.play(ext_AC_stroke.animate.set_value(8), ext_BC_stroke.animate.set_value(8), run_time = 2)
		self.wait(2)
		self.play(Create(extra_a_gamma), run_time = 3)
		self.wait(2)
		self.play(Write(extra_c_t), run_time = 3)
		self.wait(2)
		self.play(ext_AC_stroke.animate.set_value(4), ext_BC_stroke.animate.set_value(4), run_time = 2)
		self.wait(3)

		self.play(Write(final_text), run_time = 3)
		self.play(Create(sur_rec), run_time = 3)
		self.wait(3)

	def showa2(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		circle = Circle(radius=3, color=BLACK, stroke_width = 4).move_to(ORIGIN)

		radius1 = Line(circle.get_center(), circle.get_start(), color=GREEN)

		a_val = ValueTracker(5 / 360)
		radius2 = always_redraw(lambda : Line(circle.get_center(),
										circle.point_from_proportion(a_val.get_value()), color=GREEN))

		ang = always_redraw(lambda : Angle(radius1, radius2, radius = 0.7, color = RED, stroke_width = 6))

		angle_label = always_redraw(lambda: MathTex(f"\\textcolor{{red}}{{\\alpha}} = "
											  f"{int(a_val.get_value() * 360 + 0.5)}^\\circ",
											 color = BLACK, tex_template = myTemplate).next_to(circle, RIGHT)\
												 .shift(RIGHT))

		self.wait(3)
		self.play(Create(circle), run_time = 2)
		self.play(Create(radius1), run_time = 2)
		self.wait(3)

		self.play(Create(radius2), run_time = 2)
		self.play(Create(ang), run_time = 2)
		self.wait(3)

		self.play(Write(angle_label), run_time = 2)
		self.wait(3)

		self.play(a_val.animate.set_value(0.999), run_time = 6)
		self.wait(3)
		self.play(a_val.animate.set_value(0.499), run_time = 4)
		self.wait(3)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()