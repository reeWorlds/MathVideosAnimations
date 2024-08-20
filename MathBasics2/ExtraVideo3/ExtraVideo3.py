from manim import *
import math


class ExtraVid3(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		eq1 = MathTex(r"\left\{\begin{array}{l}2x+5y=5\\x-2y=7\end{array}\right.", font_size = 48,
				color=BLACK).shift(2.8 * UP + 3.5 * LEFT)

		eq2 = MathTex(r"-2x+4y=14", font_size = 48, color=BLACK).next_to(eq1, DOWN, buff = 0.35)\
			.align_to(eq1, LEFT)
		eq2_extr = MathTex(r"\times 2", font_size = 48, color=BLACK).next_to(eq1, RIGHT, buff = 0.35)\
			.shift(DOWN*0.24)
		
		eq3 = MathTex(r"2x+5y-2x+4y=5-14", font_size = 48, color=BLACK).next_to(eq2, DOWN, buff = 0.3)\
			.align_to(eq2, LEFT)
		eq4 = MathTex(r"9y=-9", font_size = 48, color=BLACK).next_to(eq3, DOWN, buff = 0.15)\
			.align_to(eq3, LEFT)
		eq5 = MathTex(r"y=-1", font_size = 48, color=BLACK).next_to(eq4, DOWN, buff = 0.15)\
			.align_to(eq4, LEFT)

		eq6 = MathTex(r"2x+5\cdot(-1)=5", font_size = 48, color=BLACK).next_to(eq5, DOWN, buff = 0.3)\
			.align_to(eq5, LEFT)
		eq7 = MathTex(r"2x=10", font_size = 48, color=BLACK).next_to(eq6, DOWN, buff = 0.15)\
			.align_to(eq6, LEFT)
		eq8 = MathTex(r"x=5", font_size = 48, color=BLACK).next_to(eq7, DOWN, buff = 0.15)\
			.align_to(eq7, LEFT)

		eq9 = MathTex(r"\boxed{x=5, y=-1}", font_size = 48, color=BLACK).shift(1.5 * DOWN + 2.5 * RIGHT)

		self.wait(1)
		self.play(Write(eq1), run_time = 2)
		self.wait(3)
		self.play(Write(eq2), Write(eq2_extr), run_time = 1)
		self.wait(1)
		self.play(Write(eq3), run_time = 1)
		self.wait(1)
		self.play(Write(eq4), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq5), run_time = 1)
		self.wait(3)
		self.play(Write(eq6), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq7), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq8), run_time = 1)
		self.wait(1)
		self.play(Write(eq9), run_time = 1)
		self.wait(4)

	def showa2(self):
		eq1 = MathTex(r"\left\{\begin{array}{l}y+x=3\\x^2+4=8y\end{array}\right.", font_size = 48,
				color=BLACK).shift(2.7 * UP + 3.5 * LEFT)

		eq2 = MathTex(r"x=3-y", font_size = 48, color=BLACK).next_to(eq1, DOWN, buff = 0.25)\
			.align_to(eq1, LEFT)
		
		eq3 = MathTex(r"(3-y)^2+4=8y", font_size = 48, color=BLACK).next_to(eq2, DOWN, buff = 0.2)\
			.align_to(eq2, LEFT)
		eq4 = MathTex(r"9-6y+y^2+4=8y", font_size = 48, color=BLACK).next_to(eq3, DOWN, buff = 0.1)\
			.align_to(eq3, LEFT)
		eq5 = MathTex(r"y^2-14y+13=0", font_size = 48, color=BLACK).next_to(eq4, DOWN, buff = 0.1)\
			.align_to(eq4, LEFT)

		eq6_1 = MathTex(r"y_1=1", font_size = 48, color=BLACK).shift(1.1 * DOWN + 3 * LEFT)
		eq6_2 = MathTex(r"y_2=13", font_size = 48, color=BLACK).shift(1.1 * DOWN + 3 * RIGHT)

		eq7_1 = MathTex(r"1+x_1=3", font_size = 48, color=BLACK).next_to(eq6_1, DOWN, buff = 0.1)
		eq8_1 = MathTex(r"x_1=2", font_size = 48, color=BLACK).next_to(eq7_1, DOWN, buff = 0.1)
		eq9_1 = MathTex(r"\boxed{x_1=2, y_1=1}", font_size = 48, color=BLACK)\
			.next_to(eq8_1, DOWN, buff = 0.15)

		eq7_2 = MathTex(r"13+x_2=3", font_size = 48, color=BLACK).next_to(eq6_2, DOWN, buff = 0.1)
		eq8_2 = MathTex(r"x_2=-10", font_size = 48, color=BLACK).next_to(eq7_2, DOWN, buff = 0.1)
		eq9_2 = MathTex(r"\boxed{x_2=-10, y_2=13}", font_size = 48, color=BLACK)\
			.next_to(eq8_2, DOWN, buff = 0.15)
		
		self.wait(1)
		self.play(Write(eq1), run_time = 2)
		self.wait(3)
		self.play(Write(eq2), run_time = 1)
		self.wait(1)
		self.play(Write(eq3), run_time = 1)
		self.wait(1)
		self.play(Write(eq4), run_time = 1)
		self.wait(1)
		self.play(Write(eq5), run_time = 1)
		self.wait(3)
		self.play(Write(eq6_1), Write(eq6_2), run_time = 1)
		self.wait(1)
		self.play(Write(eq7_1), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq8_1), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq9_1), run_time = 1)
		self.wait(1)
		self.play(Write(eq7_2), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq8_2), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq9_2), run_time = 1)
		self.wait(4)

	def showa3(self):
		axes = Axes(x_range=[-2.5, 2.5], y_range=[-1.5, 1.5], x_length=8, y_length=4.8,
			  x_axis_config={"tip_width": 0.2, "tip_height": 0.2},
			  y_axis_config={"tip_width": 0.2, "tip_height": 0.2},
			  axis_config={"color": BLACK, "stroke_width": 4}).shift(2.5 * LEFT + 0.75 * DOWN)
		px1 = MathTex(r"1", font_size = 42, color=BLACK).next_to(axes.c2p(1, 0), UP, buff = 0.2)
		
		eq1 = MathTex(r"\left\{\begin{array}{l}y=cos(x)\\y^3=x^2\end{array}\right.", font_size = 48,
				color=BLACK).shift(2.7 * UP + 3.5 * LEFT)

		f1 = axes.plot(lambda x: math.cos(x), color=BLUE)
		f2_1 = axes.plot(lambda x: math.pow(abs(x), 2.0/3.0), color=GREEN, x_range=[-2.0, -1e-3])
		f2_2 = axes.plot(lambda x: math.pow(abs(x), 2.0/3.0), color=GREEN, x_range=[1e-3, 2.0])
		
		self.wait(1)
		self.play(Create(axes), Write(px1), run_time = 1)
		self.wait(1)
		self.play(Write(eq1), run_time = 2)
		self.wait(1)
		self.play(Write(f1), run_time = 1)
		self.wait(0.5)
		self.play(Write(f2_1), run_time = 0.5)
		self.play(Write(f2_2), run_time = 0.5)
		self.wait(1)

		d1 = Dot(axes.c2p(0.683, 0.775), color=BLACK, radius=0.06)
		d2 = Dot(axes.c2p(-0.683, 0.775), color=BLACK, radius=0.06)

		dly1 = DashedLine(axes.c2p(0.683, 0.775), axes.c2p(0, 0.775), color=BLACK)
		dly2 = DashedLine(axes.c2p(-0.683, 0.775), axes.c2p(0, 0.775), color=BLACK)

		dlx1 = DashedLine(axes.c2p(0.683, 0.775), axes.c2p(0.683, 0), color=BLACK)
		dlx2 = DashedLine(axes.c2p(-0.683, 0.775), axes.c2p(-0.683, 0), color=BLACK)
		dlx = VGroup(dlx1, dlx2)

		eq1 = MathTex(r"\boxed{x_1\approx0.7 \quad y_1\approx0.75}", font_size = 42, color=BLACK)\
			.shift(1 * UP + 4.0 * RIGHT)
		eq2 = MathTex(r"\boxed{x_2\approx-0.7 \quad y_2\approx0.75}", font_size = 42, color=BLACK)\
			.shift(4.0 * RIGHT)

		self.play(Create(d1), Create(d2), run_time = 1)
		self.wait(1)
		self.play(Create(dly1), Create(dly2), run_time = 1)
		self.wait(0.5)
		self.play(Create(dlx), run_time = 1)
		self.wait(1)
		self.play(Write(eq1), run_time = 1)
		self.play(Write(eq2), run_time = 1)
		self.wait(4)


	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()

