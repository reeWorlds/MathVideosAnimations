from manim import *



class ExtraVid1(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		scene_rectangle = Rectangle(width=2.5, height=5, color=BLACK).to_edge(LEFT, buff=1.5)

		scene_text = Text("Scene", font_size=54, color=BLACK).move_to(scene_rectangle.get_center())
		scene_text.rotate(PI / 2)

		self.play(Create(scene_rectangle), run_time=2)
		self.wait(1)
		self.play(Write(scene_text), run_time=2)
		self.wait(3)

		num_rows = 18
		seats_in_first_row = 10
		seat_increment = 2

		for i in range(num_rows):
			num_seats = seats_in_first_row + i * seat_increment
			row = VGroup(*[Square(side_length=0.13, color=DARK_BLUE, stroke_width = 1.5) for _ in range(num_seats)])
			row.arrange(DOWN, buff=0.04 + 0.1 * (num_rows - 1 - i) / num_rows)
			row.next_to(scene_rectangle, RIGHT, buff=0.5)
			row.shift(1.5 * RIGHT * i * 0.15)
			self.play(Create(row), run_time = 0.4)

		self.wait(4)

	def showa2(self):
		nums = [4, 7, 10, 13, 16, 19, 22]

		seq = MathTex(" \\quad ".join([str(num) for num in nums]), font_size=84, color=BLACK)\
			.shift(UP * 2 + LEFT * 0.8)

		self.wait(1)
		self.play(Write(seq), run_time = 3)
		self.wait(2)

		t1_1 = MathTex("4 + 3 = 7", font_size=64, color=BLACK).shift(LEFT * 3.5 + UP * 0.8)
		t1_2 = MathTex("7 + 3 = 10", font_size=64, color=BLACK).next_to(t1_1, DOWN, buff=0.3)
		t1_3 = MathTex("10 + 3 = 13", font_size=64, color=BLACK).next_to(t1_2, DOWN, buff=0.3)
		t1_4 = MathTex("\dots", font_size=64, color=BLACK).next_to(t1_3, DOWN, buff=0.3)

		self.play(Write(t1_1), run_time = 1)
		self.wait(0.5)
		self.play(Write(t1_2), run_time = 1)
		self.wait(0.5)
		self.play(Write(t1_3), run_time = 1)
		self.wait(0.5)
		self.play(Write(t1_4), run_time = 1)
		self.wait(2)

		t2_1 = MathTex("a_1 = 4", font_size=64, color=BLACK).shift(RIGHT * 2.5 + UP * 0.8)
		t2_2 = MathTex("a_2 = 7", font_size=64, color=BLACK).next_to(t2_1, DOWN, buff=0.3)
		t2_3 = MathTex("a_3 = 10", font_size=64, color=BLACK).next_to(t2_2, DOWN, buff=0.3)
		t2_4 = MathTex("\dots", font_size=64, color=BLACK).next_to(t2_3, DOWN, buff=0.3)

		self.play(Write(t2_1), run_time = 1)
		self.wait(0.5)
		self.play(Write(t2_2), run_time = 1)
		self.wait(0.5)
		self.play(Write(t2_3), run_time = 1)
		self.wait(0.5)
		self.play(Write(t2_4), run_time = 1)
		self.wait(2)

		t3 = MathTex("d = 3", font_size=64, color=BLACK).shift(DOWN * 2 + LEFT * 0.5)

		self.play(Write(t3), run_time = 1)
		self.wait(4)

	def showa3(self):
		nums1 = [100, 98, 96, 94, 92, 90, 88]

		s1_a1 = MathTex("a_1 = 100", font_size=72, color=BLACK).shift(UP * 2.3 + 1.4 * LEFT)
		s1_d = MathTex("d = -2", font_size=72, color=BLACK).next_to(s1_a1, RIGHT, buff=0.9)
		seq1 = MathTex(" \\quad ".join([str(num) for num in nums1]), font_size=64, color=BLACK).shift(UP * 1.3)

		self.wait(1)
		self.play(Write(s1_a1), run_time = 1)
		self.play(Write(s1_d), run_time = 1)
		self.wait(1)
		self.play(Write(seq1), run_time = 2)
		self.wait(2)

		nums2 = [-7.3, -7.3, -7.3, -7.3, -7.3]

		s2_a1 = MathTex("a_1 = -7.3", font_size=72, color=BLACK).shift(DOWN * 0.5 + 1.45 * LEFT)
		s2_d = MathTex("d = 0", font_size=72, color=BLACK).next_to(s2_a1, RIGHT, buff=0.9)
		seq2 = MathTex(" \\quad ".join([str(num) for num in nums2]), font_size=64, color=BLACK).shift(DOWN * 1.5)

		self.play(Write(s2_a1), run_time = 1)
		self.play(Write(s2_d), run_time = 1)
		self.wait(1)
		self.play(Write(seq2), run_time = 2)
		self.wait(4)

	def showa4(self):
		t1 = MathTex("a_2 = a_1 + d", font_size=52, color=BLACK).shift(UP * 2.75 + 3.5 * LEFT)
		t2 = MathTex("a_3 = a_2 + d", font_size=52, color=BLACK).next_to(t1, DOWN, buff=0.1)
		t2_2 = MathTex("= a_1 + 2 \cdot d", font_size=52, color=BLACK).next_to(t2, RIGHT, buff=0.3)
		t3 = MathTex("a_4 = a_3 + d", font_size=52, color=BLACK).next_to(t2, DOWN, buff=0.1)
		t3_2 = MathTex("= a_1 + 3 \cdot d", font_size=52, color=BLACK).next_to(t3, RIGHT, buff=0.3)

		self.wait(1)
		self.play(Write(t1), run_time = 1)
		self.wait(1)
		self.play(Write(t2), run_time = 1)
		self.play(Write(t2_2), run_time = 1)
		self.wait(1)
		self.play(Write(t3), run_time = 1)
		self.play(Write(t3_2), run_time = 1)
		self.wait(1)

		t4 = MathTex("a_k = a_1 + (k - 1) \cdot d", font_size=52, color=BLACK).next_to(t3, DOWN, buff = 0.6)\
			.align_to(t3, LEFT)
		t4_sur_rec = SurroundingRectangle(t4, buff=0.1)
		t4_sur_rec.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=3)

		self.play(Write(t4), run_time = 1)
		self.play(Create(t4_sur_rec), run_time = 1)
		self.wait(1)
		
		t5 = MathTex("a_1 = a_2 - d", font_size=52, color=BLACK).next_to(t4, DOWN, buff = 0.6)\
			.align_to(t4, LEFT)
		t6 = MathTex("a_3 = a_8 - 5 \cdot d", font_size=52, color=BLACK).next_to(t5, DOWN, buff = 0.1)\
			.align_to(t5, LEFT)

		self.play(Write(t5), run_time = 1)
		self.wait(1)
		self.play(Write(t6), run_time = 1)
		self.wait(1)

		t7 = MathTex("a_k = a_p + (k - p) \cdot d", font_size=52, color=BLACK).next_to(t6, DOWN, buff = 0.6)\
			.align_to(t6, LEFT)
		t7_sur_rec = SurroundingRectangle(t7, buff=0.1)
		t7_sur_rec.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=3)

		self.play(Write(t7), run_time = 1)
		self.play(Create(t7_sur_rec), run_time = 1)
		self.wait(1)

		self.wait(4)

	def showa5(self):
		t1 = MathTex("4 \\quad 7 \\quad 10 \\quad 13 \\quad 16", font_size=72, color=BLACK)\
			.shift(UP * 2 + 2 * LEFT)
		t2 = MathTex("S_4 = 4 + 7 + 10 + 13 = 34", font_size=68, color=BLACK).next_to(t1, DOWN, buff=0.8)
		t3 = MathTex("S_{100} = ?", font_size=68, color=BLACK).next_to(t2, DOWN, buff=1).shift(LEFT * 1.8)
		t4 = MathTex("S_{1000} = ?", font_size=68, color=BLACK).next_to(t2, DOWN, buff=1).shift(RIGHT * 1.8)

		self.wait(1)
		self.play(Write(t1), run_time = 2)
		self.wait(2)
		self.play(Write(t2), run_time = 3)
		self.wait(2)
		self.play(Write(t3), run_time = 1)
		self.play(Write(t4), run_time = 1)
		self.wait(4)
		
	def showa6(self):
		t1 = MathTex(r"S_n = a_1 + a_2 + a_3 + \dots + a_n", font_size=64, color=BLACK)\
			.shift(UP * 3 + 1.75 * LEFT)
		t2 = MathTex(r"a_1 \quad \quad d", font_size=48, color=BLACK).next_to(t1, DOWN, buff=0.3)
		t3 = MathTex(r"S_n = a_1 + a_1 + d + a_1 + 2 \cdot d + \dots + a1 + (n - 1) \cdot d", font_size=48,\
			color=BLACK).next_to(t2, DOWN, buff=0.3).shift(RIGHT * 1)
		t4 = MathTex(r"S_n = n \cdot a_1 + d \cdot (1 + 2 + 3 + \dots + (n - 1))", font_size=48, color=BLACK)\
			.next_to(t3, DOWN, buff=0.2)

		self.wait(1)
		self.play(Write(t1), run_time = 2)
		self.wait(2)
		self.play(Write(t2), run_time = 2)
		self.wait(2)
		self.play(Write(t3), run_time = 2)
		self.wait(2)
		self.play(Write(t4), run_time = 2)
		self.wait(2)

		t5 = MathTex(r"1 + 2 + 3 + 4 + \dots + (n - 4) + (n - 3) + (n - 2) + (n - 1)", font_size=44,\
		   color=BLACK).next_to(t4, DOWN, buff=0.5).shift(LEFT * 0.4)
		t6 = MathTex(r"= n \cdot \tfrac{n - 1}{2}", font_size=44, color=BLACK).next_to(t5, RIGHT, buff=0.1)	

		self.play(Write(t5), run_time = 2)
		self.wait(2)
		self.play(Write(t6), run_time = 2)
		self.wait(2)

		t7 = MathTex(r"S_n = n \cdot a_1 + d \cdot n \cdot \tfrac{n - 1}{2}", font_size=48, color=BLACK)\
			.next_to(t5, DOWN, buff=0.5)
		t8 = MathTex(r"S_n = \frac{n \cdot (2 \cdot a_1 + (n - 1) \cdot d)}{2}", font_size=48, color=BLACK)\
			.next_to(t7, DOWN, buff=0.5).shift(LEFT * 2)
		t8_sur_box = SurroundingRectangle(t8, buff=0.1)
		t8_sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=3)
		t9 = MathTex(r"S_n = \frac{n \cdot (a_1 + a_n)}{2}", font_size=48, color=BLACK)\
			.next_to(t7, DOWN, buff=0.5).shift(RIGHT * 4.5)
		t9_sur_box = SurroundingRectangle(t9, buff=0.1)
		t9_sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=3)

		self.play(Write(t7), run_time = 2)
		self.wait(2)
		self.play(Write(t8), run_time = 2)
		self.play(Create(t8_sur_box), run_time = 1)
		self.wait(2)
		self.play(Write(t9), run_time = 2)
		self.play(Create(t9_sur_box), run_time = 2)
		self.wait(5)

	def showa7(self):
		scene_rectangle = Rectangle(width=2, height=4.5, color=BLACK).to_edge(LEFT, buff=0.5)

		scene_text = Text("Scene", font_size=54, color=BLACK).move_to(scene_rectangle.get_center())
		scene_text.rotate(PI / 2)

		self.play(Create(scene_rectangle), Write(scene_text), run_time=1)
		self.wait(1)

		num_rows = 18
		seats_in_first_row = 10
		seat_increment = 2

		for i in range(num_rows):
			num_seats = seats_in_first_row + i * seat_increment
			row = VGroup(*[Square(side_length=0.13, color=DARK_BLUE, stroke_width = 1.5) for _ in range(num_seats)])
			row.arrange(DOWN, buff=0.04 + 0.1 * (num_rows - 1 - i) / num_rows)
			row.next_to(scene_rectangle, RIGHT, buff=0.25)
			row.shift(1.5 * RIGHT * i * 0.13)
			self.play(Create(row), run_time = 0.1)

		self.wait(5)

		t1 = MathTex(r"S_n = \frac{n \cdot (2 \cdot a_1 + (n - 1) \cdot d)}{2}", font_size=40, color=BLACK)\
			.shift(RIGHT * 2.2 + UP * 1.5)

		t2 = MathTex(r"a_1 = 10", font_size=40, color=BLACK).next_to(t1, DOWN, buff=0.5).shift(LEFT * 1.5)
		t3 = MathTex(r"d = 2", font_size=40, color=BLACK).next_to(t1, DOWN, buff=0.5).shift(RIGHT * 0.4)
		t4 = MathTex(r"n = 18", font_size=40, color=BLACK).next_to(t1, DOWN, buff=0.5).shift(RIGHT * 2.3)

		t5 = MathTex(r"S_{18} = \frac{18 \cdot (2 \cdot 10 + (18 - 1) \cdot 2)}{2}", font_size=40, color=BLACK)\
			.next_to(t3, DOWN, buff=0.5).shift(LEFT * 0.4)
		t6 = MathTex(r"= 486", font_size=40, color=BLACK).next_to(t5, RIGHT, buff=0.1)

		self.play(Write(t1), run_time = 2)
		self.wait(2)
		self.play(Write(t2), run_time = 2)
		self.wait(2)
		self.play(Write(t3), run_time = 2)
		self.wait(2)
		self.play(Write(t4), run_time = 2)
		self.wait(2)
		self.play(Write(t5), run_time = 2)
		self.wait(2)
		self.play(Write(t6), run_time = 2)
		self.wait(5)

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
