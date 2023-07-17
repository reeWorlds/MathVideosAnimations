from manim import *

class TrigExtra(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		pa = 5 * LEFT + 3 * UP
		pb = 2 * LEFT + 2 * DOWN
		pc = 5 * LEFT + 2 * DOWN

		la = Line(pb, pc, color = GREEN, stroke_width = 4)
		lb = Line(pc, pa, color = BLUE, stroke_width = 4)
		lc = Line(pa, pb, color = RED, stroke_width = 4)
		lines = VGroup(la, lb, lc)

		lc_t = MathTex("1", color = BLACK, font_size = 60).next_to(lc, RIGHT).shift(LEFT * 1.5)

		ang = Angle(Line(pb, pa), Line(pb, pc), radius = 0.5, color = BLACK)
		ang_t = MathTex(r"\alpha", color = BLACK, font_size = 60).next_to(ang, LEFT)\
			.shift(RIGHT * 0.2 + UP * 0.1)

		la_t = MathTex(r"\cos(\alpha)", color = BLACK, font_size = 60).next_to(la, DOWN).shift(UP * 0.2)
		lb_t = MathTex(r"\sin(\alpha)", color = BLACK, font_size = 60).next_to(lb, LEFT).shift(RIGHT * 0.1)

		formula = MathTex(r"\sin^2(\alpha) + \cos^2(\alpha) = 1", color = BLACK, font_size = 80)\
			.shift(2.4 * RIGHT + 1 * UP)
		sur_box = SurroundingRectangle(formula).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(Create(lines), run_time = 2)
		
		self.wait(2)
		self.play(Write(lc_t), run_time = 2)

		self.wait(2)
		self.play(Create(ang), Write(ang_t), run_time = 2)

		self.wait(2)
		self.play(Write(la_t), Write(lb_t), run_time = 2)

		self.wait(2)
		self.play(Write(formula), run_time = 2)
		self.play(Create(sur_box), run_time = 2)

		self.wait(2)

	def showa2(self):
		fs = 50

		txt1 = MathTex(r"\frac{1}{\cos^2(\alpha)}", color = BLACK, font_size = fs).shift(5.8 * LEFT + 1.5 * UP)
		txt2 = MathTex(r"= \frac{\sin^2(\alpha) + \cos^2(\alpha)}{\cos^2(\alpha)}", color = BLACK,
				font_size = fs).next_to(txt1, RIGHT)
		txt3 = MathTex(r"= \frac{\sin^2(\alpha)}{\cos^2(\alpha)} + 1", color = BLACK, font_size = fs)\
			.next_to(txt2, RIGHT)
		txt4 = MathTex(r"= \tan^2(\alpha) + 1", color = BLACK, font_size = fs).next_to(txt3, RIGHT)

		formula = MathTex(r"\frac{1}{\cos^2(\alpha)} = \tan^2(\alpha) + 1", color = BLACK, font_size = 60)\
			.shift(DOWN)
		sur_box = SurroundingRectangle(formula).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)

		self.wait(2)
		self.play(Write(formula), run_time = 2)
		self.play(Write(sur_box), run_time = 2)

		self.wait(2)

	def showa3(self):
		pa = Dot(5 * LEFT + 1.25 * UP, color = BLACK, radius = 0.05)
		pb = Dot(3 * RIGHT + 1.25 * UP, color = BLACK, radius = 0.05)
		pc = Dot(2 * LEFT + 3.25 * UP, color = BLACK, radius = 0.05)
		pd = Dot(2 * LEFT + 1.25 * UP, color = BLACK, radius = 0.05)
		points = VGroup(pa, pb, pc, pd)

		pa_t = MathTex(r"A", color = BLACK, font_size = 40).next_to(pa, LEFT).shift(RIGHT * 0.2)
		pb_t = MathTex(r"B", color = BLACK, font_size = 40).next_to(pb, RIGHT).shift(LEFT * 0.2)
		pc_t = MathTex(r"C", color = BLACK, font_size = 40).next_to(pc, UP).shift(DOWN * 0.2)
		pd_t = MathTex(r"D", color = BLACK, font_size = 40).next_to(pd, DOWN).shift(UP * 0.2)
		points_t = VGroup(pa_t, pb_t, pc_t, pd_t)
		
		l1 = Line(pa.get_center(), pd.get_center(), color = BLACK, stroke_width = 4)
		l2 = Line(pd.get_center(), pb.get_center(), color = BLACK, stroke_width = 4)
		l3 = Line(pa.get_center(), pc.get_center(), color = BLACK, stroke_width = 4)
		l4 = Line(pb.get_center(), pc.get_center(), color = BLACK, stroke_width = 4)
		l5 = Line(pc.get_center(), pd.get_center(), color = BLACK, stroke_width = 4)
		lines = VGroup(l1, l2, l3, l4, l5)

		ang_a = Angle(Line(pc, pa), Line(pc, pd), radius = 0.35, color = BLACK)
		ang_b = Angle(Line(pc, pd), Line(pc, pb), radius = 0.45, color = BLACK)
		ang_r1 = RightAngle(Line(pd, pa), Line(pd, pc), length = 0.2, color = BLACK)
		ang_r2 = RightAngle(Line(pd, pc), Line(pd, pb), length = 0.24, color = BLACK)
		angles = VGroup(ang_a, ang_b, ang_r1, ang_r2)

		ang_a_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_a, DOWN)\
			.shift(UP * 0.2 + LEFT * 0.15)
		ang_b_t = MathTex(r"\beta", color = BLACK, font_size = 35).next_to(ang_b, DOWN)\
			.shift(UP * 0.3 + RIGHT * 0.1)

		cd_t = MathTex(r"1", color = BLACK, font_size = 40).next_to(l5, RIGHT).shift(LEFT * 0.15)
		cd_t2 =	MathTex(r"CD = 1", color = BLACK, font_size = 50).next_to(l4, RIGHT).shift(RIGHT * 1)

		l1_t = MathTex(r"\tan(\alpha)", color = BLACK, font_size = 35).next_to(l1, DOWN).shift(UP * 0.15)
		l2_t = MathTex(r"\tan(\beta)", color = BLACK, font_size = 35).next_to(l2, DOWN).shift(UP * 0.15)
		l3_t = MathTex(r"\frac{1}{\cos(\alpha)}", color = BLACK, font_size = 35).next_to(l3, UP)\
			.shift(DOWN * 1.05 + LEFT * 0.3)
		ang_dbc = Angle(Line(pb, pc), Line(pb, pd), radius = 0.8, color = BLACK)
		ang_dbc_t = MathTex(r"90 - \beta", color = BLACK, font_size = 30).next_to(ang_dbc, LEFT)\
			.shift(RIGHT * 0.2)
		marking = VGroup(l1_t, l2_t, l3_t)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(angles, lag_ratio = 0), Write(ang_a_t), Write(ang_b_t), run_time = 2)
		self.wait(2)
		self.play(Write(cd_t), Write(cd_t2), run_time = 2)
		self.wait(2)
		self.play(Write(marking, lag_ratio = 0), Create(ang_dbc), Write(ang_dbc_t), run_time = 2)

		txt1 = MathTex(r"\frac{\tan(\alpha) + \tan(\beta)}{\sin(\alpha + \beta)} = "
				 r"\frac{\tfrac{1}{\cos(\alpha)}}{\sin(90-\beta)}", color = BLACK, font_size = 40)\
					 .shift(0.2 * DOWN)
		txt1_rep = MathTex(r"\frac{\tan(\alpha) + \tan(\beta)}{\sin(\alpha + \beta)} = "
				 r"\frac{\tfrac{1}{\cos(\alpha)}}{\cos(\beta)}", color = BLACK, font_size = 40)\
					 .shift(0.2 * DOWN)

		txt2 = MathTex(r"\frac{\tfrac{\sin(\alpha)}{\cos(\alpha)} + \tfrac{\sin(\beta)}{\cos(\beta)}}"
				r"{\sin(\alpha + \beta)} = \frac{1}{\cos(\alpha)\cos(\beta)}", color = BLACK,
				font_size = 40).next_to(txt1, DOWN)

		formula = MathTex(r"\sin(\alpha + \beta) = \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta)",
					color = BLACK, font_size = 40).next_to(txt2, DOWN)
		sur_box = SurroundingRectangle(formula).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(Transform(txt1, txt1_rep), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Write(formula), run_time = 2)
		self.play(Create(sur_box), run_time = 2)

		self.wait(2)

	def showa4(self):
		pa = Dot(5 * LEFT + 1.25 * UP, color = BLACK, radius = 0.05)
		pb = Dot(3 * RIGHT + 1.25 * UP, color = BLACK, radius = 0.05)
		pc = Dot(2 * LEFT + 3.25 * UP, color = BLACK, radius = 0.05)
		pd = Dot(2 * LEFT + 1.25 * UP, color = BLACK, radius = 0.05)
		points = VGroup(pa, pb, pc, pd)

		pa_t = MathTex(r"A", color = BLACK, font_size = 40).next_to(pa, LEFT).shift(RIGHT * 0.2)
		pb_t = MathTex(r"B", color = BLACK, font_size = 40).next_to(pb, RIGHT).shift(LEFT * 0.2)
		pc_t = MathTex(r"C", color = BLACK, font_size = 40).next_to(pc, UP).shift(DOWN * 0.2)
		pd_t = MathTex(r"D", color = BLACK, font_size = 40).next_to(pd, DOWN).shift(UP * 0.2)
		points_t = VGroup(pa_t, pb_t, pc_t, pd_t)
		
		l1 = Line(pa.get_center(), pd.get_center(), color = BLACK, stroke_width = 4)
		l2 = Line(pd.get_center(), pb.get_center(), color = BLACK, stroke_width = 4)
		l3 = Line(pa.get_center(), pc.get_center(), color = BLACK, stroke_width = 4)
		l4 = Line(pb.get_center(), pc.get_center(), color = BLACK, stroke_width = 4)
		l5 = Line(pc.get_center(), pd.get_center(), color = BLACK, stroke_width = 4)
		lines = VGroup(l1, l2, l3, l4, l5)

		ang_a = Angle(Line(pc, pa), Line(pc, pd), radius = 0.35, color = BLACK)
		ang_b = Angle(Line(pc, pd), Line(pc, pb), radius = 0.45, color = BLACK)
		ang_r1 = RightAngle(Line(pd, pa), Line(pd, pc), length = 0.2, color = BLACK)
		ang_r2 = RightAngle(Line(pd, pc), Line(pd, pb), length = 0.24, color = BLACK)
		angles = VGroup(ang_a, ang_b, ang_r1, ang_r2)

		ang_a_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_a, DOWN)\
			.shift(UP * 0.2 + LEFT * 0.15)
		ang_b_t = MathTex(r"\beta", color = BLACK, font_size = 35).next_to(ang_b, DOWN)\
			.shift(UP * 0.3 + RIGHT * 0.1)

		cd_t = MathTex(r"1", color = BLACK, font_size = 40).next_to(l5, RIGHT).shift(LEFT * 0.15)
		cd_t2 =	MathTex(r"CD = 1", color = BLACK, font_size = 50).next_to(l4, RIGHT).shift(RIGHT * 1)

		l1_t = MathTex(r"\tan(\alpha)", color = BLACK, font_size = 35).next_to(l1, DOWN).shift(UP * 0.15)
		l2_t = MathTex(r"\tan(\beta)", color = BLACK, font_size = 35).next_to(l2, DOWN).shift(UP * 0.15)
		l3_t = MathTex(r"\frac{1}{\cos(\alpha)}", color = BLACK, font_size = 35).next_to(l3, UP)\
			.shift(DOWN * 1.05 + LEFT * 0.3)
		l4_t = MathTex(r"\frac{1}{\cos(\beta)}", color = BLACK, font_size = 35).next_to(l4, UP)\
			.shift(DOWN * 1.15 + RIGHT * 0.3)
		marking = VGroup(l1_t, l2_t, l3_t, l4_t)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(angles, lag_ratio = 0), Write(ang_a_t), Write(ang_b_t), run_time = 2)
		self.wait(2)
		self.play(Write(cd_t), Write(cd_t2), run_time = 2)
		self.wait(2)
		self.play(Write(marking, lag_ratio = 0), run_time = 2)

		txt1 = MathTex(r"\tfrac{1}{\cos^2(\alpha)} + \tfrac{1}{\cos^2(\beta)} - 2\tfrac{\cos(\alpha + \beta)}"
				 r"{\cos(\alpha)\cos(\beta)} = (\tan(\alpha) + \tan(\beta))^2", color = BLACK,
				font_size = 40).shift(0.1 * DOWN)
		txt2 = MathTex(r"\tfrac{1}{\cos^2(\alpha)} + \tfrac{1}{\cos^2(\beta)} - 2\tfrac{\cos(\alpha + \beta)}"
				 r"{\cos(\alpha)\cos(\beta)} = \tan^2(\alpha) + 2\tan(\alpha)\tan(\beta) + \tan^2(\beta)",
				 color = BLACK, font_size = 40).next_to(txt1, DOWN)

		txt3 = MathTex(r"\cos^2(\beta) + \cos^2(\alpha) - 2\cos(\alpha + \beta)\cos(\alpha)\cos(\beta) = "
				 r"\sin^2(\alpha)\cos^2(\beta) + 2\sin(\alpha)\cos(\alpha)\sin(\beta)\cos(\beta) + "
				 r"\sin^2(\beta)\cos^2(\alpha)", color = BLACK, font_size = 25).next_to(txt2, DOWN)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(FadeOut(txt1), FadeOut(txt2), txt3.animate.shift(2 * UP), run_time = 2)
		self.wait(2)

		txt4 = MathTex(r"\cos^2(\beta)(1 - \sin^2(\alpha)) + \cos^2(\alpha)(1 - \sin^2(\beta)) - "
				 r"2\cos(\alpha + \beta)\cos(\alpha)\cos(\beta) = 2\sin(\alpha)\cos(\alpha)"
				 r"\sin(\beta)\cos(\beta)", color = BLACK, font_size = 30).next_to(txt3, DOWN)

		txt5 = MathTex(r"\cos^2(\beta)\cos^2(\alpha) + \cos^2(\alpha)\cos^2(\beta) - "
				 r"2\cos(\alpha + \beta)\cos(\alpha)\cos(\beta) = 2\sin(\alpha)\cos(\alpha)"
				 r"\sin(\beta)\cos(\beta)", color = BLACK, font_size = 33).next_to(txt4, DOWN)

		txt6 = MathTex(r"2\cos^2(\alpha)\cos^2(\beta) - 2\cos(\alpha + \beta)\cos(\alpha)\cos(\beta) = "
				 r"2\sin(\alpha)\cos(\alpha)\sin(\beta)\cos(\beta)", color = BLACK, font_size = 35)\
					 .next_to(txt5, DOWN)

		txt7 = MathTex(r"\cos(\alpha)\cos(\beta) - \cos(\alpha + \beta) = \sin(\alpha)\sin(\beta)",
				color = BLACK, font_size = 40).next_to(txt6, DOWN)

		formula = MathTex(r"\cos(\alpha + \beta) = \cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta)",
					color = BLACK, font_size = 45).next_to(txt7, DOWN).shift(DOWN * 0.2)
		sur_box = SurroundingRectangle(formula).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Write(txt6), run_time = 2)
		self.wait(2)
		self.play(Write(txt7), run_time = 2)
		self.wait(2)
		self.play(Write(formula), run_time = 2)
		self.play(Create(sur_box), run_time = 2)

		self.wait(2)

	def showa5(self):
		txt1 = MathTex(r"\sin(2\alpha) = 2\sin(\alpha)\cos(\alpha)", color = BLACK, font_size = 80)\
			.shift(UP * 2.7)
		sur_box1 = SurroundingRectangle(txt1).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		txt2 = MathTex(r"\cos(2\alpha) = \cos^2(\alpha) - \sin^2(\alpha)", color = BLACK, font_size = 80)\
			.next_to(txt1, DOWN).shift(0.4 * DOWN)
		sur_box2 = SurroundingRectangle(txt2).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		txt3 = MathTex(r"\sin(3\alpha) = 3\sin(\alpha) - 4\sin^3(\alpha)", color = BLACK, font_size = 80)\
			.next_to(txt2, DOWN).shift(0.4 * DOWN)
		sur_box3 = SurroundingRectangle(txt3).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		txt4 = MathTex(r"\cos(3\alpha) = 4\cos^3(\alpha) - 3\cos(\alpha)", color = BLACK, font_size = 80)\
			.next_to(txt3, DOWN).shift(0.4 * DOWN)
		sur_box4 = SurroundingRectangle(txt4).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.play(Create(sur_box1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.play(Create(sur_box2), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.play(Create(sur_box3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.play(Create(sur_box4), run_time = 2)

		self.wait(2)

	def showa6(self):
		txt1 = MathTex(r"\cos(\alpha) = \cos(\tfrac{\alpha}{2} + \tfrac{\alpha}{2}) = "
				  r"\cos^2(\tfrac{\alpha}{2}) - \sin^2(\tfrac{\alpha}{2})",
				  color = BLACK, font_size = 50).shift(UP * 2.5)

		txt2 = MathTex(r"\cos(\alpha) = \cos^2(\tfrac{\alpha}{2}) - (1 - \cos^2(\tfrac{\alpha}{2}))",
				  color = BLACK, font_size = 60).next_to(txt1, DOWN)

		txt3 = MathTex(r"\cos(\alpha) = 2\cos^2(\tfrac{\alpha}{2}) - 1", color = BLACK, font_size = 60)\
			.next_to(txt2, DOWN)

		txt4 = MathTex(r"1 + \cos(\alpha) = 2\cos^2(\tfrac{\alpha}{2})", color = BLACK, font_size = 60)\
			.next_to(txt3, DOWN)

		txt5 = MathTex(r"\cos^2(\tfrac{\alpha}{2}) = \tfrac{1 + \cos(\alpha)}{2}", color = BLACK,
				font_size = 60).next_to(txt4, DOWN).shift(DOWN * 0.2)
		sur_box_1 = SurroundingRectangle(txt5).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)
		sur_box_1_g = VGroup(sur_box_1, txt5)

		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.play(Create(sur_box_1), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt1), FadeOut(txt2), FadeOut(txt3), FadeOut(txt4),
		   sur_box_1_g.animate.shift(3 * UP), run_time = 2)

		txt6 = MathTex(r"1 - sin^2(\tfrac{\alpha}{2}) = \tfrac{1 + \cos(\alpha)}{2}", color = BLACK,
				font_size = 60).next_to(sur_box_1, DOWN).shift(DOWN * 0.2)

		txt7 = MathTex(r"\sin^2(\tfrac{\alpha}{2}) = \tfrac{-1 - \cos(\alpha)}{2} + 1", color = BLACK,
				font_size = 60).next_to(txt6, DOWN)

		txt8 = MathTex(r"\sin^2(\tfrac{\alpha}{2}) = \tfrac{1 - \cos(\alpha)}{2}", color = BLACK,
				font_size = 60).next_to(txt7, DOWN).shift(DOWN * 0.2)
		sur_box_2 = SurroundingRectangle(txt8).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)
		sur_box_2_g = VGroup(sur_box_2, txt8)

		self.wait(2)
		self.play(Write(txt6), run_time = 2)
		self.wait(2)
		self.play(Write(txt7), run_time = 2)
		self.wait(2)
		self.play(Write(txt8), run_time = 2)
		self.play(Create(sur_box_2), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt6), FadeOut(txt7), sur_box_2_g.animate.shift(2 * UP), run_time = 2)

		self.wait(2)

	def showa7(self):
		base1 = MathTex(r"\cos(\alpha - \beta) = \cos(\alpha)\cos(\beta) + \sin(\alpha)\sin(\beta)",
				  color = BLACK, font_size = 60).shift(UP * 3)
		base2 = MathTex(r"\cos(\alpha + \beta) = \cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta)",
				  color = BLACK, font_size = 60).next_to(base1, DOWN)

		f1_1 = MathTex(r"\cos(\alpha - \beta) + \cos(\alpha + \beta) = 2\cos(\alpha)\cos(\beta)",
				 color = BLACK, font_size = 60).next_to(base2, DOWN).shift(0.4 * DOWN)
		f1_2 = MathTex(r"\cos(\alpha)\cos(\beta) = \tfrac{\cos(\alpha - \beta) + \cos(\alpha + \beta)}{2}",
				 color = BLACK, font_size = 60).next_to(f1_1, DOWN)
		sur_box_f1 = SurroundingRectangle(f1_2).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)
		g1 = VGroup(f1_2, sur_box_f1)

		f2_1 = MathTex(r"\cos(\alpha - \beta) - \cos(\alpha + \beta) = 2\sin(\alpha)\sin(\beta)",
				 color = BLACK, font_size = 60).next_to(f1_2, DOWN).shift(0.4 * DOWN)
		f2_2 = MathTex(r"\sin(\alpha)\sin(\beta) = \tfrac{\cos(\alpha - \beta) - \cos(\alpha + \beta)}{2}",
				 color = BLACK, font_size = 60).next_to(f2_1, DOWN)
		sur_box_f2 = SurroundingRectangle(f2_2).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)
		g2 = VGroup(f2_2, sur_box_f2)

		self.wait(2)
		self.play(Write(base1), run_time = 2)
		self.play(Write(base2), run_time = 2)
		
		self.wait(2)
		self.play(Write(f1_1), run_time = 2)
		self.wait(2)
		self.play(Write(f1_2), run_time = 2)
		self.play(Create(sur_box_f1), run_time = 2)

		self.wait(2)
		self.play(Write(f2_1), run_time = 2)
		self.wait(2)
		self.play(Write(f2_2), run_time = 2)
		self.play(Create(sur_box_f2), run_time = 2)

		self.wait(2)
		self.play(FadeOut(base1), FadeOut(base2), FadeOut(f1_1), FadeOut(f2_1), g1.animate.shift(3.15 * UP),
			g2.animate.shift(4.15 * UP), run_time = 2)

		base3 = MathTex(r"\sin(\alpha + \beta) = \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta)",
				  color = BLACK, font_size = 60).next_to(sur_box_f2, DOWN).shift(DOWN * 0.4)
		base4 = MathTex(r"\sin(\alpha - \beta) = \sin(\alpha)\cos(\beta) - \cos(\alpha)\sin(\beta)",
				  color = BLACK, font_size = 60).next_to(base3, DOWN)

		f3_1 = MathTex(r"\sin(\alpha - \beta) + \sin(\alpha + \beta) = 2\sin(\alpha)\cos(\beta)",
				 color = BLACK, font_size = 60).next_to(base4, DOWN).shift(0.2 * DOWN)
		f3_2 = MathTex(r"\sin(\alpha)\cos(\beta) = \tfrac{\sin(\alpha + \beta) - \sin(\alpha + \beta)}{2}",
				 color = BLACK, font_size = 60).next_to(f3_1, DOWN)
		sur_box_f3 = SurroundingRectangle(f3_2).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)
		g3 = VGroup(f3_2, sur_box_f3)

		self.wait(2)
		self.play(Write(base3), run_time = 2)
		self.play(Write(base4), run_time = 2)
		self.wait(2)
		self.play(Write(f3_1), run_time = 2)
		self.wait(2)
		self.play(Write(f3_2), run_time = 2)
		self.play(Create(sur_box_f3), run_time = 2)

		self.wait(2)
		self.play(FadeOut(base3), FadeOut(base4), FadeOut(f3_1), g3.animate.shift(3.05 * UP), run_time = 2)

		self.wait(2)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()
		self.showa4()
		self.clearEverything()
		self.showa5()
		self.clearEverything()
		self.showa6()
		self.clearEverything()
		self.showa7()
		self.clearEverything()