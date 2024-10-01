from manim import *



class ExtraVid8(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		eq1 = MathTex(r"x + y + z = 21", font_size = 54, color=BLACK).shift(UP * 1 + LEFT * 4)
		eq2 = MathTex(r"0.3x + 0.4y + 0.55z = 0.45 \cdot 21", font_size = 54,
			   color=BLACK).next_to(eq1, DOWN, buff=0.3).align_to(eq1, LEFT)
		eq3 = MathTex(r"3x + 4y + 7z = 111", font_size = 54, color=BLACK)\
			.next_to(eq2, DOWN, buff=0.3).align_to(eq2, LEFT)
		
		self.wait(1)
		self.play(Write(eq1), run_time=2)
		self.wait(4)
		self.play(Write(eq2), run_time=2)
		self.wait(4)
		self.play(Write(eq3), run_time=2)
		self.wait(4)

		eq4 = MathTex(r"x = 6", font_size = 54, color=BLACK).shift(UP * 1 + RIGHT * 4)
		eq5 = MathTex(r"y = 4", font_size = 54, color=BLACK).next_to(eq4, DOWN, buff=0.3)\
			.align_to(eq4, LEFT)
		eq6 = MathTex(r"z = 11", font_size = 54, color=BLACK).next_to(eq5, DOWN, buff=0.3)\
			.align_to(eq5, LEFT)

		group = VGroup(eq4, eq5, eq6)
		sur_box = SurroundingRectangle(group, buff=0.3)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=5)

		self.play(Write(eq4), run_time=0.5)
		self.play(Write(eq5), run_time=0.5)
		self.play(Write(eq6), run_time=0.5)
		self.play(Create(sur_box), run_time=1)
		self.wait(4)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
