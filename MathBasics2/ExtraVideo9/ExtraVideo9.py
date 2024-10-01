from manim import *



class ExtraVid9(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		eq1 = MathTex(r"\frac{3x+6}{x} \leq 0", font_size=48, color=BLACK).shift(UP * 1)
		eq2 = MathTex(r"\log_{\frac{a}{2}}{\left( (x-a+2)^2 \right)} \geq 2\log_{\frac{a}{2}}{(a-1)}",
			   font_size=48, color=BLACK).next_to(eq1, DOWN, buff=0.2)
		
		self.wait(1)
		self.play(Write(eq1), run_time=1)
		self.play(Write(eq2), run_time=2)
		self.wait(4)

	def showa2(self):
		eq1 = MathTex(r"x \neq 0", font_size=48, color=BLACK).shift(UP * 3 + 3 * LEFT)
		
		eq2 = MathTex(r"\frac{a}{2} > 0", font_size=48, color=BLACK).next_to(eq1, DOWN, buff=0.2)\
			.align_to(eq1, LEFT)
		eq2_2 = MathTex(r"\Rightarrow a > 0", font_size=48, color=BLACK).next_to(eq2, RIGHT, buff=0.3)\
			.shift(UP * 0.08)

		eq3 = MathTex(r"\frac{a}{2} \neq 1", font_size=48, color=BLACK).next_to(eq2, DOWN, buff=0.2)\
			.align_to(eq2, LEFT)
		e3_2 = MathTex(r"\Rightarrow a \neq 2", font_size=48, color=BLACK).next_to(eq3, RIGHT, buff=0.3)\
			.shift(UP * 0.05)

		self.wait(1)
		self.play(Write(eq1), run_time=1)
		self.wait(2)
		self.play(Write(eq2), run_time=1)
		self.play(Write(eq2_2), run_time=1)
		self.wait(2)
		self.play(Write(eq3), run_time=1)
		self.play(Write(e3_2), run_time=1)
		self.wait(4)

		req1 = MathTex(r"x = 0", font_size=48, color=RED).next_to(eq3, DOWN, buff=0.6).align_to(eq1, LEFT)
		req2 = MathTex(r"a \leq 0", font_size=48, color=RED).next_to(req1, DOWN, buff=0.2)\
			.align_to(req1, LEFT)
		req3 = MathTex(r"a = 2", font_size=48, color=RED).next_to(req2, DOWN, buff=0.2)\
			.align_to(req2, LEFT)

		self.play(Write(req1), run_time=1)
		self.wait(2)
		self.play(Write(req2), run_time=1)
		self.wait(2)
		self.play(Write(req3), run_time=1)
		self.wait(4)

	def showa3(self):
		eq1 = MathTex(r"(x-a+2)^2 \geq 0", font_size=48, color=BLACK).shift(UP * 3 + 3 * LEFT)
		eq2 = MathTex(r"(x-a+2)^2 \neq 0", font_size=48, color=BLACK).next_to(eq1, DOWN, buff=0.1)\
			.align_to(eq1, LEFT)
		eq3 = MathTex(r"x-a+2 \neq 0", font_size=48, color=BLACK).next_to(eq2, DOWN, buff=0.1)\
			.align_to(eq2, LEFT)
		eq4 = MathTex(r"a \neq x+2", font_size=48, color=BLACK).next_to(eq3, DOWN, buff=0.1)\
			.align_to(eq3, LEFT)

		eq5 = MathTex(r"a-1 > 0", font_size=48, color=BLACK).next_to(eq4, DOWN, buff=0.3)\
			.align_to(eq4, LEFT)
		eq6 = MathTex(r"a > 1", font_size=48, color=BLACK).next_to(eq5, DOWN, buff=0.1)\
			.align_to(eq5, LEFT)

		self.wait(1)
		self.play(Write(eq1), run_time=1)
		self.wait(1)
		self.play(Write(eq2), run_time=1)
		self.wait(1)
		self.play(Write(eq3), run_time=1)
		self.wait(1)
		self.play(Write(eq4), run_time=1)
		self.wait(2)
		self.play(Write(eq5), run_time=1)
		self.wait(1)
		self.play(Write(eq6), run_time=1)
		self.wait(4)

		req1 = MathTex(r"a = x+2", font_size=48, color=RED).next_to(eq6, DOWN, buff=0.6).align_to(eq6, LEFT)
		req2 = MathTex(r"a \leq 1", font_size=48, color=RED).next_to(req1, DOWN, buff=0.2)\
			.align_to(req1, LEFT)

		self.play(Write(req1), run_time=1)
		self.wait(2)
		self.play(Write(req2), run_time=1)
		self.wait(4)

	def showa4(self):
		eq1 = MathTex(r"x = 0", font_size=48, color=BLACK).shift(UP * 3 + 3 * LEFT)
		
		eq2 = MathTex(r"3x + 6 = 0", font_size=48, color=BLACK).next_to(eq1, DOWN, buff=0.3)\
			.align_to(eq1, LEFT)
		eq3 = MathTex(r"x = -2", font_size=48, color=BLACK).next_to(eq2, DOWN, buff=0.1)\
			.align_to(eq2, LEFT)
		
		eq4 = MathTex(r"x \in [-2;0)", font_size=48, color=BLACK).next_to(eq3, DOWN, buff=0.3)\
			.align_to(eq3, LEFT)

		self.wait(1)
		self.play(Write(eq1), run_time=1)
		self.wait(1)
		self.play(Write(eq2), run_time=1)
		self.wait(1)
		self.play(Write(eq3), run_time=1)
		self.wait(1)
		self.play(Write(eq4), run_time=1)
		self.wait(4)

		req1 = MathTex(r"x < 2", font_size=48, color=RED).next_to(eq4, DOWN, buff=0.5).align_to(eq4, LEFT)
		req2 = MathTex(r"x \geq 0", font_size=48, color=RED).next_to(req1, DOWN, buff=0.15)\
			.align_to(req1, LEFT)

		self.play(Write(req1), run_time=1)
		self.wait(1)
		self.play(Write(req2), run_time=1)
		self.wait(4)

	def showa5(self):
		eq1 = MathTex(r"\log_{\frac{a}{2}}{\left( (x-a+2)^2 \right)} \geq 2\log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).shift(UP * 3 + 2 * LEFT)
		eq2 = MathTex(r"2\log_{\frac{a}{2}}{(x-a+2)} \geq 2\log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).next_to(eq1, DOWN, buff=0.2).align_to(eq1, LEFT)
		eq3 = MathTex(r"\log_{\frac{a}{2}}{(x-a+2)} \geq \log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).next_to(eq2, DOWN, buff=0.2).align_to(eq2, LEFT)
		eq4 = MathTex(r"x-a+2 \leq a-1", font_size=42, color=BLACK).next_to(eq3, DOWN, buff=0.2)\
			.align_to(eq3, LEFT)
		eq5 = MathTex(r"a \geq \tfrac{1}{2}x+1.5", font_size=42, color=BLACK).next_to(eq4, DOWN, buff=0.2)\
			.align_to(eq4, LEFT)
		eq6 = MathTex(r"x \leq 2a-3", font_size=42, color=BLACK).next_to(eq5, DOWN, buff=0.2)\
			.align_to(eq5, LEFT)

		self.wait(1)
		self.play(Write(eq1), run_time=1.5)
		self.wait(2)
		self.play(Write(eq2), run_time=1.5)
		self.wait(1)
		self.play(Write(eq3), run_time=1)
		self.wait(3)
		self.play(Write(eq4), run_time=1)
		self.wait(1)
		self.play(Write(eq5), run_time=1)
		self.play(Write(eq6), run_time=1)
		self.wait(4)

		req1 = MathTex(r"a < \tfrac{1}{2}x+1.5", font_size=48, color=RED).next_to(eq6, DOWN, buff=0.5)\
			.align_to(eq6, LEFT)

		self.play(Write(req1), run_time=1)
		self.wait(4)

	def showa6(self):
		eq1 = MathTex(r"\log_{\frac{a}{2}}{\left( (x-a+2)^2 \right)} \geq 2\log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).shift(UP * 3 + 2 * LEFT)
		eq2 = MathTex(r"2\log_{\frac{a}{2}}{(a-x-2)} \geq 2\log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).next_to(eq1, DOWN, buff=0.2).align_to(eq1, LEFT)
		eq3 = MathTex(r"\log_{\frac{a}{2}}{(a-x-2)} \geq \log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).next_to(eq2, DOWN, buff=0.2).align_to(eq2, LEFT)
		eq4 = MathTex(r"a-x-2 \leq a-1", font_size=42, color=BLACK).next_to(eq3, DOWN, buff=0.2)\
			.align_to(eq3, LEFT)
		eq5 = MathTex(r"-x-2 \leq -1", font_size=42, color=BLACK).next_to(eq4, DOWN, buff=0.2)\
			.align_to(eq4, LEFT)
		eq6 = MathTex(r"-x \leq 1", font_size=42, color=BLACK).next_to(eq5, DOWN, buff=0.2)\
			.align_to(eq5, LEFT)
		eq7 = MathTex(r"x \geq -1", font_size=42, color=BLACK).next_to(eq6, DOWN, buff=0.2)\
			.align_to(eq6, LEFT)

		self.wait(1)
		self.play(Write(eq1), run_time=1.5)
		self.wait(2)
		self.play(Write(eq2), run_time=1.5)
		self.wait(3)
		self.play(Write(eq3), run_time=1)
		self.wait(1)
		self.play(Write(eq4), run_time=1)
		self.wait(2)
		self.play(Write(eq5), run_time=1)
		self.play(Write(eq6), run_time=1)
		self.play(Write(eq7), run_time=1)
		self.wait(4)

		req1 = MathTex(r"x < -1", font_size=48, color=RED).next_to(eq7, DOWN, buff=0.5)\
			.align_to(eq7, LEFT)

		self.play(Write(req1), run_time=1)
		self.wait(4)

	def showa7(self):
		eq1 = MathTex(r"\log_{\frac{a}{2}}{\left( (x-a+2)^2 \right)} \geq 2\log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).shift(UP * 3 + 2 * LEFT)
		eq2 = MathTex(r"\log_{\frac{a}{2}}{(a-x-2)} \geq \log_{\frac{a}{2}}{(a-1)}",
				font_size=42, color=BLACK).next_to(eq1, DOWN, buff=0.2).align_to(eq1, LEFT)
		eq3 = MathTex(r"a-x-2 \geq a-1", font_size=42, color=BLACK).next_to(eq2, DOWN, buff=0.2)\
			.align_to(eq2, LEFT)
		eq4 = MathTex(r"-x-2 \geq -1", font_size=42, color=BLACK).next_to(eq3, DOWN, buff=0.2)\
			.align_to(eq3, LEFT)
		eq5 = MathTex(r"x \leq -1", font_size=42, color=BLACK).next_to(eq4, DOWN, buff=0.2)\
			.align_to(eq4, LEFT)

		self.wait(1)
		self.play(Write(eq1), run_time=1)
		self.wait(1)
		self.play(Write(eq2), run_time=1.5)
		self.wait(3)
		self.play(Write(eq3), run_time=1)
		self.wait(1)
		self.play(Write(eq4), run_time=1)
		self.play(Write(eq5), run_time=1)
		self.wait(4)

		req1 = MathTex(r"x > -1", font_size=48, color=RED).next_to(eq5, DOWN, buff=0.5)\
			.align_to(eq5, LEFT)

		self.play(Write(req1), run_time=1)
		self.wait(4)

	def showa8(self):
		eq1 = MathTex(r"a \in (1;1.5) \Rightarrow x \in [-1;a-2) \cup (a-2;2a-3)", font_size=42,
				color=BLACK).shift(UP * 2 + 2 * LEFT)
		eq2 = MathTex(r"a \in [1.5;2) \Rightarrow x \in [-1;a-2) \cup (a-2;0)", font_size=42,
				color=BLACK).next_to(eq1, DOWN, buff=0.2).align_to(eq1, LEFT)
		eq3 = MathTex(r"a \in (2;+\infty) \Rightarrow x \in [-2;-1]", font_size=42,
				color=BLACK).next_to(eq2, DOWN, buff=0.2).align_to(eq2, LEFT)
		eq4 = MathTex(r"a \in (-\infty;1] \cup \{2\} \Rightarrow x \in \emptyset", font_size=42,
				color=BLACK).next_to(eq3, DOWN, buff=0.2).align_to(eq3, LEFT)

		self.wait(1)
		self.play(Write(eq1), run_time=2)
		self.wait(3)
		self.play(Write(eq2), run_time=2)
		self.wait(3)
		self.play(Write(eq3), run_time=2)
		self.wait(3)
		self.play(Write(eq4), run_time=2)
		self.wait(4)


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
		self.showa8()
		self.clearEverything()
