from re import T
from webbrowser import get
from manim import *
import math

def get_vgroup_bounding_box(vgroup):
	min_point = np.array([np.inf, np.inf, np.inf])
	max_point = np.array([-np.inf, -np.inf, -np.inf])

	for submob in vgroup.submobjects:
		min_point = np.minimum(min_point, submob.get_corner(DL))
		max_point = np.maximum(max_point, submob.get_corner(UR))

	lower_left = min_point
	upper_left = np.array([min_point[0], max_point[1], 0])
	upper_right = max_point
	lower_right = np.array([max_point[0], min_point[1], 0])

	return [lower_left, upper_left, upper_right, lower_right]

def get_vgroup_angles(p_main, p1, p2, radius, num_marks):
	angs = VGroup()
	for i in range(num_marks):
		delta = 0.05 * i
		ang = Angle(Line(p_main, p1), Line(p_main, p2), radius=radius - delta, color = BLACK, stroke_width=2)
		angs.add(ang)
	return angs

class ExtraVid5(ThreeDScene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		pa = 2.5 * LEFT + 2.5 * DOWN
		pb = 4.5 * LEFT + 2.5 * UP
		pc = 6.0 * LEFT + 1.5 * DOWN

		da = Dot(pa, color = BLACK, radius=0.05)
		db = Dot(pb, color = BLACK, radius=0.05)
		dc = Dot(pc, color = BLACK, radius=0.05)

		la = Line(pc, pb, color = BLACK, stroke_width=3)
		lb = Line(pa, pc, color = BLACK, stroke_width=3)
		lc = Line(pa, pb, color = BLACK, stroke_width=3)

		tla = MathTex(r"a", color = BLACK).next_to(la, LEFT).shift(0.8 * RIGHT)
		tlb = MathTex(r"b", color = BLACK).next_to(lb, DOWN).shift(0.6 * UP)
		tlc = MathTex(r"c", color = BLACK).next_to(lc, RIGHT).shift(1.1 * LEFT)

		#ang_alpha = Angle(Line(pa, pb), Line(pa, pc), radius=0.35, color=BLACK)
		ang_alpha = get_vgroup_angles(pa, pb, pc, 0.35, 1)
		#ang_beta = Angle(Line(pb, pc), Line(pb, pa), radius=0.35, color=BLACK)
		ang_beta = get_vgroup_angles(pb, pc, pa, 0.365, 2)
		#ang_gamma = Angle(Line(pc, pa), Line(pc, pb), radius=0.35, color=BLACK)
		ang_gamma = get_vgroup_angles(pc, pa, pb, 0.38, 3)

		ta_alpha = MathTex(r"\alpha", color = BLACK, font_size = 38).next_to(ang_alpha, LEFT)\
			.shift(0.3 * RIGHT + 0.2 * UP)
		ta_beta = MathTex(r"\beta", color = BLACK, font_size = 38).next_to(ang_beta, DOWN)\
			.shift(0.2 * UP)
		ta_gamma = MathTex(r"\gamma", color = BLACK, font_size = 38).next_to(ang_gamma, RIGHT)\
			.shift(0.25 * LEFT + 0.05 * UP)

		self.wait(1)
		self.play(Create(da), Create(db), Create(dc), run_time = 1)
		self.wait(0.5)
		self.play(Create(la), Create(lb), Create(lc), run_time = 1)
		self.play(Write(tla), Write(tlb), Write(tlc), run_time = 1)
		self.wait(0.5)
		self.play(Create(ang_alpha), Create(ang_beta), Create(ang_gamma), run_time = 1)
		self.play(Write(ta_alpha), Write(ta_beta), Write(ta_gamma), run_time = 1)
		self.wait(2)

		t_cos1 = MathTex(r"a^2 = b^2 + c^2 - 2 \cdot b \cdot c \cdot \cos(\alpha)", color = BLACK,
				   font_size = 48).shift(2 * RIGHT + 1.5 * UP)
		t_cos2 = MathTex(r"b^2 = c^2 + a^2 - 2 \cdot a \cdot c \cdot \cos(\beta)", color = BLACK,
				   font_size = 48).next_to(t_cos1, DOWN)
		t_cos3 = MathTex(r"c^2 = a^2 + b^2 - 2 \cdot a \cdot b \cdot \cos(\gamma)", color = BLACK,
				   font_size = 48).next_to(t_cos2, DOWN)

		t_sin = MathTex(r"\frac{a}{\sin(\alpha)} = \frac{b}{\sin(\beta)} = \frac{c}{\sin(\gamma)}",
				  color = BLACK, font_size = 48).next_to(t_cos3, DOWN).shift(0.25 * DOWN)

		self.play(Write(t_cos1), run_time = 1)
		self.play(Write(t_cos2), run_time = 1)
		self.play(Write(t_cos3), run_time = 1)
		self.wait(1)
		self.play(Write(t_sin), run_time = 1)
		self.wait(2)

	def showa2(self):
		ref_a_len = 3
		ref_b_len = 4
		ref_gamma_deg = 40 / 180 * math.pi

		ref_a_start = 6 * LEFT + 3 * UP
		ref_a = Line(ref_a_start, ref_a_start + ref_a_len * RIGHT, color = BLUE, stroke_width=3)
		ref_a_t = MathTex(r"a", color = BLUE).next_to(ref_a, UP).shift(0.2 * DOWN)
		ref_b_start = 6 * LEFT + 2 * UP
		ref_b = Line(ref_b_start, ref_b_start + ref_b_len * RIGHT, color = GREEN, stroke_width=3)
		ref_b_t = MathTex(r"b", color = GREEN).next_to(ref_b, UP).shift(0.2 * DOWN)
		ref_gamma_start = 6 * LEFT + 0.5 * UP
		ref_gamma_d1 = RIGHT
		ref_gamma_d2 = math.cos(ref_gamma_deg) * RIGHT + math.sin(ref_gamma_deg) * UP
		ref_gamma_l1 = Line(ref_gamma_start, ref_gamma_start + ref_gamma_d1, color = BLACK, stroke_width=3)
		ref_gamma_l2 = Line(ref_gamma_start, ref_gamma_start + ref_gamma_d2, color = BLACK, stroke_width=3)
		#ref_gamma_ang = Angle(ref_gamma_l1, ref_gamma_l2, radius=0.35, color=BLACK)
		ref_gamma_ang = get_vgroup_angles(ref_gamma_start, ref_gamma_start + ref_gamma_d1,
									ref_gamma_start + ref_gamma_d2, 0.35, 1)
		ref_gamma_t = MathTex(r"\gamma", color = BLACK, font_size = 38).next_to(ref_gamma_ang, RIGHT)\
			.shift(0.25 * LEFT + 0.05 * UP)
		ref_gamma_group = VGroup(ref_gamma_l1, ref_gamma_l2, ref_gamma_ang, ref_gamma_t)

		self.wait(1)
		self.play(Create(ref_a), Write(ref_a_t), Create(ref_b), Write(ref_b_t), Create(ref_gamma_l1),
			Create(ref_gamma_l2), Create(ref_gamma_ang), Write(ref_gamma_t), run_time = 1)
		self.wait(2)

		text1 = MathTex(r"c = \sqrt{a^2 + b^2 - 2 \cdot a \cdot b \cdot \cos(\gamma)}", color = BLACK,
				  font_size = 44).shift(3 * RIGHT + 1.5 * UP)

		copy_gamma_group = ref_gamma_group.copy()
		copy_gamma_new_pos = 6 * LEFT + 2.5 * DOWN
		ang_l1 = Line(copy_gamma_new_pos, copy_gamma_new_pos + ref_gamma_d1 * 5, color = BLACK,
				stroke_width=3)
		ang_l2 = Line(copy_gamma_new_pos, copy_gamma_new_pos + ref_gamma_d2 * 5, color = BLACK,
				stroke_width=3)

		pc = copy_gamma_new_pos
		pb = pc + ref_a_len * (math.cos(ref_gamma_deg) * RIGHT + math.sin(ref_gamma_deg) * UP)
		pa = pc + ref_b_len * RIGHT

		la = Line(pc, pb, color = BLUE, stroke_width=5.5)
		la_t = MathTex(r"a", color = BLUE).next_to(la, UP).shift(1.0 * DOWN)
		lb = Line(pc, pa, color = GREEN, stroke_width=5.5)
		lb_t = MathTex(r"b", color = GREEN).next_to(lb, DOWN).shift(0.15 * UP)
		
		lc = Line(pa, pb, color = RED, stroke_width=3)
		lc_t = MathTex(r"c", color = RED).next_to(lc, RIGHT).shift(0.9 * LEFT)

		#ang_alpha = Angle(Line(pa, pb), Line(pa, pc), radius=0.35, color=BLACK)
		ang_alpha = get_vgroup_angles(pa, pb, pc, 0.35, 2)
		ang_alpha_t = MathTex(r"\alpha", color = BLACK, font_size = 38).next_to(ang_alpha, LEFT)\
			.shift(0.15 * RIGHT + 0.05 * UP)
		#ang_beta = Angle(Line(pb, pc), Line(pb, pa), radius=0.35, color=BLACK)
		ang_beta = get_vgroup_angles(pb, pc, pa, 0.35, 3)
		ang_beta_t = MathTex(r"\beta", color = BLACK, font_size = 38).next_to(ang_beta, DOWN)\
			.shift(0.15 * UP)

		text2 = MathTex(r"\alpha = \arcsin \left( \frac{a \cdot \sin(\gamma)}{c} \right)", color = BLACK,
				  font_size = 44).next_to(text1, DOWN, buff = 0.5)
		text3 = MathTex(r"\beta = \arcsin \left( \frac{b \cdot \sin(\gamma)}{c} \right)", color = BLACK,
				  font_size = 44).next_to(text2, DOWN, buff = 0.2)

		self.play(Write(text1), run_time = 1)
		self.wait(1)
		g_box = get_vgroup_bounding_box(ref_gamma_group)
		g_pos = copy_gamma_new_pos + 0.5 * (g_box[2] - g_box[0])
		self.play(copy_gamma_group.animate.move_to(g_pos), run_time = 1)
		self.play(Create(ang_l1), Create(ang_l2), run_time = 1)
		self.wait(1)
		self.play(TransformFromCopy(ref_a, la), Write(la_t), run_time = 1)
		self.wait(1)
		self.play(TransformFromCopy(ref_b, lb), Write(lb_t), run_time = 1)
		self.wait(1)
		self.play(Create(lc), Write(lc_t), run_time = 1)
		self.wait(1)
		self.play(Create(ang_alpha), Write(ang_alpha_t), Create(ang_beta), Write(ang_beta_t), run_time = 1)
		self.wait(1)
		self.play(Write(text2), run_time = 1)
		self.play(Write(text3), run_time = 1)
		self.wait(5)

	def showa3(self):
		ref_c_len = 5
		ref_alpha_deg = 30 / 180 * math.pi
		ref_beta_deg = 50 / 180 * math.pi

		ref_c_start = 6 * LEFT + 3 * UP
		ref_c = Line(ref_c_start, ref_c_start + ref_c_len * RIGHT, color = RED, stroke_width=3)
		ref_c_t = MathTex(r"c", color = RED).next_to(ref_c, UP).shift(0.2 * DOWN)

		ref_alpha_start = 6 * LEFT + 2.2 * UP
		ref_alpha_d1 = RIGHT
		ref_alpha_d2 = math.cos(ref_alpha_deg) * RIGHT + math.sin(ref_alpha_deg) * UP
		ref_alpha_l1 = Line(ref_alpha_start, ref_alpha_start + ref_alpha_d1, color = BLACK, stroke_width=3)
		ref_alpha_l2 = Line(ref_alpha_start, ref_alpha_start + ref_alpha_d2, color = BLACK, stroke_width=3)
		#ref_alpha_ang = Angle(ref_alpha_l1, ref_alpha_l2, radius=0.35, color=BLACK)
		ref_alpha_ang = get_vgroup_angles(ref_alpha_start, ref_alpha_start + ref_alpha_d1,
									ref_alpha_start + ref_alpha_d2, 0.35, 1)
		ref_alpha_t = MathTex(r"\alpha", color = BLACK, font_size = 36).next_to(ref_alpha_ang, RIGHT)\
			.shift(0.15 * LEFT + 0.05 * UP)

		ref_beta_start = 6 * LEFT + 1.0 * UP
		ref_beta_d1 = RIGHT
		ref_beta_d2 = math.cos(ref_beta_deg) * RIGHT + math.sin(ref_beta_deg) * UP
		ref_beta_l1 = Line(ref_beta_start, ref_beta_start + ref_beta_d1, color = BLACK, stroke_width=3)
		ref_beta_l2 = Line(ref_beta_start, ref_beta_start + ref_beta_d2, color = BLACK, stroke_width=3)
		#ref_beta_ang = Angle(ref_beta_l1, ref_beta_l2, radius=0.35, color=BLACK)
		ref_beta_ang = get_vgroup_angles(ref_beta_start, ref_beta_start + ref_beta_d1,
								   ref_beta_start + ref_beta_d2, 0.35, 2)
		ref_beta_t = MathTex(r"\beta", color = BLACK, font_size = 36).next_to(ref_beta_ang, RIGHT)\
			.shift(0.2 * LEFT + 0.1 * UP)

		self.wait(1)
		self.play(Create(ref_c), Write(ref_c_t), Create(ref_alpha_l1), Create(ref_alpha_l2),
			Create(ref_alpha_ang), Write(ref_alpha_t), Create(ref_beta_l1), Create(ref_beta_l2),
			Create(ref_beta_ang), Write(ref_beta_t), run_time = 1)
		self.wait(2)

		baseline = Line(6 * LEFT + 2.5 * DOWN, 2 * RIGHT + 2.5 * DOWN, color = BLACK, stroke_width=3)

		pa = 5 * LEFT + 2.5 * DOWN
		pb = pa + ref_c_len * RIGHT
		b_lenth = ref_c_len / math.sin(math.pi - ref_beta_deg - ref_alpha_deg) * math.sin(ref_beta_deg)
		pc = pa + b_lenth * math.cos(ref_alpha_deg) * RIGHT + b_lenth * math.sin(ref_alpha_deg) * UP

		la = Line(pb, pc, color = BLUE, stroke_width=3)
		la_t = MathTex(r"a", color = BLUE).next_to(la, RIGHT).shift(0.9 * LEFT)
		lb = Line(pc, pa, color = GREEN, stroke_width=3)
		lb_t = MathTex(r"b", color = GREEN).next_to(lb, LEFT).shift(1.5 * RIGHT)
		lc = Line(pa, pb, color = RED, stroke_width=6)
		lc_t = MathTex(r"c", color = RED).next_to(lc, DOWN).shift(0.15 * UP)
		
		pre_alpha_l = Line(pa, pa + ref_alpha_d2, color = BLACK, stroke_width=1)
		#pre_alpha_ang = Angle(Line(pa, pa + ref_alpha_d1), Line(pa, pa + ref_alpha_d2), radius=0.35,
		#				color=BLACK)
		pre_alpha_ang = get_vgroup_angles(pa, pa + ref_alpha_d1, pa + ref_alpha_d2, 0.35, 1)
		pre_alpha_t = MathTex(r"\alpha", color = BLACK, font_size = 36).next_to(pre_alpha_ang, RIGHT)\
			.shift(0.15 * LEFT + 0.08 * UP)
		pre_beta_d = math.cos(ref_beta_deg) * LEFT + math.sin(ref_beta_deg) * UP
		pre_beta_l = Line(pb, pb + pre_beta_d, color = BLACK, stroke_width=1)
		#pre_beta_ang = Angle(Line(pb, pb + pre_beta_d), Line(pb, pb - ref_beta_d1), radius=0.35,
		#			   color=BLACK)
		pre_beta_ang = get_vgroup_angles(pb, pb + pre_beta_d, pb - ref_beta_d1, 0.35, 2)
		pre_beta_t = MathTex(r"\beta", color = BLACK, font_size = 36).next_to(pre_beta_ang, LEFT)\
			.shift(0.18 * RIGHT + 0.13 * UP)

		full_alpha_l = Line(pa, pa + ref_alpha_d2 * 5, color = BLACK, stroke_width=2)
		full_beta_l = Line(pb, pb + pre_beta_d * 3.5, color = BLACK, stroke_width=2)

		ang_gamma = get_vgroup_angles(pc, pa, pb, 0.35, 3)
		ang_gamma_t = MathTex(r"\gamma", color = BLACK, font_size = 36).next_to(ang_gamma, DOWN, buff = 0.1)

		text1 = MathTex(r"\gamma = 180 - \alpha - \beta", color = BLACK).shift(2 * UP + 3 * RIGHT)
		text2 = MathTex(r"a = \frac{c \cdot \sin(\beta)}{\sin(\gamma)}", color = BLACK)\
			.next_to(text1, DOWN, buff = 0.5)
		text3 = MathTex(r"b = \frac{c \cdot \sin(\alpha)}{\sin(\gamma)}", color = BLACK)\
			.next_to(text2, DOWN, buff = 0.2)

		self.play(Create(baseline), run_time = 1)
		self.wait(1)
		self.play(TransformFromCopy(ref_c, lc), Write(lc_t), time = 1.0)
		self.wait(1)
		self.play(TransformFromCopy(ref_alpha_l2, pre_alpha_l),
			TransformFromCopy(ref_alpha_ang, pre_alpha_ang),
			Write(pre_alpha_t), run_time = 1)
		self.play(TransformFromCopy(ref_beta_l2, pre_beta_l),
			TransformFromCopy(ref_beta_ang, pre_beta_ang),
			Write(pre_beta_t), run_time = 1)
		self.wait(1)
		self.play(Create(full_alpha_l), Create(full_beta_l), run_time = 1)
		self.wait(1)
		self.play(Create(la), Write(la_t), Create(lb), Write(lb_t), run_time = 1)
		self.wait(1)
		self.play(Write(text1), Create(ang_gamma), Write(ang_gamma_t), run_time = 1)
		self.play(Write(text2), run_time = 1)
		self.play(Write(text3), run_time = 1)
		self.wait(5)

	def showa4(self):
		pa = 2.5 * LEFT + 2.5 * DOWN
		pb = 4.5 * LEFT + 2.5 * UP
		pc = 6.0 * LEFT + 1.5 * DOWN

		da = Dot(pa, color = BLACK, radius=0.05)
		db = Dot(pb, color = BLACK, radius=0.05)
		dc = Dot(pc, color = BLACK, radius=0.05)

		la = Line(pc, pb, color = BLUE, stroke_width=3)
		lb = Line(pa, pc, color = GREEN, stroke_width=3)
		lc = Line(pa, pb, color = RED, stroke_width=3)

		tla = MathTex(r"a", color = BLUE).next_to(la, LEFT).shift(0.8 * RIGHT)
		tlb = MathTex(r"b", color = GREEN).next_to(lb, DOWN).shift(0.6 * UP)
		tlc = MathTex(r"c", color = RED).next_to(lc, RIGHT).shift(1.1 * LEFT)

		#ang_alpha = Angle(Line(pa, pb), Line(pa, pc), radius=0.35, color=BLACK)
		ang_alpha = get_vgroup_angles(pa, pb, pc, 0.35, 1)
		#ang_beta = Angle(Line(pb, pc), Line(pb, pa), radius=0.35, color=BLACK)
		ang_beta = get_vgroup_angles(pb, pc, pa, 0.35, 2)
		#ang_gamma = Angle(Line(pc, pa), Line(pc, pb), radius=0.35, color=BLACK)
		ang_gamma = get_vgroup_angles(pc, pa, pb, 0.35, 3)

		ta_alpha = MathTex(r"\alpha", color = BLACK, font_size = 38).next_to(ang_alpha, LEFT)\
			.shift(0.3 * RIGHT + 0.2 * UP)
		ta_beta = MathTex(r"\beta", color = BLACK, font_size = 38).next_to(ang_beta, DOWN)\
			.shift(0.2 * UP)
		ta_gamma = MathTex(r"\gamma", color = BLACK, font_size = 38).next_to(ang_gamma, RIGHT)\
			.shift(0.25 * LEFT + 0.05 * UP)

		text_cos_alpha = MathTex(r"\alpha = \arccos \left( \frac{b^2 + c^2 - a^2}{2 \cdot b \cdot c} \right)",
						  color = BLACK, font_size = 36).shift(2.5 * RIGHT + 1.5 * UP)
		text_cos_beta = MathTex(r"\beta = \arccos \left( \frac{a^2 + c^2 - b^2}{2 \cdot a \cdot c} \right)",
						  color = BLACK, font_size = 36).next_to(text_cos_alpha, DOWN, buff = 0.5)
		text_cos_gamma = MathTex(r"\gamma = \arccos \left( \frac{a^2 + b^2 - c^2}{2 \cdot a \cdot b} \right)",
						   color = BLACK, font_size = 36).next_to(text_cos_beta, DOWN, buff = 0.5)

		self.wait(1)
		self.play(Create(da), Create(db), Create(dc), run_time = 1)
		self.wait(0.5)
		self.play(Create(la), Create(lb), Create(lc), Write(tla), Write(tlb), Write(tlc), run_time = 1)
		self.wait(1)
		self.play(Create(ang_alpha), Write(ta_alpha), Write(text_cos_alpha), run_time = 1)
		self.play(Create(ang_beta), Write(ta_beta), Write(text_cos_beta), run_time = 1)
		self.play(Create(ang_gamma), Write(ta_gamma), Write(text_cos_gamma), run_time = 1)
		self.wait(4)

	def showa5(self):
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{xcolor}")

		t1_bp = 6 * LEFT + 1.5 * UP
		t2_bp = 6 * LEFT + 2.0 * DOWN
		a_d = ORIGIN
		b_d = 0.2 * RIGHT + 1 * UP
		c_d = 1.3 * RIGHT + 0.3 * DOWN

		t1_pa = t1_bp + a_d * 2
		t1_pb = t1_bp + b_d * 2
		t1_pc = t1_bp + c_d * 2
		t2_pa = t2_bp + a_d * 3
		t2_pb = t2_bp + b_d * 3
		t2_pc = t2_bp + c_d * 3

		t1_da = Dot(t1_pa, color = BLACK, radius=0.05)
		t1_db = Dot(t1_pb, color = BLACK, radius=0.05)
		t1_dc = Dot(t1_pc, color = BLACK, radius=0.05)
		t2_da = Dot(t2_pa, color = BLACK, radius=0.05)
		t2_db = Dot(t2_pb, color = BLACK, radius=0.05)
		t2_dc = Dot(t2_pc, color = BLACK, radius=0.05)

		t1_la = Line(t1_pb, t1_pc, color = BLUE, stroke_width=3)
		t1_lb = Line(t1_pa, t1_pc, color = GREEN, stroke_width=3)
		t1_lc = Line(t1_pa, t1_pb, color = RED, stroke_width=3)
		t2_la = Line(t2_pb, t2_pc, color = BLUE, stroke_width=3)
		t2_lb = Line(t2_pa, t2_pc, color = GREEN, stroke_width=3)
		t2_lc = Line(t2_pa, t2_pb, color = RED, stroke_width=3)

		t1_la_t = MathTex(r"a", color = BLUE).next_to(t1_la, RIGHT).shift(1.1 * LEFT)
		t1_lb_t = MathTex(r"b", color = GREEN).next_to(t1_lb, DOWN).shift(0.5 * UP)
		t1_lc_t = MathTex(r"c", color = RED).next_to(t1_lc, LEFT).shift(0.35 * RIGHT)
		t2_la_t = MathTex(r"d", color = BLUE).next_to(t2_la, RIGHT).shift(1.65 * LEFT)
		t2_lb_t = MathTex(r"e", color = GREEN).next_to(t2_lb, DOWN).shift(0.6 * UP)
		t2_lc_t = MathTex(r"f", color = RED).next_to(t2_lc, LEFT).shift(0.5 * RIGHT)

		#t1_alpha_ang = Angle(Line(t1_pa, t1_pc), Line(t1_pa, t1_pb), radius=0.4, color = BLACK)
		t1_alpha_ang = get_vgroup_angles(t1_pa, t1_pc, t1_pb, 0.4, 1)
		#t1_beta_ang = Angle(Line(t1_pb, t1_pa), Line(t1_pb, t1_pc), radius=0.4, color = BLACK)
		t1_beta_ang = get_vgroup_angles(t1_pb, t1_pa, t1_pc, 0.4, 2)
		#t1_gamma_ang = Angle(Line(t1_pc, t1_pb), Line(t1_pc, t1_pa), radius=0.4, color = BLACK)
		t1_gamma_ang = get_vgroup_angles(t1_pc, t1_pb, t1_pa, 0.4, 3)
		#t2_alpha_ang = Angle(Line(t2_pa, t2_pc), Line(t2_pa, t2_pb), radius=0.4, color = BLACK)
		t2_alpha_ang = get_vgroup_angles(t2_pa, t2_pc, t2_pb, 0.4, 1)
		#t2_beta_ang = Angle(Line(t2_pb, t2_pa), Line(t2_pb, t2_pc), radius=0.4, color = BLACK)
		t2_beta_ang = get_vgroup_angles(t2_pb, t2_pa, t2_pc, 0.4, 2)
		#t2_gamma_ang = Angle(Line(t2_pc, t2_pb), Line(t2_pc, t2_pa), radius=0.4, color = BLACK)
		t2_gamma_ang = get_vgroup_angles(t2_pc, t2_pb, t2_pa, 0.4, 3)

		t1_alpha_t = MathTex(r"\alpha", color = BLACK, font_size = 36).next_to(t1_alpha_ang, RIGHT).shift(0.2 * LEFT)
		t1_beta_t = MathTex(r"\beta", color = BLACK, font_size = 36).next_to(t1_beta_ang, DOWN).shift(0.2 * UP)
		t1_gamma_t = MathTex(r"\gamma", color = BLACK, font_size = 36).next_to(t1_gamma_ang, LEFT)\
			.shift(0.25 * RIGHT + 0.1 * UP)
		t2_alpha_t = MathTex(r"\alpha", color = BLACK, font_size = 36).next_to(t2_alpha_ang, RIGHT).shift(0.2 * LEFT)
		t2_beta_t = MathTex(r"\beta", color = BLACK, font_size = 36).next_to(t2_beta_ang, DOWN).shift(0.2 * UP)
		t2_gamma_t = MathTex(r"\gamma", color = BLACK, font_size = 36).next_to(t2_gamma_ang, LEFT)\
			.shift(0.25 * RIGHT + 0.1 * UP)

		self.wait(1)
		self.play(Create(t1_da), Create(t1_db), Create(t1_dc), Create(t2_da), Create(t2_db), Create(t2_dc),
			run_time = 1)
		self.wait(0.5)
		self.play(Create(t1_la), Create(t1_lb), Create(t1_lc), Create(t2_la), Create(t2_lb), Create(t2_lc),
			run_time = 1)
		self.wait(1)
		self.play(Create(t1_alpha_ang), Create(t1_beta_ang), Create(t1_gamma_ang), Create(t2_alpha_ang),
			Create(t2_beta_ang), Create(t2_gamma_ang), run_time = 1)
		self.wait(0.5)
		self.play(Write(t1_alpha_t), Write(t1_beta_t), Write(t1_gamma_t), Write(t2_alpha_t),
			Write(t2_beta_t), Write(t2_gamma_t), run_time = 1)
		self.wait(2)
		self.play(Write(t1_la_t), Write(t1_lb_t), Write(t1_lc_t), Write(t2_la_t), Write(t2_lb_t),
			Write(t2_lc_t), run_time = 1)
		self.wait(2)

		text1 = MathTex(r"\frac{a}{\sin(\alpha)} = \frac{b}{\sin(\beta)}", color = BLACK,
				  font_size = 36).shift(2.5 * UP + 1.5 * RIGHT)
		text2 = MathTex(r"\frac{d}{\sin(\alpha)} = \frac{e}{\sin(\beta)}", color = BLACK,
				  font_size = 36).next_to(text1, DOWN)

		text3_1 = MathTex(r"\frac{a}{b} = \frac{\sin(\alpha)}{\sin(\beta)}", color = BLACK, font_size = 36)
		text3_2 = MathTex(r"\frac{d}{e} = \frac{\sin(\alpha)}{\sin(\beta)}", color = BLACK, font_size = 36)
		text3 = VGroup(text3_1, text3_2).arrange(RIGHT, aligned_edge = UP, buff = 0.5)\
			.next_to(text2, DOWN, buff = 0.5)

		text4 = MathTex(r"\frac{\textcolor{blue}{a}}{\textcolor{green}{b}} = "
				  r"\frac{\textcolor{blue}{d}}{\textcolor{green}{e}}",
				  tex_template = myTemplate, color = BLACK, font_size = 36)
		text5 = MathTex(r"\frac{\textcolor{blue}{a}}{\textcolor{red}{c}} = "
				  r"\frac{\textcolor{blue}{d}}{\textcolor{red}{f}}",
				  tex_template = myTemplate, color = BLACK, font_size = 36)
		text6 = MathTex(r"\frac{\textcolor{green}{b}}{\textcolor{red}{c}} = "
				  r"\frac{\textcolor{green}{e}}{\textcolor{red}{f}}",
				  tex_template = myTemplate, color = BLACK, font_size = 36)
		
		t456_g = VGroup(text4, text5, text6).arrange(RIGHT, aligned_edge = UP, buff = 1.0)\
			.next_to(text3, DOWN, buff = 0.75)

		sur_box1 = SurroundingRectangle(text4, buff=0.2)
		sur_box1.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)
		sur_box2 = SurroundingRectangle(text5, buff=0.2)
		sur_box2.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)
		sur_box3 = SurroundingRectangle(text6, buff=0.2)
		sur_box3.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		self.play(Write(text1), run_time = 1)
		self.wait(1)
		self.play(Write(text2), run_time = 1)
		self.wait(1)
		self.play(Write(text3), run_time = 1)
		self.wait(1)
		self.play(Write(text4), Create(sur_box1), run_time = 1)
		self.wait(2)
		self.play(Write(text5), Create(sur_box2), run_time = 1)
		self.wait(1)
		self.play(Write(text6), Create(sur_box3), run_time = 1)
		self.wait(5)

	def showa6(self):
		pa = 6 * LEFT + 2.5 * DOWN
		pb = 3 * LEFT + 1.5 * DOWN
		pc = 4 * LEFT + 2.5 * UP

		da = Dot(pa, color = BLACK, radius = 0.05)
		db = Dot(pb, color = BLACK, radius = 0.05)
		dc = Dot(pc, color = BLACK, radius = 0.05)

		da_t = MathTex("A", color = BLACK, font_size = 36).next_to(da, DOWN, buff = 0.1)
		db_t = MathTex("B", color = BLACK, font_size = 36).next_to(db, DOWN, buff = 0.1)
		dc_t = MathTex("C", color = BLACK, font_size = 36).next_to(dc, UP, buff = 0.1)

		la = Line(pc, pb, color = BLACK, stroke_width = 3)
		lb = Line(pa, pc, color = BLACK, stroke_width = 3)
		lc = Line(pa, pb, color = BLACK, stroke_width = 3)

		f_size = 36

		eq1 = MathTex(r"S_{ABC} = 18", color = BLACK, font_size = f_size)

		pk = pa + (2.0 / 3.0) * (pb - pa)
		dk = Dot(pk, color = BLACK, radius = 0.05)
		dk_t = MathTex("K", color = BLACK, font_size = 36).next_to(dk, DOWN, buff = 0.1).shift(0.15 * LEFT)

		eq2 = MathTex(r"AK = \tfrac{2}{3} AB", color = BLACK, font_size = f_size)

		pl = pa + (2.0 / 3.0) * (pc - pa)
		dl = Dot(pl, color = BLACK, radius = 0.05)
		dl_t = MathTex("L", color = BLACK, font_size = 36).next_to(dl, LEFT, buff = 0.1)

		l_kl = Line(pk - 0.3 * (pl - pk), pl - 0.3 * (pk - pl), color = BLACK, stroke_width = 3)

		eq3 = MathTex(r"BC \parallel KL", color = BLACK, font_size = f_size)
		
		eq123_g = VGroup(eq1, eq2, eq3).arrange(RIGHT, aligned_edge = UP, buff = 0.5)\
			.shift(3 * UP + 1 * RIGHT)

		eq4 = MathTex(r"S_{AKL} = ?", color = BLACK, font_size = f_size).next_to(eq123_g, DOWN, buff = 0.2)

		self.wait(1)
		self.play(Create(da), Create(db), Create(dc), Write(da_t), Write(db_t), Write(dc_t), run_time = 1)
		self.play(Create(la), Create(lb), Create(lc), run_time = 1)
		self.wait(1)
		self.play(Write(eq1), run_time = 1)
		self.wait(1)
		self.play(Create(dk), Write(dk_t), run_time = 1)
		self.play(Write(eq2), run_time = 1)
		self.wait(1)
		self.play(Create(l_kl), run_time = 1)
		self.wait(1)
		self.play(Create(dl), Write(dl_t), run_time = 1)
		self.play(Write(eq3), run_time = 1)
		self.wait(1)
		self.play(Write(eq4), run_time = 1)
		self.wait(2)

		#ang_a = Angle(Line(pa, pb), Line(pa, pc), radius = 0.35, color = BLACK, stroke_width = 3)
		ang_a = get_vgroup_angles(pa, pb, pc, 0.35, 1)
		#ang_b = Angle(Line(pb, pc), Line(pb, pa), radius = 0.35, color = BLACK, stroke_width = 3)
		ang_b = get_vgroup_angles(pb, pc, pa, 0.35, 2)
		#ang_c = Angle(Line(pc, pa), Line(pc, pb), radius = 0.35, color = BLACK, stroke_width = 3)
		ang_c = get_vgroup_angles(pc, pa, pb, 0.35, 3)

		ang_a_t = MathTex(r"\alpha", color = BLACK, font_size = 36).next_to(ang_a, RIGHT, buff = 0.1)\
			.shift(0.2 * UP + 0.1 * LEFT)
		ang_b_t = MathTex(r"\beta", color = BLACK, font_size = 36).next_to(ang_b, LEFT, buff = 0.05)
		ang_c_t = MathTex(r"\gamma", color = BLACK, font_size = 36).next_to(ang_c, DOWN, buff = 0.1)

		#ang_k = Angle(Line(pk, pl), Line(pk, pa), radius = 0.35, color = BLACK, stroke_width = 3)
		ang_k = get_vgroup_angles(pk, pl, pa, 0.35, 2)
		ang_k_t = MathTex(r"\beta", color = BLACK, font_size = 36).next_to(ang_k, LEFT, buff = 0.05)

		#ang_l = Angle(Line(pl, pa), Line(pl, pk), radius = 0.35, color = BLACK, stroke_width = 3)
		ang_l = get_vgroup_angles(pl, pa, pk, 0.35, 3)
		ang_l_t = MathTex(r"\gamma", color = BLACK, font_size = 36).next_to(ang_l, DOWN, buff = 0.1)

		eq5 = MathTex(r"\triangle ABC \sim \triangle AKL", color = BLACK, font_size = f_size)\
			.next_to(eq4, DOWN, buff = 0.2)

		self.play(Create(ang_a), Create(ang_b), Create(ang_c), Write(ang_a_t), Write(ang_b_t),
			Write(ang_c_t), run_time = 1)
		self.wait(1)
		self.play(Create(ang_k), Write(ang_k_t), run_time = 1)
		self.wait(1)
		self.play(Create(ang_l), Write(ang_l_t), run_time = 1)
		self.wait(1)
		self.play(Write(eq5), run_time = 1)
		self.wait(1)

		eq6 = MathTex(r"\frac{AK}{AB} = \frac{AL}{AC}", color = BLACK, font_size = f_size)\
			.next_to(eq5, DOWN, buff = 0.2)
		eq7 = MathTex(r"\frac{\tfrac{2}{3} AB}{AB} = \frac{AL}{AC}", color = BLACK, font_size = f_size)\
			.next_to(eq6, DOWN, buff = 0.2)
		eq8 = MathTex(r"\frac{2}{3} = \frac{AL}{AC}", color = BLACK, font_size = f_size)\
			.next_to(eq7, DOWN, buff = 0.2)
		eq9 = MathTex(r"AL = \tfrac{2}{3} AC", color = BLACK, font_size = f_size)\
			.next_to(eq8, DOWN, buff = 0.2)

		self.play(Write(eq6), run_time = 1)
		self.wait(1)
		self.play(Write(eq7), run_time = 1)
		self.wait(1)
		self.play(Write(eq8), run_time = 1)
		self.wait(1)
		self.play(Write(eq9), run_time = 1)
		self.wait(1)
		self.play(FadeOut(eq6), FadeOut(eq7), FadeOut(eq8), run_time = 1)
		self.wait(1)
		self.play(eq9.animate().shift(3.0 * UP), run_time = 1)
		self.wait(1)

		eq10 = MathTex(r"S = \tfrac{1}{2} \cdot a \cdot b \cdot \sin(\alpha)", color = BLACK,
				 font_size = f_size).next_to(eq9, DOWN, buff = 0.5)
		eq11 = MathTex(r"S_{AKL} = \tfrac{1}{2} \cdot AK \cdot AL \cdot \sin(\alpha)", color = BLACK,
				 font_size = f_size).next_to(eq9, DOWN, buff = 0.5)
		eq12 = MathTex(r"S_{AKL} = \tfrac{1}{2} \cdot \tfrac{2}{3} AB \cdot \tfrac{2}{3} AC \cdot "
				 r"\sin(\alpha)", color = BLACK, font_size = f_size).next_to(eq11, DOWN, buff = 0.3)
		eq13 = MathTex(r"S_{AKL} = \tfrac{4}{9} \cdot \tfrac{1}{2} AB \cdot AC \cdot \sin(\alpha)",
				 color = BLACK, font_size = f_size).next_to(eq12, DOWN, buff = 0.3)
		eq14 = MathTex(r"S_{AKL} = \tfrac{4}{9} \cdot 18", color = BLACK, font_size = f_size)\
			.next_to(eq13, DOWN, buff = 0.3)
		eq15 = MathTex(r"S_{AKL} = 8", color = BLACK, font_size = f_size).next_to(eq14, DOWN, buff = 0.3)

		sur_box = SurroundingRectangle(eq15, buff=0.2)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		self.play(Write(eq10), run_time = 1)
		self.wait(1)
		self.play(Transform(eq10, eq11), run_time = 1)
		self.wait(1)
		self.play(Write(eq12), run_time = 1)
		self.wait(1)
		self.play(Write(eq13), run_time = 1)
		self.wait(1)
		self.play(Write(eq14), run_time = 1)
		self.wait(1)
		self.play(Write(eq15), run_time = 1)
		self.play(Create(sur_box), run_time = 1)
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
