from manim import *

class ExtraVid6(ThreeDScene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		eq1 = MathTex(r"V_3 = \tfrac{1}{3} h \pi \left(\tfrac{3}{3}r\right) ^{2} + "
				r"\tfrac{1}{3} h \pi \left(\tfrac{2}{3}r\right) ^{2} + "
				r"\tfrac{1}{3} h \pi \left(\tfrac{1}{3}r\right) ^{2}", font_size=38,
				color=BLACK).shift(2.5 * UP + 2.8 * LEFT)
		eq2 = MathTex(r"V_4 = \tfrac{1}{4} h \pi \left(\tfrac{4}{4}r\right) ^{2} + "
				r"\tfrac{1}{4} h \pi \left(\tfrac{3}{4}r\right) ^{2} + "
				r"\tfrac{1}{4} h \pi \left(\tfrac{2}{4}r\right) ^{2} + "
				r"\tfrac{1}{4} h \pi \left(\tfrac{1}{4}r\right) ^{2}", font_size=38,
				color=BLACK).next_to(eq1, DOWN, aligned_edge=LEFT, buff=0.4)
		eq3 = MathTex(r"V_5 = \tfrac{1}{5} h \pi \left(\tfrac{5}{5}r\right) ^{2} + "
				r"\tfrac{1}{5} h \pi \left(\tfrac{4}{5}r\right) ^{2} + "
				r"\tfrac{1}{5} h \pi \left(\tfrac{3}{5}r\right) ^{2} + "
				r"\tfrac{1}{5} h \pi \left(\tfrac{2}{5}r\right) ^{2} + ", font_size=38,
                color=BLACK).next_to(eq2, DOWN, aligned_edge=LEFT, buff=0.4)
		eq3_2 = MathTex(r"\tfrac{1}{5} h \pi \left(\tfrac{1}{5}r\right) ^{2}", font_size=38, color=BLACK)\
			.next_to(eq3, DOWN, aligned_edge=LEFT, buff=0.1).shift(0.96 * RIGHT)
		eq4 = MathTex(r"V_6 = \tfrac{1}{6} h \pi \left(\tfrac{6}{6}r\right) ^{2} + "
				r"\tfrac{1}{6} h \pi \left(\tfrac{5}{6}r\right) ^{2} + "
				r"\tfrac{1}{6} h \pi \left(\tfrac{4}{6}r\right) ^{2} + "
				r"\tfrac{1}{6} h \pi \left(\tfrac{3}{6}r\right) ^{2} + ", font_size=38,
				color=BLACK).next_to(eq3_2, DOWN, buff=0.4).align_to(eq3, LEFT)
		eq4_2 = MathTex(r"\tfrac{1}{6} h \pi \left(\tfrac{2}{6}r\right) ^{2} + "
				r"\tfrac{1}{6} h \pi \left(\tfrac{1}{6}r\right) ^{2}", font_size=38, color=BLACK)\
					.next_to(eq4, DOWN, aligned_edge=LEFT, buff=0.1).shift(0.96 * RIGHT)

		self.wait(1)
		self.play(Write(eq2), run_time = 2)
		self.wait(4)
		self.play(Write(eq1), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq3), run_time = 1)
		self.play(Write(eq3_2), run_time = 0.25)
		self.wait(0.5)
		self.play(Write(eq4), run_time = 1)
		self.play(Write(eq4_2), run_time = 0.5)
		self.wait(4)

	def showa2(self):
		eq1 = MathTex(r"V_n = \tfrac{1}{n} h \pi \left(\tfrac{1}{n}r\right) ^{2} + "
				r"\tfrac{1}{n} h \pi \left(\tfrac{2}{n}r\right) ^{2} + \cdots +"
				r"\tfrac{1}{n} h \pi \left(\tfrac{n-1}{n}r\right) ^{2} +"
				r"\tfrac{1}{n} h \pi \left(\tfrac{n}{n}r\right) ^{2} +", font_size=38,
				color=BLACK).shift(2 * UP + 0.5 * LEFT)

		eq2 = MathTex(r"V_n = \tfrac{1}{n} h \pi \left( \left(\tfrac{1}{n}r\right) ^{2} + "
				r"\left(\tfrac{2}{n}r\right) ^{2} + \cdots + \left(\tfrac{n-1}{n}r\right) ^{2} +"
				r"\left(\tfrac{n}{n}r\right) ^{2} \right)", font_size=38, color=BLACK)\
					.next_to(eq1, DOWN, aligned_edge=LEFT, buff=0.4)

		eq3 = MathTex(r"V_n = \tfrac{1}{n} h \pi \left( \tfrac{1^2 r^2}{n^2} + \tfrac{2^2 r^2}{n^2}"
				r" + \cdots + \tfrac{(n-1)^2 r^2}{n^2} + \tfrac{n^2 r^2}{n^2} \right)", font_size=38,
				color=BLACK).next_to(eq2, DOWN, aligned_edge=LEFT, buff=0.4)

		eq4 = MathTex(r"V_n = \tfrac{h \pi r^2}{n^3} \left( 1^2 + 2^2 + \cdots + (n-1)^2 + n^2 \right)",
				font_size=38, color=BLACK).next_to(eq3, DOWN, aligned_edge=LEFT, buff=0.4)

		self.wait(1)
		self.play(Write(eq1), run_time = 2)
		self.wait(1)
		self.play(Write(eq2), run_time = 1)
		self.wait(1)
		self.play(Write(eq3), run_time = 1)
		self.wait(1)
		self.play(Write(eq4), run_time = 1)
		self.wait(2)
		self.play(FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), run_time = 1)
		self.play(eq4.animate.shift(3 * UP), run_time = 1)
		self.wait(2)

		eq5 = MathTex(r"1^2 + 2^2 + \cdots + (n-1)^2 + n^2 = \tfrac{n^3}{3} + \tfrac{n^2}{2} + "
				r"\tfrac{n}{6}", font_size=38, color=BLACK).next_to(eq4, DOWN, aligned_edge=LEFT, buff=0.4)

		eq6 = MathTex(r"V_n = \tfrac{h \pi r^2}{n^3} \left( \tfrac{n^3}{3} + \tfrac{n^2}{2} + "
				r"\tfrac{n}{6} \right)", font_size=38, color=BLACK).next_to(eq5, DOWN, aligned_edge=LEFT,
																buff=0.4)

		eq7 = MathTex(r"V_n = \pi h r^2 \left( \tfrac{1}{3} + \tfrac{1}{2n} + \tfrac{1}{6n^2} \right)",
				font_size=38, color=BLACK).next_to(eq6, DOWN, aligned_edge=LEFT, buff=0.4)

		self.play(Write(eq5), run_time = 1)
		self.wait(1)
		self.play(Write(eq6), run_time = 1)
		self.wait(1)
		self.play(Write(eq7), run_time = 1)
		self.wait(2)
		self.play(FadeOut(eq4), FadeOut(eq5), FadeOut(eq6), run_time = 1)
		self.play(eq7.animate.shift(3 * UP), run_time = 1)
		self.wait(3)

		eq8 = MathTex(r"V_{\infty} = \pi h r^2 \left( \tfrac{1}{3} + 0 + 0 \right)", font_size=38,
				color=BLACK).next_to(eq7, DOWN, aligned_edge=LEFT, buff=0.4)

		eq9 = MathTex(r"V = \tfrac{1}{3} \pi h r^2", font_size=38, color=BLACK)\
			.next_to(eq8, DOWN, aligned_edge=LEFT, buff=0.4)
		sur_box = SurroundingRectangle(eq9, buff=0.15)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		self.play(Write(eq8), run_time = 1)
		self.wait(1)
		self.play(Write(eq9), run_time = 1)
		self.play(Create(sur_box), run_time = 1)
		self.wait(4)

	def showa3(self):
		eq1 = MathTex(r"h = 2000", font_size=54, color=BLACK).shift(2.25 * UP + 4.5 * LEFT)
		eq2 = MathTex(r"r = 4500", font_size=54, color=BLACK)\
			.next_to(eq1, DOWN, aligned_edge=LEFT, buff=0.2)

		eq3 = MathTex(r"V = \tfrac{1}{3} \pi h r^2", font_size=54, color=BLACK)\
			.next_to(eq2, DOWN, aligned_edge=LEFT, buff=0.5)
		
		eq4 = MathTex(r"V = \tfrac{1}{3} \pi (2000) (4500)^2 \approx 42500000000", font_size=54,
				color=BLACK).next_to(eq3, DOWN, aligned_edge=LEFT, buff=0.5)

		self.wait(1)
		self.play(Write(eq1), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq2), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq3), run_time = 1)
		self.wait(1)
		self.play(Write(eq4), run_time = 1)
		self.wait(4)


	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()
