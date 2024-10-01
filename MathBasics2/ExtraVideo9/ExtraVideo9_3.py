
from manim import *


class ExtraVid9_3(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		number_line = NumberLine(x_range=[-4, 2, 1], length=8, include_numbers=True, include_tip=True,
						   color=BLACK)

		t0 = MathTex(r"0", color=BLACK, font_size = 48).next_to(number_line.n2p(0), DOWN)
		t1 = MathTex(r"1", color=BLACK, font_size = 48).next_to(number_line.n2p(1), DOWN)

		self.wait(1)
		self.play(Create(number_line), run_time = 2)
		self.play(Write(t0), Write(t1), run_time = 1)
		self.wait(3)

		d0 = Dot(number_line.n2p(0), color=BLACK, radius=0.08)
		tm2 = MathTex(r"-2", color=BLACK, font_size = 48).next_to(number_line.n2p(-2), DOWN)
		dm2 = Dot(number_line.n2p(-2), color=BLACK, radius=0.08)

		self.play(Create(d0), run_time = 1)
		self.wait(2)
		self.play(Write(tm2), Create(dm2), run_time = 1)
		self.wait(3)


		arc1 = CurvedArrow(number_line.n2p(-4) + 0.6*UP, number_line.n2p(-2), angle=-TAU/10,
					 color=BLACK, tip_length=0.01)
		arc1_text = MathTex(r"+", color=BLACK, font_size = 48).next_to(number_line.n2p(-3.25), UP)\
			.shift(0.1*DOWN)
		arc2 = CurvedArrow(number_line.n2p(-2), number_line.n2p(0), angle=-TAU/4, color=BLACK,
					 tip_length=0.01)
		arc2_text = MathTex(r"-", color=BLACK, font_size = 48).next_to(number_line.n2p(-1), UP)
		arc3 = CurvedArrow(number_line.n2p(0), number_line.n2p(2) + 0.6*UP, angle=-TAU/10,
					 color=BLACK,tip_length=0.01)
		arc3_text = MathTex(r"+", color=BLACK, font_size = 48).next_to(number_line.n2p(1.25), UP)\
			.shift(0.1*DOWN)

		self.play(Create(arc1), run_time = 1)
		self.play(Write(arc1_text), run_time = 1)
		self.wait(2)
		self.play(Create(arc2), run_time = 1)
		self.play(Write(arc2_text), run_time = 1)
		self.wait(2)
		self.play(Create(arc3), run_time = 1)
		self.play(Write(arc3_text), run_time = 1)
		self.wait(4)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
