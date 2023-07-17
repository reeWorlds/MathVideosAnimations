from manim import *

def line_intersection(line1, line2):
	xdiff = (line1.get_start()[0] - line1.get_end()[0], line2.get_start()[0] - line2.get_end()[0])
	ydiff = (line1.get_start()[1] - line1.get_end()[1], line2.get_start()[1] - line2.get_end()[1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)

	d = (det(*line1.get_start_and_end()), det(*line2.get_start_and_end()))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return Dot(x * RIGHT + y * UP, color = BLACK, radius = 0.06)


class CircleProps(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		circ = Circle(radius = 2.5, color = BLACK).shift(2.5 * LEFT)

		pa = Dot(circ.point_from_proportion(0.1), radius = 0.05, color = BLACK)
		pb = Dot(circ.point_from_proportion(0.5), radius = 0.05, color = BLACK)
		pc = Dot(circ.point_from_proportion(0.25), radius = 0.05, color = BLACK)
		pd = Dot(circ.point_from_proportion(0.8), radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc, pd)

		pa_t = MathTex("A", color = BLACK).next_to(pa, RIGHT).shift(0.2 * LEFT + 0.1 * UP)
		pb_t = MathTex("B", color = BLACK).next_to(pb, LEFT).shift(0.1 * RIGHT)
		pc_t = MathTex("C", color = BLACK).next_to(pc, UP).shift(0.1 * DOWN)
		pd_t = MathTex("D", color = BLACK).next_to(pd, DOWN).shift(0.1 * UP)
		points_t = VGroup(pa_t, pb_t, pc_t, pd_t)

		l1 = Line(pa.get_center(), pb.get_center(), color = BLACK)
		l2 = Line(pc.get_center(), pd.get_center(), color = BLACK)

		pp = line_intersection(l1, l2)
		pp_t = MathTex("P", color = BLACK).next_to(pp, RIGHT).shift(0.2 * LEFT + 0.2 * DOWN)

		ta = MathTex("a", color = BLACK).next_to(Line(pa.get_center(), pp.get_center()), UP).shift(0.4 * DOWN)
		tb = MathTex("b", color = BLACK).next_to(Line(pb.get_center(), pp.get_center()), UP).shift(0.55 * DOWN)
		tc = MathTex("c", color = BLACK).next_to(Line(pc.get_center(), pp.get_center()), RIGHT).shift(0.3 * LEFT)
		td = MathTex("d", color = BLACK).next_to(Line(pd.get_center(), pp.get_center()), RIGHT).shift(0.4 * LEFT)
		lines_t = VGroup(ta, tb, tc, td)

		eq1 = MathTex(r"a \cdot b = c \cdot d", color = BLACK, font_size = 100).shift(3.5 * RIGHT)

		eq2_1 = MathTex(r"\angle{APC} = \angle{BPD}", color = BLACK, font_size = 50).shift(3.5 * RIGHT + 2.5 * UP)
		eq2_2 = MathTex(r"\angle{CAB} = \angle{CDB}", color = BLACK, font_size = 50).next_to(eq2_1, DOWN)
		eq2_3 = MathTex(r"\angle{ACD} = \angle{ABD}", color = BLACK, font_size = 50).next_to(eq2_2, DOWN)
		eq2_4 = MathTex(r"\triangle APC \sim \triangle DPB", color = BLACK, font_size = 60)\
			.next_to(eq2_3, DOWN).shift(0.4 * DOWN)

		self.wait(2)
		self.play(Create(circ), run_time = 2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(l1), Create(l2), run_time = 2)
		self.wait(2)
		self.play(Create(pp), Write(pp_t), run_time = 2)
		self.wait(2)
		self.play(Write(lines_t), run_time = 2)
		self.wait(2)
		self.play(Write(eq1), run_time = 2)

		self.wait(2)
		self.play(FadeOut(eq1), run_time = 2)
		self.wait(2)
		self.play(Write(eq2_1), run_time = 2)
		self.wait(2)
		self.play(Write(eq2_2), run_time = 2)
		self.wait(2)
		self.play(Write(eq2_3), run_time = 2)
		self.wait(2)
		self.play(Write(eq2_4), run_time = 2)

		self.wait(2)
		self.play(FadeOut(eq2_1), FadeOut(eq2_2), FadeOut(eq2_3), run_time = 2)
		self.play(eq2_4.animate.shift(2.5 * UP), run_time = 2)

		eq3_1 = MathTex(r"\frac{PA}{PC} = \frac{PD}{PB}", color = BLACK, font_size = 50).next_to(eq2_4, DOWN)
		eq3_2 = MathTex(r"PA \cdot PB = PC \cdot PD", color = BLACK, font_size = 50).next_to(eq3_1, DOWN)
		eq3_3 = MathTex(r"a \cdot b = c \cdot d", color = BLACK, font_size = 70).next_to(eq3_2, DOWN)\
			.shift(0.3 * DOWN)
		sur_box1 = SurroundingRectangle(eq3_3).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		final_eq_1_g = VGroup(eq3_3, sur_box1)

		self.wait(2)
		self.play(Write(eq3_1), run_time = 2)
		self.wait(2)
		self.play(Write(eq3_2), run_time = 2)
		self.wait(2)
		self.play(Write(eq3_3), run_time = 2)
		self.play(Create(sur_box1), run_time = 2)

		self.wait(2)
		self.play(FadeOut(eq2_4), FadeOut(eq3_1), FadeOut(eq3_2), run_time = 2)
		self.play(final_eq_1_g.animate.shift(1.5 * UP), run_time = 2)

		po = Dot(circ.get_center(), radius = 0.05, color = BLACK)
		po_t = MathTex("O", color = BLACK).next_to(po, RIGHT).shift(0.3 * LEFT + 0.2 * DOWN)

		po_pp_vector = pp.get_center() - po.get_center()
		po_pp_alpha = np.arctan2(po_pp_vector[1], po_pp_vector[0])
		diameter_line = Line(circ.point_at_angle(po_pp_alpha), circ.point_at_angle(po_pp_alpha + PI), color=BLUE)\
			.set_z_index(-1)

		r_t = MathTex("r", font_size = 40, color = BLUE).next_to(
			Line(circ.point_at_angle(po_pp_alpha + PI), po.get_center()), LEFT).shift(0.5 * RIGHT)
		d_t = MathTex("d", font_size = 40, color = BLUE).next_to(
			Line(po.get_center(), pp.get_center()), LEFT).shift(0.3 * RIGHT)
		rmd_t = MathTex(r"r \!-\! d", font_size = 40, color = BLUE).next_to(
			Line(pp.get_center(), circ.point_at_angle(po_pp_alpha)), RIGHT).shift(0.4 * LEFT + 0.1 * UP)

		eq4_1 = MathTex(r"a \cdot b = c \cdot d = (r + d) \cdot (c - d)", color = BLACK, font_size = 50)\
			.next_to(sur_box1, DOWN).shift(0.3 * DOWN)
		eq4_2 = MathTex(r"a \cdot b = c \cdot d = r^2 - d^2", color = BLACK, font_size = 50).next_to(eq4_1, DOWN)\
			.shift(0.2)
		sur_box2 = SurroundingRectangle(eq4_2).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(Create(po), Write(po_t), Create(diameter_line), run_time = 2)
		self.wait(2)
		self.play(Write(r_t), run_time = 2)
		self.wait(2)
		self.play(Write(d_t), run_time = 2)
		self.wait(2)
		self.play(Write(rmd_t), run_time = 2)

		self.wait(2)
		self.play(Write(eq4_1), run_time = 2)
		self.wait(2)
		self.play(Write(eq4_2), run_time = 2)
		self.wait(2)
		self.play(FadeOut(eq4_1), Create(sur_box2), run_time = 2)

		self.wait(3)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()