from manim import *


class ExtraVid10(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		t1 = MathTex(r"1", font_size=130, color=BLACK).shift(LEFT * 5)
		t2 = MathTex(r"+ 2", font_size=130, color=BLACK).next_to(t1, RIGHT, buff=0.2).shift(0.01*DOWN)
		t3 = MathTex(r"+ 3", font_size=130, color=BLACK).next_to(t2, RIGHT, buff=0.2)
		t4 = MathTex(r"+ 4", font_size=130, color=BLACK).next_to(t3, RIGHT, buff=0.2)
		t5 = MathTex(r"+ 5", font_size=130, color=BLACK).next_to(t4, RIGHT, buff=0.2)
		t_etc = MathTex(r"+ \cdots", font_size=130, color=BLACK).next_to(t5, RIGHT, buff=0.2)\
			.shift(0.05*DOWN)

		self.wait(1)
		self.play(Write(t1))
		self.wait(0.5)
		self.play(Write(t2))
		self.wait(0.5)
		self.play(Write(t3))
		self.wait(0.5)
		self.play(Write(t4))
		self.wait(0.5)
		self.play(Write(t5))
		self.wait(0.5)
		self.play(Write(t_etc))
		self.wait(3)

	def showa2(self):
		eq1 = MathTex(r"S = 1 + 2 + 3 + 4 + 5 + \cdots", font_size=52, color=BLACK)\
			.shift(LEFT * 2 + UP * 3.1)

		eq2 = MathTex(r"A = 1 - 1 + 1 - 1 + 1 - 1 \cdots", font_size=52, color=BLACK)\
			.next_to(eq1, DOWN, buff=1).align_to(eq1, LEFT)
		eq3 = MathTex(r"A = 1 - (1 - 1 + 1 - 1 + 1 \cdots)", font_size=52, color=BLACK)\
			.next_to(eq2, DOWN, buff=0.3).align_to(eq2, LEFT)
		eq4 = MathTex(r"A = 1 - A", font_size=52, color=BLACK).next_to(eq3, DOWN, buff=0.3)\
			.align_to(eq3, LEFT)
		eq5 = MathTex(r"2 \cdot A = 1", font_size=52, color=BLACK).next_to(eq4, DOWN, buff=0.3)\
			.align_to(eq4, LEFT)
		eq6 = MathTex(r"A = \tfrac{1}{2}", font_size=52, color=BLACK).next_to(eq5, DOWN, buff=0.3)\
			.align_to(eq5, LEFT)

		self.wait(1)
		self.play(Write(eq1))
		self.wait(2)
		self.play(Write(eq2))
		self.wait(2)
		self.play(Write(eq3))
		self.wait(2)
		self.play(Write(eq4))
		self.wait(0.5)
		self.play(Write(eq5))
		self.wait(0.5)
		self.play(Write(eq6))
		self.wait(2)

		self.play(FadeOut(eq3), FadeOut(eq4), FadeOut(eq5), run_time=1)
		self.play(eq2.animate.shift(UP * 0.6), eq6.animate.shift(UP * 3.03), run_time=1)
		self.wait(2)

		eq7 = MathTex(r"B = 1 - 2 + 3 - 4 + 5 - 6 \cdots", font_size=52, color=BLACK)\
			.next_to(eq6, DOWN, buff=0.5).align_to(eq6, LEFT)
		eq8 = MathTex(r"B = \quad\:\:\,\, 1 - 2 + 3 - 4 + 5 \cdots", font_size=52, color=BLACK)\
			.next_to(eq7, DOWN, buff=0.15).align_to(eq7, LEFT)
		eq9 = MathTex(r"B + B = 1 - 1 + 1 - 1 + 1 - 1 \cdots", font_size=52, color=BLACK)\
			.next_to(eq8, DOWN, buff=0.2).align_to(eq8, LEFT)
		eq10 = MathTex(r"2 \cdot B = A", font_size=52, color=BLACK)\
			.next_to(eq9, DOWN, buff=0.2).align_to(eq9, LEFT)
		eq11 = MathTex(r"2 \cdot B = \tfrac{1}{2}", font_size=52, color=BLACK)\
			.next_to(eq10, DOWN, buff=0.2).align_to(eq10, LEFT)
		eq12 = MathTex(r"B = \tfrac{1}{4}", font_size=52, color=BLACK)\
			.next_to(eq11, DOWN, buff=0.1).align_to(eq11, LEFT)

		self.play(Write(eq7))
		self.wait(1)
		self.play(Write(eq8))
		self.wait(2)
		self.play(Write(eq9))
		self.wait(2)
		self.play(Write(eq10))
		self.wait(0.5)
		self.play(Write(eq11))
		self.wait(0.5)
		self.play(Write(eq12))
		self.wait(2)

		self.play(FadeOut(eq8), FadeOut(eq9), FadeOut(eq10), FadeOut(eq11), run_time=1)
		self.play(eq7.animate.shift(UP * 0.2), eq12.animate.shift(UP * 2.83), run_time=1)
		self.wait(2)

		eq13 = MathTex(r"S = 1 + 2 + 3 + 4 + 5 + 6 \cdots", font_size=52, color=BLACK)\
			.next_to(eq12, DOWN, buff=0.4).align_to(eq12, LEFT)
		eq14 = MathTex(r"B = 1 - 2 + 3 - 4 + 5 - 6 \cdots", font_size=52, color=BLACK)\
			.next_to(eq13, DOWN, buff=0.1).align_to(eq13, LEFT).shift(LEFT * 0.05)

		eq15 = MathTex(r"S - B = 4 + 8 + 12 + 16 \cdots", font_size=52, color=BLACK)\
			.next_to(eq14, DOWN, buff=0.2).align_to(eq14, LEFT)
		eq16 = MathTex(r"S - B = 4 \cdot (1 + 2 + 3 + 4 \cdots)", font_size=52, color=BLACK)\
			.next_to(eq15, DOWN, buff=0.2).align_to(eq15, LEFT)
		eq17 = MathTex(r"S - B = 4 \cdot S", font_size=52, color=BLACK)\
			.next_to(eq16, DOWN, buff=0.2).align_to(eq16, LEFT)
		
		self.play(Write(eq13))
		self.wait(0.5)
		self.play(Write(eq14))
		self.wait(2)
		self.play(Write(eq15))
		self.wait(2)
		self.play(Write(eq16))
		self.wait(1)
		self.play(Write(eq17))
		self.wait(1)

		self.play(FadeOut(eq13), FadeOut(eq14), FadeOut(eq15), FadeOut(eq16), run_time=0.5)
		self.play(eq17.animate.shift(UP * 2.5), run_time=0.5)
		self.wait(1)

		eq18 = MathTex(r"-3 \cdot S = B", font_size=52, color=BLACK)\
			.next_to(eq17, DOWN, buff=0.15).align_to(eq17, LEFT)
		eq19 = MathTex(r"S = \tfrac{-B}{3}", font_size=52, color=BLACK)\
			.next_to(eq18, DOWN, buff=0.15).align_to(eq18, LEFT)

		eq20 = MathTex(r"S = -\tfrac{1}{12}", font_size=52, color=BLACK)\
			.next_to(eq19, DOWN, buff=0.25).align_to(eq19, LEFT)

		self.play(Write(eq18))
		self.wait(0.5)
		self.play(Write(eq19))
		self.wait(1)
		self.play(Write(eq20))
		self.wait(0.5)

		self.play(FadeOut(eq17), FadeOut(eq18), FadeOut(eq19), run_time=0.5)
		self.play(eq20.animate.shift(UP * 2), run_time=0.5)
		self.wait(0.25)

		sur_box = SurroundingRectangle(eq20, buff=0.15)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=3)

		self.play(Create(sur_box), run_time=1)
		self.wait(4)


	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()

