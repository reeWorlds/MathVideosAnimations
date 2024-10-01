from manim import *
import math


def foot_of_perpendicular(pa, pb, pc):
	vec_pa = np.array(pa)
	vec_pb = np.array(pb)
	vec_pc = np.array(pc)
	line_vec = vec_pb - vec_pa
	pa_to_pc = vec_pc - vec_pa
	projection = np.dot(pa_to_pc, line_vec) / np.dot(line_vec, line_vec)
	foot_vec = vec_pa + projection * line_vec
	return foot_vec


class ExtraVid7(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])
		self.wait(1)

	def showa1(self):
		la_val = ValueTracker(3)
		lb_val = ValueTracker(3)
		lc_val = ValueTracker(3)
		lh_val = ValueTracker(3)
		lha_val = ValueTracker(3)
		lhb_val = ValueTracker(3)

		pa = 3 * LEFT + 2.8 * DOWN
		pb = 6 * LEFT + 2.8 * UP
		pc = 6 * LEFT + 2.8 * DOWN

		da = Dot(pa, color = BLACK, radius=0.08)
		da_t = MathTex(r"A", color = BLACK).next_to(da, RIGHT, buff=0.1)
		db = Dot(pb, color = BLACK, radius=0.08)
		db_t = MathTex(r"B", color = BLACK).next_to(db, LEFT, buff=0.1)
		dc = Dot(pc, color = BLACK, radius=0.08)
		dc_t = MathTex(r"C", color = BLACK).next_to(dc, LEFT, buff=0.1)

		la = always_redraw(lambda: Line(pc, pb, color = BLACK, stroke_width=la_val.get_value()))
		lb = always_redraw(lambda: Line(pa, pc, color = BLACK, stroke_width=lb_val.get_value()))
		lc = always_redraw(lambda: Line(pa, pb, color = BLACK, stroke_width=lc_val.get_value()))

		ang_c = RightAngle(Line(pc, pa), Line(pc, pb), length=0.35, color=BLACK)

		ph = foot_of_perpendicular(pa, pb, pc)
		dh = Dot(ph, color = BLACK, radius=0.08)
		dh_t = MathTex(r"H", color = BLACK).next_to(dh, RIGHT).shift(0.15 * UP)
		lh = always_redraw(lambda: Line(pc, ph, color = BLACK, stroke_width=lh_val.get_value()))
		ang_right1 = RightAngle(Line(ph, pc), Line(ph, pb), length=0.3, color=BLACK)

		lha = always_redraw(lambda: Line(pa, ph, color = BLACK, stroke_width=lha_val.get_value()))
		lhb = always_redraw(lambda: Line(pb, ph, color = BLACK, stroke_width=lhb_val.get_value()))

		self.wait(1)
		self.play(Create(da), Write(da_t), Create(db), Write(db_t), Create(dc), Write(dc_t), run_time = 1)
		self.play(Write(la), Write(lb), Write(lc), run_time = 1)
		self.play(Create(ang_c), run_time = 1)
		self.wait(1)
		self.play(Create(dh), Write(dh_t), Create(lh), Create(ang_right1), run_time = 1)
		self.add(lha, lhb)
		self.wait(2)

		ang_a = Angle(Line(pa, pb), Line(pa, pc), radius=0.35, color=BLACK)
		ang_a_t = MathTex(r"\alpha", color = BLACK, font_size = 38).next_to(ang_a, LEFT)\
			.shift(0.1 * UP + 0.2 * RIGHT)
		
		ang_b = VGroup(Angle(Line(pb, pc), Line(pb, pa), radius=0.45, color=BLACK),
				 Angle(Line(pb, pc), Line(pb, pa), radius=0.55, color=BLACK))
		ang_b_t = MathTex(r"\beta", color = BLACK, font_size = 38).next_to(ang_b, DOWN)\
			.shift(0.05 * RIGHT + 0.2 * UP)

		ang_b2 = VGroup(Angle(Line(pc, pa), Line(pc, ph), radius=0.55, color=BLACK),
				  Angle(Line(pc, pa), Line(pc, ph), radius=0.65, color=BLACK))
		ang_b2_t = MathTex(r"\beta", color = BLACK, font_size = 38).next_to(ang_b2, RIGHT)\
			.shift(0.05 * UP + 0.15 * LEFT)

		ang_a2 = Angle(Line(pc, ph), Line(pc, pb), radius=0.6, color=BLACK)
		ang_a2_t = MathTex(r"\alpha", color = BLACK, font_size = 38).next_to(ang_a2, UP)\
			.shift(0.25 * DOWN + 0.1 * RIGHT)

		self.play(Create(ang_a), Write(ang_a_t), run_time = 1)
		self.wait(0.5)
		self.play(Create(ang_b), Write(ang_b_t), run_time = 1)
		self.wait(1)
		self.play(lb_val.animate.set_value(7), lh_val.animate.set_value(7), lha_val.animate.set_value(7),
			run_time = 1)
		self.wait(1)
		self.play(Create(ang_b2), Write(ang_b2_t), run_time = 1)
		self.wait(1)
		self.play(lb_val.animate.set_value(3), lh_val.animate.set_value(3), lha_val.animate.set_value(3),
			run_time = 1)
		self.wait(1)
		self.play(la_val.animate.set_value(7), lh_val.animate.set_value(7), lhb_val.animate.set_value(7),
			run_time = 1)
		self.wait(1)
		self.play(Create(ang_a2), Write(ang_a2_t), run_time = 1)
		self.wait(1)
		self.play(la_val.animate.set_value(3), lh_val.animate.set_value(3), lhb_val.animate.set_value(3),
			run_time = 1)
		self.wait(2)

		eq1 = MathTex(r"\triangle ABC \sim \triangle ACH", color = BLACK, font_size = 48)\
			.shift(3 * UP + 0.15 * RIGHT)
		eq2 = MathTex(r"\triangle ABC \sim \triangle CBH", color = BLACK, font_size = 48)\
			.next_to(eq1, DOWN, aligned_edge=LEFT)

		self.play(Write(eq1), run_time = 1)
		self.wait(3)
		self.play(Write(eq2), run_time = 1)
		self.wait(2)

		l_a_text = MathTex(r"a", color = BLACK, font_size = 48).next_to(la, LEFT).shift(0.1 * RIGHT)
		l_b_text = MathTex(r"b", color = BLACK, font_size = 48).next_to(lb, DOWN).shift(0.1 * UP)
		l_c_text = MathTex(r"c", color = BLACK, font_size = 48).next_to(lc, RIGHT).shift(1.6 * LEFT)
		l_h_text = MathTex(r"h", color = BLACK, font_size = 48).next_to(lh, UP).shift(0.7 * DOWN)
		l_n_text = MathTex(r"n", color = BLACK, font_size = 48).next_to(lha, RIGHT).shift(0.45 * LEFT)
		l_m_text = MathTex(r"m", color = BLACK, font_size = 48).next_to(lhb, RIGHT).shift(1.2 * LEFT)

		gr_line_vals = VGroup(l_a_text, l_b_text, l_c_text, l_h_text, l_n_text, l_m_text)

		self.play(Write(gr_line_vals), run_time = 3)
		self.wait(3)

		eq1_1 = MathTex(r"\frac{CA}{CB} = \frac{HA}{HC}", color = BLACK, font_size = 48)\
			.next_to(eq2, DOWN, buff=0.3).shift(1.8 * LEFT)
		eq1_2 = MathTex(r"\frac{CA}{CB} = \frac{HC}{HB}", color = BLACK, font_size = 48)\
			.next_to(eq1_1, RIGHT, aligned_edge=UP, buff=0.8)

		eq1_3 = MathTex(r"\frac{HA}{HC} = \frac{HC}{HB}", color = BLACK, font_size = 48)\
			.next_to(VGroup(eq1_1, eq1_2), DOWN, buff=0.3)

		eq1_4 = MathTex(r"\frac{n}{h} = \frac{h}{m}", color = BLACK, font_size = 48)\
			.next_to(eq1_3, DOWN, buff=0.3)
		eq1_5 = MathTex(r"h^2 = n \cdot m", color = BLACK, font_size = 48)\
			.next_to(eq1_4, DOWN, buff=0.35)
		sur_box = SurroundingRectangle(eq1_5, buff=0.15)
		sur_box.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		g_eq1_5 = VGroup(eq1_5, sur_box)

		self.play(Write(eq1_1), run_time = 1)
		self.wait(1)
		self.play(Write(eq1_2), run_time = 1)
		self.wait(1)
		self.play(Write(eq1_3), run_time = 1)
		self.wait(1)
		self.play(Write(eq1_4), run_time = 1)
		self.wait(1)
		self.play(Write(eq1_5), run_time = 1)
		self.play(Create(sur_box), run_time = 1)
		self.wait(2)
		self.play(FadeOut(eq1_1), FadeOut(eq1_2), FadeOut(eq1_3), FadeOut(eq1_4), run_time = 1)
		self.play(g_eq1_5.animate.shift(4.0 * UP), run_time = 1)
		self.wait(2)

		eq2_1 = MathTex(r"\frac{HA}{CA} = \frac{CA}{BA}", color = BLACK, font_size = 48)\
			.next_to(eq1_5, DOWN, buff=0.5)
		eq2_2 = MathTex(r"\frac{n}{b} = \frac{b}{c}", color = BLACK, font_size = 48)\
			.next_to(eq2_1, DOWN, buff=0.3)
		eq2_3 = MathTex(r"b^2 = n \cdot c", color = BLACK, font_size = 48)\
			.next_to(eq2_2, DOWN, buff=0.35)
		sur_box2 = SurroundingRectangle(eq2_3, buff=0.15)
		sur_box2.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		g_eq2_3 = VGroup(eq2_3, sur_box2)

		self.play(Write(eq2_1), run_time = 1)
		self.wait(1)
		self.play(Write(eq2_2), run_time = 1)
		self.wait(1)
		self.play(Write(eq2_3), run_time = 1)
		self.play(Create(sur_box2), run_time = 1)
		self.wait(2)
		self.play(FadeOut(eq2_1), FadeOut(eq2_2), run_time = 1)
		self.play(g_eq2_3.animate.shift(2.6 * UP), run_time = 1)
		self.wait(2)

		eq3_1 = MathTex(r"\frac{HB}{CB} = \frac{CB}{AB}", color = BLACK, font_size = 48)\
			.next_to(eq2_3, DOWN, buff=0.4)
		eq3_2 = MathTex(r"\frac{m}{a} = \frac{a}{c}", color = BLACK, font_size = 48)\
			.next_to(eq3_1, DOWN, buff=0.3)
		eq3_3 = MathTex(r"a^2 = m \cdot c", color = BLACK, font_size = 48)\
			.next_to(eq3_2, DOWN, buff=0.35)
		sur_box3 = SurroundingRectangle(eq3_3, buff=0.15)
		sur_box3.set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width=4)

		g_eq3_3 = VGroup(eq3_3, sur_box3)

		self.play(Write(eq3_1), run_time = 1)
		self.wait(1)
		self.play(Write(eq3_2), run_time = 1)
		self.wait(1)
		self.play(Write(eq3_3), run_time = 1)
		self.play(Create(sur_box3), run_time = 1)
		self.wait(2)
		self.play(FadeOut(eq3_1), FadeOut(eq3_2), run_time = 1)
		self.play(g_eq3_3.animate.shift(2.5 * UP), run_time = 1)
		self.wait(4)


	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
