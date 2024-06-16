from manim import *

class QuadraticFormula(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		eq1 = MathTex(r"ax^2 + bx + c = 0", font_size = 120, color = BLACK).shift(2*UP)
		eq2 = MathTex(r"D=b^2-4ax", font_size = 80, color = BLACK).next_to(eq1, DOWN)
		eqx1 = MathTex(r"x_1=\dfrac{-b+\sqrt{D}}{2a}", font_size = 50, color = BLACK)
		eqx2 = MathTex(r"x_2=\dfrac{-b-\sqrt{D}}{2a}", font_size = 50, color = BLACK)
		xgroup = VGroup(eqx1, eqx2).arrange(RIGHT, buff = 1).next_to(eq2, DOWN)

		self.wait(3)
		self.play(Write(VGroup(eq1, eq2)), run_time = 2)
		self.wait(2)
		self.play(Write(eqx1), Write(eqx2), run_time = 2)
		self.wait(3)

	def showa2(self):
		eq = MathTex(r"ax^2 + bx + c = 0", font_size = 100, color = BLACK).shift(2.5 * UP)
		eq_exmpl = MathTex(r"2x^2 - 3x - 2 = 0", font_size = 70, color = BLACK).next_to(eq, DOWN).shift(DOWN)
		
		exmpl1_1 = MathTex(r"x_1=2", font_size = 50, color = BLACK)
		exmpl2_1 = MathTex(r"x_2=-\tfrac{1}{2}", font_size = 50, color = BLACK)
		xgroup = VGroup(exmpl1_1, exmpl2_1).arrange(RIGHT, buff = 4).next_to(eq_exmpl, DOWN)

		exmpl1_2 = MathTex(r"2\cdot2^2 - 3\cdot2 - 2 = 0", font_size = 40, color = BLACK).next_to(exmpl1_1, DOWN)
		exmpl1_3 = MathTex(r"8 - 6 - 2 = 0", font_size = 40, color = BLACK).next_to(exmpl1_2, DOWN)
		exmpl1_4 = MathTex(r"0 = 0", font_size = 40, color = BLACK).next_to(exmpl1_3, DOWN)

		exmpl2_2 = MathTex(r"2\cdot(\tfrac{-1}{2})^2 - 3\cdot\tfrac{-1}{2} - 2 = 0", font_size = 40,
				color = BLACK).next_to(exmpl2_1, DOWN)
		exmpl2_3 = MathTex(r"\tfrac{1}{2} + \tfrac{3}{2} - 2 = 0", font_size = 40,
				color = BLACK).next_to(exmpl2_2, DOWN)
		exmpl2_4 = MathTex(r"0 = 0", font_size = 40, color = BLACK).next_to(exmpl2_3, DOWN)

		self.wait(3)
		self.play(Write(eq), run_time = 2)
		self.wait(2)
		self.play(Write(eq_exmpl), run_time = 2)
		self.wait(2)

		self.play(Write(exmpl1_1), Write(exmpl2_1), run_time = 2)
		self.wait(2)

		self.play(Write(exmpl1_2), Write(exmpl2_2), run_time = 1)
		self.play(Write(exmpl1_3), Write(exmpl2_3), run_time = 1)
		self.play(Write(exmpl1_4), Write(exmpl2_4), run_time = 1)
		self.wait(3)

	def showa3(self):
		font_sz = 50

		step1_eq = MathTex(r"ax^2 + bx + c = 0", font_size = font_sz + 10, color = BLACK).shift(3 * UP)
		step2_eq = MathTex(r"4a^2x^2 + 4abx + 4ac = 0", font_size = font_sz, color = BLACK)\
			.next_to(step1_eq, DOWN)
		step3_eq = MathTex(r"4a^2x^2 + 4abx + b^2 - b^2 + 4ac = 0", font_size = font_sz, color = BLACK)\
			.next_to(step2_eq, DOWN)
		step4_eq = MathTex(r"(2ax + b)^2 - b^2 + 4ac = 0", font_size = font_sz, color = BLACK)\
			.next_to(step3_eq, DOWN)
		step5_eq = MathTex(r"(2ax + b)^2 = b^2 - 4ac", font_size = font_sz, color = BLACK)\
			.next_to(step4_eq, DOWN)
		step6_eq = MathTex(r"2ax + b = \pm\sqrt{b^2 - 4ac}", font_size = font_sz, color = BLACK)\
			.next_to(step5_eq, DOWN)
		step7_eq = MathTex(r"x = \frac{-b\pm\sqrt{b^2 - 4ac}}{2a}", font_size = font_sz, color = BLACK)\
			.next_to(step6_eq, DOWN)

		eq1_extra = MathTex(r"\vert \cdot4a", font_size = font_sz, color = BLACK).next_to(step1_eq, RIGHT)\
			.shift(2 * RIGHT)
		eq2_extra = MathTex(r"\vert +b^2-b^2", font_size = font_sz, color = BLACK).next_to(step2_eq, RIGHT)\
			.align_to(eq1_extra, LEFT)

		steps = [step1_eq, step2_eq, step3_eq, step4_eq, step5_eq, step6_eq, step7_eq]

		sur_rec1 = SurroundingRectangle(step7_eq, buff=0.1)
		sur_rec1.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)
		sol1 = VGroup(step7_eq, sur_rec1)

		self.wait(3)

		for i, step in enumerate(steps):
			if i == 0:
				self.play(Write(step), run_time = 2)
				self.wait(2)
				self.play(Write(eq1_extra), run_time = 2)
				self.wait(2)
			else:
				self.play(TransformFromCopy(steps[i - 1], step), run_time = 2)
				self.wait(2)
				if i == 1:
					self.play(Write(eq2_extra), run_time = 2)
					self.wait(2)

		self.play(Create(sur_rec1), run_time = 2)
		self.wait(2)

		self.play(FadeOut(VGroup(*steps[1:-1], eq1_extra, eq2_extra)), run_time = 2)
		self.wait(2)

		self.play(sol1.animate.shift(3.3 * UP), run_time = 2)
		self.wait(2)

		step8_eq = MathTex(r"D = b^2 - 4ac", font_size = font_sz, color = BLACK).next_to(sur_rec1, DOWN)\
			.shift(0.5 * DOWN)
		step9_eq = MathTex(r"x = \frac{-b\pm\sqrt{D}}{2a}", font_size = font_sz, color = BLACK)\
			.next_to(step8_eq, DOWN)
		sur_rec2 = SurroundingRectangle(step9_eq, buff=0.1)
		sur_rec2.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		self.play(Write(step8_eq), run_time = 2)
		self.play(Write(step9_eq), run_time = 2)
		self.play(Create(sur_rec2), run_time = 2)

		self.wait(3)
		
	def construct(self):
		self.camera.background_color = WHITE
		
		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()