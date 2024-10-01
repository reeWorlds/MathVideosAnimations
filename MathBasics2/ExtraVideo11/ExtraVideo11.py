from manim import *
import numpy as np


def get_spec_object(radius, n):
	n2 = n // 2
	theta = 2 * PI / n

	line_len = radius * np.sin(theta) / np.sin((PI - theta) / 2.0)

	init_point1 = 2.9 * DOWN + 1.8 * LEFT
	init_point2 = init_point1 + (line_len / 2) * RIGHT + np.sqrt(radius**2 - (line_len / 2)**2) * UP

	g1 = [VGroup(
		Line(init_point1 + (i * line_len) * RIGHT, init_point2 + (i * line_len) * RIGHT, color=BLUE),
		Line(init_point1 + ((i + 1) * line_len) * RIGHT, init_point2 + (i * line_len) * RIGHT, color=BLUE),
		ArcBetweenPoints(init_point1 + (i * line_len) * RIGHT, init_point1 + ((i + 1) * line_len) * RIGHT,
				   angle=theta, color=GREEN)
		)
	   for i in range(n2)]
	g2 = [VGroup(
		Line(init_point2 + (i * line_len) * RIGHT, init_point1 + ((i + 1) * line_len) * RIGHT, color=BLUE),
		Line(init_point2 + ((i + 1) * line_len) * RIGHT, init_point1 + ((i + 1) * line_len) * RIGHT, color=BLUE),
		ArcBetweenPoints(init_point2 + (i * line_len) * RIGHT, init_point2 + ((i + 1) * line_len) * RIGHT,
				   angle=-theta, color=GREEN)
		)
	   for i in range(n2)]

	g_all = []
	for i in range(n2):
		g_all.append(g1[i])
		g_all.append(g2[i])

	return g_all


class ExtraVid11(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		radius = 2.4

		circle = Circle(radius=radius, color=GREEN).shift(LEFT * 4.2 + UP * 1.2)

		l_radius = Line(start=circle.get_center(), end=circle.point_at_angle(PI/6), color=BLUE)
		t_radius = MathTex(r"r", font_size=72, color=BLACK).next_to(l_radius, UP, buff=-0.4)

		t_len = MathTex(r"L = 2 \cdot \pi \cdot r", font_size=48, color=BLACK).shift(UP * 3.2)


		self.wait(1)
		self.play(Create(circle), run_time=1)
		self.wait(1)
		self.play(Create(l_radius), Write(t_radius), run_time=1)
		self.wait(1)
		self.play(Write(t_len), run_time=1)
		self.wait(2)

		animations4 = []
		g4 = get_spec_object(radius, 4)
		for g in g4:
			animations4.append(AnimationGroup(*[Create(mobject) for mobject in g]))

		self.play(Succession(*animations4), run_time=3)
		self.wait(2)

		animations6 = []
		g6 = get_spec_object(radius, 6)
		for g in g6:
			animations6.append(AnimationGroup(*[Create(mobject) for mobject in g]))
		
		self.play(FadeOut(*g4), run_time=0.25)
		self.play(Succession(*animations6), run_time=1)
		self.wait(1)
		
		animations8 = []
		g8 = get_spec_object(radius, 8)
		for g in g8:
			animations8.append(AnimationGroup(*[Create(mobject) for mobject in g]))
		
		self.play(FadeOut(*g6), run_time=0.25)
		self.play(Succession(*animations8), run_time=1)
		self.wait(1)
		
		animations10 = []
		g10 = get_spec_object(radius, 10)
		for g in g10:
			animations10.append(AnimationGroup(*[Create(mobject) for mobject in g]))
		
		self.play(FadeOut(*g8), run_time=0.25)
		self.play(Succession(*animations10), run_time=1)
		self.wait(3)
		
		animations20 = []
		g20 = get_spec_object(radius, 20)
		for g in g20:
			animations20.append(AnimationGroup(*[Create(mobject) for mobject in g]))
		
		self.play(FadeOut(*g10), run_time=0.25)
		self.play(Succession(*animations20), run_time=1)
		self.wait(1)
		
		animations50 = []
		g50 = get_spec_object(radius, 50)
		for g in g50:
			animations50.append(AnimationGroup(*[Create(mobject) for mobject in g]))
		
		self.play(FadeOut(*g20), run_time=0.25)
		self.play(Succession(*animations50), run_time=1)
		self.wait(1)

		animations200 = []
		g200 = get_spec_object(radius, 200)
		for g in g200:
			animations200.append(AnimationGroup(*[Create(mobject) for mobject in g]))

		self.play(FadeOut(*g50), run_time=0.25)
		self.play(Succession(*animations200), run_time=1)
		self.wait(4)

		g_r_text = MathTex(r"r", font_size=54, color=BLACK).shift(DOWN * 1.7 + LEFT * 2.05)
		g_l2_text = MathTex(r"\pi \cdot r", font_size=54, color=BLACK).shift(DOWN * 0.25 + RIGHT * 2)

		s_sq_t = MathTex(r"S_{\square} = r \cdot \pi \cdot r = \pi \cdot r^2", font_size=48, color=BLACK)\
			.next_to(t_len, DOWN, buff=0.2).align_to(t_len, LEFT)

		self.play(Write(g_r_text), run_time=1)
		self.wait(1)
		self.play(Write(g_l2_text), run_time=1)
		self.wait(1)
		self.play(Write(s_sq_t), run_time=1)
		self.wait(2)

		s_circ_t = MathTex(r"S_{\circ} = S_{\square} = \pi \cdot r^2", font_size=48, color=BLACK)\
			.next_to(s_sq_t, DOWN, buff=0.2).align_to(s_sq_t, LEFT)
		sur_box = SurroundingRectangle(s_circ_t, buff=0.1)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=2)

		self.play(Write(s_circ_t), run_time=1)
		self.play(Create(sur_box), run_time=1)
		self.wait(2)

		r10_t = MathTex(r"r = 30", font_size=48, color=BLACK).next_to(s_circ_t, DOWN, buff=0.25)\
			.align_to(s_circ_t, LEFT)
		s_circ_10 = MathTex(r"S_{\circ} = \pi \cdot 30^2 = 900 \cdot \pi \approx 2800", font_size=48,
					  color=BLACK).next_to(r10_t, DOWN, buff=0.1).align_to(r10_t, LEFT)

		self.play(Write(r10_t), run_time=1)
		self.wait(1)
		self.play(Write(s_circ_10), run_time=1)
		self.wait(4)


	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
