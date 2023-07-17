from manim import *

class PythagoreanTheorem(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		pa = 0.5 * RIGHT - 2 * UP
		pb = 5.5 * LEFT + 2 * UP
		pc = 5.5 * LEFT - 2 * UP

		la = Line(pc, pb, color=BLUE, stroke_width = 6.0)
		lb = Line(pc, pa, color=GREEN, stroke_width = 6.0)
		lc = Line(pa, pb, color=RED, stroke_width = 6.0)
		lines = VGroup(la, lb, lc)

		r_a = RightAngle(la, lb, length = 0.35, other_angle = False, color=BLACK, stroke_width = 4.0)

		ta = MathTex(r"a", font_size = 80, color = BLUE).next_to(la, LEFT)
		tb = MathTex(r"b", font_size = 80, color = GREEN).next_to(lb, DOWN)
		tc = MathTex(r"c", font_size = 80, color = RED).next_to(lc, UP).shift(2 * DOWN)
		texts = VGroup(ta, tb, tc)

		formula = MathTex(r"\textcolor{blue}{a}^2 + \textcolor{green}{b}^2 = \textcolor{red}{c}^2",
				   font_size = 100, tex_template = myTemplate, color = BLACK).next_to(lines, RIGHT)

		self.wait(3)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(r_a), run_time = 2)
		self.wait(2)
		self.play(Write(texts), run_time = 2)
		self.wait(2)
		
		self.play(Write(formula), run_time = 2)

		self.wait(3)

	def showa2(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")
		
		pa = -1 * UP
		pb = 4 * LEFT + 2 * UP
		pc = 4 * LEFT - 1 * UP

		la = Line(pc, pb, color=BLUE, stroke_width = 6.0)
		lb = Line(pc, pa, color=GREEN, stroke_width = 6.0)
		lc = Line(pa, pb, color=RED, stroke_width = 6.0)
		lines = VGroup(la, lb, lc)

		r_a = RightAngle(la, lb, length = 0.35, color=BLACK, stroke_width = 4.0)

		ta = MathTex(r"a = 3", font_size = 60, color = BLUE).next_to(la, LEFT)
		tb = MathTex(r"b = 4", font_size = 60, color = GREEN).next_to(lb, DOWN)
		tc = MathTex(r"c", font_size = 60, color = RED).next_to(lc, UP).shift(1.5 * DOWN)
		texts = VGroup(ta, tb, tc)

		formula1 = MathTex(r"\textcolor{blue}{a}^2 + \textcolor{green}{b}^2 = \textcolor{red}{c}^2",
				   font_size = 80, tex_template = myTemplate, color = BLACK).shift(3.5 * RIGHT + 2.5 * UP)
		formula2 = MathTex(r"\textcolor{blue}{3}^2 + \textcolor{green}{4}^2 = \textcolor{red}{c}^2",
				   font_size = 80, tex_template = myTemplate, color = BLACK).next_to(formula1, DOWN)
		formula3 = MathTex(r"9 + 16 = \textcolor{red}{c}^2", font_size = 80, tex_template = myTemplate,
					color = BLACK).next_to(formula2, DOWN)
		formula4 = MathTex(r"25 = \textcolor{red}{c}^2", font_size = 80, tex_template = myTemplate,
					color = BLACK).next_to(formula3, DOWN)
		formula5 = MathTex(r"\textcolor{red}{c} = 5", font_size = 80, tex_template = myTemplate,
					color = BLACK).next_to(formula4, DOWN)

		self.wait(3)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)
		self.play(Create(r_a), run_time = 2)
		self.play(Write(texts), run_time = 2)
		self.wait(2)

		self.play(Write(formula1), run_time = 2)
		self.wait(2)
		self.play(Write(formula2), run_time = 2)
		self.wait(2)
		self.play(Write(formula3), run_time = 2)
		self.wait(2)
		self.play(Write(formula4), run_time = 2)
		self.wait(2)
		self.play(Write(formula5), run_time = 2)

		self.wait(3)

	def showa3(self):
		gScale = 0.65
		a = ValueTracker(3 * gScale)
		b = ValueTracker(6 * gScale)

		baseLineA = Line(start = ORIGIN, end = UP * a.get_value(), color = BLUE, stroke_width = 5.0)
		baseLineB = Line(start = ORIGIN, end = RIGHT * b.get_value(), color = GREEN, stroke_width = 5.0)
		baseLineC = Line(start = RIGHT * b.get_value(), end = UP * a.get_value(), color = RED,
				  stroke_width=5.0)

		baseAngle = always_redraw(
			lambda : RightAngle(line1 = baseLineA, line2 = baseLineB, other_angle = True, length = 0.25,
					  color = BLACK))

		textA = always_redraw(lambda : Text(text = "a", color = BLUE).next_to(baseLineA, LEFT))
		textB = always_redraw(lambda : Text(text = "b", color = GREEN).next_to(baseLineB, DOWN))
		textC = always_redraw(lambda : Text(text = "c=???", color = RED).next_to(baseLineC, ORIGIN)\
			.shift(UP * 0.4 + RIGHT * 0.6))

		baseGroup = VGroup(baseLineA, baseLineB, baseLineC)

		self.wait(3)
		self.play(Create(baseLineA), Write(textA), run_time = 2)
		self.play(Create(baseLineB), Write(textB), run_time = 2)
		self.play(Create(baseAngle), run_time = 2)
		self.play(Create(baseLineC), Write(textC), run_time = 2)
		self.play(baseGroup.animate.to_edge(LEFT + UP).shift(RIGHT * 1.5), run_rime = 2)
		self.wait(2)
		textC_alternative = always_redraw(lambda : Text(text="c", color=RED).next_to(baseLineC, ORIGIN)\
			.shift(UP * 0.4 + RIGHT * 0.2))
		self.play(ReplacementTransform(textC, textC_alternative), run_time = 1)
		textC = textC_alternative
		self.wait(3)

		triangle1 = baseGroup.copy()
		triangle1.target = triangle1.copy().move_to(ORIGIN).shift(DOWN * 2 + RIGHT * 2.5)
		triangle1.target.add(Polygon(triangle1.target.get_corner(DR), triangle1.target.get_corner(DL),
							  triangle1.target.get_corner(UL), color = YELLOW, fill_opacity = 0.075)\
								  .set_stroke(opacity = 0.0))
		self.play(Transform(triangle1, triangle1.target), run_time=2)

		triangle2 = baseGroup.copy()
		triangle2.target = triangle1.copy().rotate(-PI / 2, about_point = triangle1.get_corner(DR))\
			.next_to(triangle1, UP, buff = 0).align_to(triangle1, LEFT)
		self.play(Transform(triangle2, triangle2.target), run_time=2)

		triangle3 = baseGroup.copy()
		triangle3.target = triangle2.copy().rotate(-PI / 2, about_point=triangle2.get_corner(UR)) \
			.next_to(triangle2, RIGHT, buff=0).align_to(triangle2, UP)
		self.play(Transform(triangle3, triangle3.target), run_time=2)

		triangle4 = baseGroup.copy()
		triangle4.target = triangle3.copy().rotate(-PI / 2, about_point=triangle3.get_corner(DR)) \
			.next_to(triangle3, DOWN, buff=0).align_to(triangle3, RIGHT)
		self.play(Transform(triangle4, triangle4.target), run_time=2)
		self.wait(0.5)

		bigRightA_1 = RightAngle(
				line1 = Line(start = triangle1[2].get_end(), end = triangle1[2].get_start()),
				line2 = Line(start = triangle2[2].get_start(), end = triangle2[2].get_end()),
				length=0.25, color=BLACK)
		bigRightA_2 = RightAngle(
				line1=Line(start=triangle2[2].get_end(), end=triangle2[2].get_start()),
				line2=Line(start=triangle3[2].get_start(), end=triangle3[2].get_end()),
				length=0.25, color=BLACK)
		bigRightA_3 = RightAngle(
				line1=Line(start=triangle3[2].get_end(), end=triangle3[2].get_start()),
				line2=Line(start=triangle4[2].get_start(), end=triangle4[2].get_end()),
				length=0.25, color=BLACK)
		bigRightA_4 = RightAngle(
				line1=Line(start=triangle4[2].get_end(), end=triangle4[2].get_start()),
				line2=Line(start=triangle1[2].get_start(), end=triangle1[2].get_end()),
				length=0.25, color=BLACK)
		bigRightA_P = Polygon(triangle1.get_corner(UL), triangle2.get_corner(UR), triangle3.get_corner(DR),
					   triangle4.get_corner(DL), color = RED, fill_opacity = 0.1)

		bigRightAnglesG = VGroup(bigRightA_1, bigRightA_2, bigRightA_3, bigRightA_4, bigRightA_P)

		self.play(Create(bigRightA_1), Create(bigRightA_2), Create(bigRightA_3), Create(bigRightA_4),
		   run_time = 2)
		self.play(Create(bigRightA_P), run_time = 3)

		bigTextGroup = VGroup(
			Text("a", color = BLUE).next_to(triangle1[0], LEFT),
			Text("a", color = BLUE).next_to(triangle2[0], UP),
			Text("b", color = GREEN).next_to(triangle2[1], LEFT),
			Text("b", color = GREEN).next_to(triangle3[1], UP),
			Text("c", color = RED).next_to(triangle1[2], ORIGIN).shift(UP * 0.3 + RIGHT * 0.1),
			Text("c", color = RED).next_to(triangle2[2], ORIGIN).shift(DOWN * 0.1 + RIGHT * 0.3))
		self.play(Write(bigTextGroup, lag_ratio = 0), run_time = 2)
		self.wait(3)

		scaleFormula = 0.18
		scaleTextFormula = 0.7
		f2_scale = 0.7

		f1_p1 = VGroup(*triangle1.copy(), *triangle2.copy(), *triangle3.copy(), *triangle4.copy(), *bigRightAnglesG.copy())
		f1_p1.target = f1_p1.copy().scale(scaleFormula).next_to(textB, DOWN).to_edge(LEFT)
		self.play(Transform(f1_p1, f1_p1.target), run_time = 2)
		
		f1_pE = Text("=", color = BLACK).scale(scaleTextFormula).next_to(f1_p1, RIGHT, buff = 0.1)
		self.play(Write(f1_pE), run_time = 0.5)
		
		f1_p2 = triangle1.copy()
		f1_p2.target = triangle1.copy().scale(scaleFormula).next_to(f1_pE, RIGHT, buff = 0.1)
		self.play(Transform(f1_p2, f1_p2.target), run_time = 2)
		
		f1_pA1 = Text("+", color=BLACK).scale(scaleTextFormula).next_to(f1_p2, RIGHT, buff=0.1)
		self.play(Write(f1_pA1), run_time = 0.5)
		
		f1_p3 = triangle2.copy()
		f1_p3.target = triangle2.copy().scale(scaleFormula).next_to(f1_pA1, RIGHT, buff=0.1)
		self.play(Transform(f1_p3, f1_p3.target), run_time = 2)
		
		f1_pA2 = Text("+", color=BLACK).scale(scaleTextFormula).next_to(f1_p3, RIGHT, buff=0.1)
		self.play(Write(f1_pA2), run_time = 0.5)
		
		f1_p4 = triangle3.copy()
		f1_p4.target = triangle3.copy().scale(scaleFormula).next_to(f1_pA2, RIGHT, buff=0.1)
		self.play(Transform(f1_p4, f1_p4.target), run_time = 2)
		
		f1_pA3 = Text("+", color=BLACK).scale(scaleTextFormula).next_to(f1_p4, RIGHT, buff=0.1)
		self.play(Write(f1_pA3), run_time = 0.5)
		
		f1_p5 = triangle4.copy()
		f1_p5.target = triangle4.copy().scale(scaleFormula).next_to(f1_pA3, RIGHT, buff=0.1)
		self.play(Transform(f1_p5, f1_p5.target), run_time = 2)
		
		f1_pA4 = Text("+", color=BLACK).scale(scaleTextFormula).next_to(f1_p5, RIGHT, buff=0.1)
		self.play(Write(f1_pA4), run_time = 0.5)
		
		f1_p6 = bigRightAnglesG.copy()
		f1_p6.target = bigRightAnglesG.copy().scale(scaleFormula).next_to(f1_pA4, RIGHT, buff=0.1)
		self.play(Transform(f1_p6, f1_p6.target), run_time = 2)
		self.wait(2)

		f2 = VGroup(*f1_p1.copy(), *f1_p2.copy(), *f1_p3.copy(), *f1_p4.copy(), *f1_p5.copy(), *f1_p6.copy())
		f2.target = MathTex("(a+b)^2", "=", "\\frac{ab}{2}", "+", "\\frac{ab}{2}", "+", "\\frac{ab}{2}",
					 "+", "\\frac{ab}{2}", "+", "c^2").set_color(BLACK).scale(f2_scale)\
						 .next_to(f1_pA2, DOWN).shift(DOWN * 0.3)
		self.play(Write(f2), MoveToTarget(f2), run_time = 2)
		self.wait(2)

		f3 = f2.copy()
		f3.target = MathTex("a^2", "+", "2ab", "+", "b^2", "=", "2ab", "+", "c^2")\
			.set_color(BLACK).scale(f2_scale).next_to(f2, DOWN).shift(DOWN * 0.1)
		self.play(Write(f3), MoveToTarget(f3), run_time = 2)
		self.wait(2)

		f4 = f3.copy()
		f4.target = MathTex("a^2", "+", "b^2", "=", "c^2").set_color(BLACK).scale(2.1)\
			.next_to(f3, DOWN).shift(DOWN * 0.25)

		f4_box = SurroundingRectangle(f4.target).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width=4)

		self.play(Write(f4), MoveToTarget(f4), run_time = 2)
		self.play(Create(f4_box), run_time = 2)

		self.wait(3)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()