from manim import *


class ExtraVid2(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		line = NumberLine(x_range=[-1, 25, 1], length=12, include_numbers=True, include_tip=True,
					color=BLACK, tip_width=0.15, tip_height=0.25).shift(1.5 * DOWN + 0.5 * RIGHT)

		t0 = MathTex(r"0", color=BLACK, font_size = 42).next_to(line.n2p(0), DOWN)
		t1 = MathTex(r"1", color=BLACK, font_size = 42).next_to(line.n2p(1), DOWN)
		t10 = MathTex(r"10", color=BLACK, font_size = 42).next_to(line.n2p(10), DOWN)

		st_dot = Dot(line.n2p(0), color=BLACK, radius=0.08)
		st_img = ImageMobject("./ExtraVideo2/tank.png").scale(1.4).next_to(st_dot, UP, buff=0.1)\
			.align_to(st_dot, RIGHT)
		
		end_dot = Dot(line.n2p(10), color=BLACK, radius=0.08)
		end_img = ImageMobject("./ExtraVideo2/enemy.png").scale(0.6).next_to(end_dot, UP, buff=0.1)\
			.align_to(end_dot, RIGHT)


		self.wait(1)
		self.play(Create(line), run_time = 2)
		self.play(Write(t0), Write(t1), Write(t10), run_time = 1)
		self.wait(1)
		self.play(FadeIn(st_img), Create(st_dot), run_time = 1)
		self.wait(0.5)
		self.play(FadeIn(end_img), Create(end_dot), run_time = 1)
		self.wait(1)
		
		st_arr = Arrow(start=ORIGIN, end=1.0*RIGHT, color=BLACK, tip_length=0.15, buff=0)\
			.next_to(st_img, UP, buff=0.1)
		st_text = MathTex(r"2 \mathit{v}", color=BLACK, font_size = 42).next_to(st_arr, UP, buff=0.1)

		end_arr = Arrow(start=ORIGIN, end=0.5*RIGHT, color=BLACK, tip_length=0.15, buff=0)\
			.next_to(end_img, UP, buff=0.1)
		end_text = MathTex(r"\mathit{v}", color=BLACK, font_size = 42).next_to(end_arr, UP, buff=0.1)
		
		self.play(Create(st_arr), Write(st_text), run_time = 1)
		self.wait(0.5)
		self.play(Create(end_arr), Write(end_text), run_time = 1)
		self.wait(0.5)

		anim1 = Group(st_img, st_dot, st_arr, st_text).animate.shift(6 * RIGHT).set_rate_func(linear)
		anim2 = Group(end_img, end_dot, end_arr, end_text).animate.shift(3 * RIGHT).set_rate_func(linear)

		self.play(anim1, anim2, run_time = 6)
		self.wait(3)

	def showa2(self):
		b1_text = MathTex(r"b_1", font_size=56, color=BLACK).shift(3 * UP + 2 * LEFT)
		q_text = MathTex(r"q", font_size=56, color=BLACK).shift(3 * UP)

		eq1 = MathTex(r"b_{i+1} = b_i \cdot q", font_size=48, color=BLACK).shift(2 * UP + 3 * LEFT)
		sur_box1 = SurroundingRectangle(eq1, buff=0.15)
		sur_box1.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=3)

		eq2 = MathTex(r"b_2 = b_1 \cdot q", font_size=48, color=BLACK).next_to(eq1, DOWN, buff=0.45)\
			.align_to(eq1, LEFT)
		eq3 = MathTex(r"b_3 = b_2 \cdot q", font_size=48, color=BLACK).next_to(eq2, DOWN, buff=0.1)\
			.align_to(eq2, LEFT)
		eq4 = MathTex(r"b_7 = b_6 \cdot q", font_size=48, color=BLACK).next_to(eq3, DOWN, buff=0.1)\
			.align_to(eq3, LEFT)

		eq5 = MathTex(r"b_3 = b_1 \cdot q^2", font_size=48, color=BLACK).next_to(eq2, RIGHT, buff=2.0)
		eq6 = MathTex(r"b_4 = b_1 \cdot q^3", font_size=48, color=BLACK).next_to(eq3, RIGHT, buff=2.0)
		eq7 = MathTex(r"b_7 = b_1 \cdot q^6", font_size=48, color=BLACK).next_to(eq4, RIGHT, buff=2.0)

		eq8 = MathTex(r"b_k = b_1 \cdot q^{k-1}", font_size=48, color=BLACK).next_to(eq4, DOWN, buff=0.4)
		sur_box2 = SurroundingRectangle(eq8, buff=0.15)
		sur_box2.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=3)

		eq9 = MathTex(r"b_1 = 3 \quad q = 2", font_size=48, color=BLACK).next_to(eq8, DOWN, buff=0.5)
		eq10 = MathTex(r"b_1=3 \quad b_2=6 \quad b_3=12 \quad b_4=24 \quad b_5=48 \quad b_6=96",
				 font_size=48, color=BLACK).next_to(eq9, DOWN, buff=0.25).shift(3.5 * RIGHT)

		self.wait(1)
		self.play(Write(b1_text), run_time = 1)
		self.wait(1)
		self.play(Write(q_text), run_time = 1)
		self.wait(2)
		self.play(Write(eq1), run_time = 1)
		self.play(Create(sur_box1), run_time = 1)
		self.wait(1)
		self.play(Write(eq2), run_time = 1)
		self.wait(0.25)
		self.play(Write(eq3), run_time = 1)
		self.wait(0.25)
		self.play(Write(eq4), run_time = 1)
		self.wait(1)
		self.play(Write(eq5), run_time = 1)
		self.wait(0.25)
		self.play(Write(eq6), run_time = 1)
		self.wait(0.25)
		self.play(Write(eq7), run_time = 1)
		self.wait(1)
		self.play(Write(eq8), run_time = 1)
		self.play(Create(sur_box2), run_time = 1)
		self.wait(1)
		self.play(Write(eq9), run_time = 1)
		self.wait(1)
		self.play(Write(eq10), run_time = 2)
		self.wait(3)

	def showa3(self):
		eq1 = MathTex(r"S_n = b_1 + b_2 + b_3 + \cdots + b_n", font_size=48, color=BLACK)\
			.shift(3.2 * UP + 3 * LEFT)

		eq2 = MathTex(r"S_n = b_1 + b1 \cdot q + b1 \cdot q^2 + \cdots + b1 \cdot q^{n-1}",
			   font_size=48, color=BLACK).next_to(eq1, DOWN, buff=0.3).align_to(eq1, LEFT)
		eq3 = MathTex(r"S_n = b_1 \cdot (1 + q + q^2 + \cdots + q^{n-2} + q^{n-1})", font_size=48,
				color=BLACK).next_to(eq2, DOWN, buff=0.15).align_to(eq2, LEFT)

		eq4 = MathTex(r"x = 1 + q + q^2 + q^3 + \cdots + q^{n-2} + q^{n-1}", font_size=48, color=BLACK)\
			.next_to(eq3, DOWN, buff=0.2).align_to(eq3, LEFT)
		eq4_2 = MathTex(r"= b_1 \cdot x", font_size=48, color=BLACK).next_to(eq3, RIGHT, buff=0.2)

		eq5 = MathTex(r"x \cdot (q - 1) = \quad\quad\quad q + q^2 + \cdots + q^{n-1} + q^n", font_size=48,
				color=BLACK).next_to(eq4, DOWN, buff=0.2).align_to(eq4, LEFT)
		eq6 = MathTex(r"-1 - q - q^2 - \cdots - q^{n-1}", font_size=48, color=BLACK)\
			.next_to(eq5, DOWN, buff=0.1).align_to(eq5, LEFT).shift(3.05 * RIGHT)

		self.wait(1)
		self.play(Write(eq1), run_time = 1)
		self.wait(1)
		self.play(Write(eq2), run_time = 1)
		self.wait(1)
		self.play(Write(eq3), run_time = 1)
		self.wait(2)
		self.play(Write(eq4), Write(eq4_2), run_time = 1)
		self.wait(2)
		self.play(Write(eq5), run_time = 1)
		self.play(Write(eq6), run_time = 1)
		self.wait(2)
		
		eq7 = MathTex(r"x \cdot (q - 1) = q^n - 1", font_size=48, color=BLACK)\
			.next_to(eq6, DOWN, buff=0.2).align_to(eq5, LEFT)

		eq8 = MathTex(r"x = \frac{q^n - 1}{q - 1}", font_size=48, color=BLACK)\
			.next_to(eq7, DOWN, buff=0.3).align_to(eq7, LEFT)
		
		self.play(Write(eq7), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq8), run_time = 1)
		self.wait(1)
		self.play(FadeOut(eq5), FadeOut(eq6), FadeOut(eq7), run_time = 0.5)
		self.play(eq8.animate.shift(2.0 * UP), run_time = 1)
		self.wait(1)

		eq9 = MathTex(r"S_n = b_1 \frac{q^n-1}{q-1}", font_size=48, color=BLACK)\
			.next_to(eq8, DOWN, buff=0.5).align_to(eq8, LEFT)
		sur_box = SurroundingRectangle(eq9, buff=0.15)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		self.play(Write(eq9), run_time = 1)
		self.play(Create(sur_box), run_time = 1)
		self.wait(4)

	def showa4(self):
		eq1 = MathTex(r"S_n = b_1 + b_1 \cdot q + b_1 \cdot q^2 + b_1 \cdot q^3 + \cdots", font_size=48,
				color=BLACK).shift(2.75 * UP + 1 * LEFT)
		eq2 = MathTex(r"|x| < 1", font_size=48, color=BLACK).next_to(eq1, DOWN, buff=0.1)\
			.align_to(eq1, LEFT)

		eq3 = MathTex(r"S_n = b_1 \frac{q^n-1}{q-1} = \frac{b_1 \cdot q^n}{q-1} + \frac{-b_1}{q-1}",
				font_size=48, color=BLACK).next_to(eq2, DOWN, buff=0.4).align_to(eq2, LEFT)
		eq4 = MathTex(r"n \to \infty", font_size=48, color=BLACK).next_to(eq3, DOWN, buff=0.15)\
			.align_to(eq3, LEFT)
		
		eq5 = MathTex(r"S = \frac{-b_1}{q-1}", font_size=48, color=BLACK).next_to(eq4, DOWN, buff=0.4)\
			.align_to(eq4, LEFT)
		
		eq6 = MathTex(r"S = \frac{b_1}{1-q}", font_size=48, color=BLACK).next_to(eq5, DOWN, buff=0.3)\
			.align_to(eq5, LEFT)
		sur_box = SurroundingRectangle(eq6, buff=0.15)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		self.wait(1)
		self.play(Write(eq1), run_time = 1)
		self.wait(1)
		self.play(Write(eq2), run_time = 1)
		self.wait(2)
		self.play(Write(eq3), run_time = 1)
		self.wait(1)
		self.play(Write(eq4), run_time = 1)
		self.wait(3)
		self.play(Write(eq5), run_time = 1)
		self.wait(0.5)
		self.play(Write(eq6), run_time = 1)
		self.play(Create(sur_box), run_time = 1)
		self.wait(4)

	def showa5(self):
		line = NumberLine(x_range=[-1, 25, 1], length=12, include_numbers=True, include_tip=True,
					color=BLACK, tip_width=0.15, tip_height=0.25).shift(1.5 * DOWN + 0.5 * RIGHT)

		t0 = MathTex(r"0", color=BLACK, font_size = 42).next_to(line.n2p(0), DOWN)
		t1 = MathTex(r"1", color=BLACK, font_size = 42).next_to(line.n2p(1), DOWN)
		t10 = MathTex(r"10", color=BLACK, font_size = 42).next_to(line.n2p(10), DOWN)

		st_dot = Dot(line.n2p(0), color=BLACK, radius=0.08)
		st_img = ImageMobject("./ExtraVideo2/tank.png").scale(1.4).next_to(st_dot, UP, buff=0.1)\
			.align_to(st_dot, RIGHT)
		
		end_dot = Dot(line.n2p(10), color=BLACK, radius=0.08)
		end_img = ImageMobject("./ExtraVideo2/enemy.png").scale(0.6).next_to(end_dot, UP, buff=0.1)\
			.align_to(end_dot, RIGHT)

		st_arr = Arrow(start=ORIGIN, end=1.0*RIGHT, color=BLACK, tip_length=0.15, buff=0)\
			.next_to(st_img, UP, buff=0.1)
		st_text = MathTex(r"2 \mathit{v}", color=BLACK, font_size = 42).next_to(st_arr, UP, buff=0.1)

		end_arr = Arrow(start=ORIGIN, end=0.5*RIGHT, color=BLACK, tip_length=0.15, buff=0)\
			.next_to(end_img, UP, buff=0.1)
		end_text = MathTex(r"\mathit{v}", color=BLACK, font_size = 42).next_to(end_arr, UP, buff=0.1)

		g1 = Group(st_img, st_dot, st_arr, st_text)
		g2 = Group(end_img, end_dot, end_arr, end_text)

		self.wait(1)
		self.play(Create(line), run_time = 1)
		self.play(Write(t0), Write(t1), Write(t10), run_time = 0.5)
		self.play(FadeIn(st_img), Create(st_dot), run_time = 0.5)
		self.play(FadeIn(end_img), Create(end_dot), run_time = 1)
		self.wait(0.5)
		self.play(Create(st_arr), Write(st_text), run_time = 1)
		self.play(Create(end_arr), Write(end_text), run_time = 1)
		self.wait(2)

		sd = 0.75 * DOWN

		mv1 = line.n2p(10) - line.n2p(0)
		t15 = MathTex(r"15", color=BLACK, font_size = 42).next_to(line.n2p(15), DOWN)
		
		dist10 = DoubleArrow(start=line.n2p(0) + sd, end=line.n2p(10) + sd, color=BLACK, buff=0,
					   tip_length=0.2)
		dist10_text = MathTex(r"10", color=BLACK, font_size = 36).next_to(dist10, DOWN, buff=0.1)

		self.play(g1.animate.shift(mv1), g2.animate.shift(0.5 * mv1), Create(dist10),
			Write(dist10_text), Write(t15), run_time = 2)
		self.wait(2)

		mv2 = line.n2p(15) - line.n2p(10)

		t17_5 = MathTex(r"17.5", color=BLACK, font_size = 42).next_to(line.n2p(17.5), DOWN)
		dist5 = DoubleArrow(start=line.n2p(10) + sd, end=line.n2p(15) + sd, color=BLACK, buff=0,
					  tip_length=0.2)
		dist5_text = MathTex(r"5", color=BLACK, font_size = 36).next_to(dist5, DOWN, buff=0.1)

		self.play(g1.animate.shift(mv2), g2.animate.shift(0.5 * mv2), Create(dist5),
			Write(dist5_text), Write(t17_5), run_time = 2)
		self.wait(2)

		mv3 = line.n2p(17.5) - line.n2p(15)

		dist2_5 = DoubleArrow(start=line.n2p(15) + sd, end=line.n2p(17.5) + sd, color=BLACK, buff=0,
						tip_length=0.2)
		dist2_5_text = MathTex(r"2.5", color=BLACK, font_size = 36).next_to(dist2_5, DOWN, buff=0.1)

		self.play(g1.animate.shift(mv3), g2.animate.shift(0.5 * mv3), Create(dist2_5),
			Write(dist2_5_text), run_time = 2)
		self.wait(1)

		mv4 = line.n2p(20) - line.n2p(17.5)

		dist_rest = DoubleArrow(start=line.n2p(17.5) + sd, end=line.n2p(20) + sd, color=BLACK, buff=0,
						  tip_length=0.2)
		dist_rest_text = MathTex(r"\cdots", color=BLACK, font_size = 42).next_to(dist_rest, DOWN, buff=0.1)

		self.play(g1.animate.shift(mv4), g2.animate.shift(0.5 * mv4), Create(dist_rest),
			Write(dist_rest_text), run_time = 1)
		self.wait(2)

		eq1 = MathTex(r"b_1 = 10 \quad b_2 = 5 \quad b_3 = 2.5 \quad b_4 = 1.25", color=BLACK,
				font_size = 42).shift(2 * UP + 2 * LEFT)
		eq2 = MathTex(r"q = 0.5", color=BLACK, font_size = 42).next_to(eq1, DOWN, buff=0.15)

		eq3 = MathTex(r"S = \frac{b_1}{1-q} = \frac{10}{1-0.5} = 20", color=BLACK, font_size = 42)\
			.next_to(eq2, DOWN, buff=0.4)

		self.play(Write(eq1), run_time = 1)
		self.play(Write(eq2), run_time = 1)
		self.wait(2)
		self.play(Write(eq3), run_time = 1)
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
