from manim import *
import math

def line_intersection(line1, line2):
	xdiff = (line1.get_start()[0] - line1.get_end()[0], line2.get_start()[0] - line2.get_end()[0])
	ydiff = (line1.get_start()[1] - line1.get_end()[1], line2.get_start()[1] - line2.get_end()[1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)

	d = (det(*line1.get_start_and_end()), det(*line2.get_start_and_end()))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return Dot(x * RIGHT + y * UP, color = BLACK, radius = 0.075)

def add_hash_mark(line, offset, n_hashes):
	angle = line.get_angle() + PI * 0.35
	hash_marks = VGroup()
	
	for i in range(n_hashes):
		pos = line.point_from_proportion(0.43 + (i+1)/(n_hashes+1) * 0.14)
		mark = Line(pos - offset * rotate_vector(RIGHT, angle), pos + offset * rotate_vector(RIGHT, angle),
					color=line.get_color(), stroke_width = 2)
		hash_marks.add(mark)
	
	return hash_marks

class TriangMedian(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		pa = Dot(4.5 * LEFT + 2 * DOWN, radius = 0.06, color = BLACK)
		pb = Dot(ORIGIN, radius = 0.06, color = BLACK)
		pc = Dot(3 * LEFT + 3 * UP, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK).next_to(pa, DOWN).shift(0.2 * LEFT + 0.3 * UP)
		pb_t = MathTex("B", color = BLACK).next_to(pb, DOWN).shift(0.2 * RIGHT + 0.3 * UP)
		pc_t = MathTex("C", color = BLACK).next_to(pc, UP).shift(0.2 * DOWN)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lb = Line(pa.get_center(), pc.get_center(), color = BLACK)
		lc = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lines = VGroup(la, lb, lc)

		mp = Dot(0.5 * (pb.get_center() + pc.get_center()), radius = 0.06, color = BLACK)
		mp_t = MathTex(r"M", color = BLACK).next_to(mp, UP).shift(0.2 * RIGHT + 0.2 * DOWN)
		median = Line(pa.get_center(), mp.get_center(), color = BLACK)
		mark1_1 = add_hash_mark(Line(mp.get_center(), pb.get_center(), color = BLACK), 0.15, 1)
		mark1_2 = add_hash_mark(Line(mp.get_center(), pc.get_center(), color = BLACK), 0.15, 1)
		txt1 = MathTex(r"BM = CM", color = BLACK).shift(3.5 * RIGHT + 2 * UP)

		kp = Dot(0.5 * (pa.get_center() + pc.get_center()), radius = 0.06, color = BLACK)
		kp_t = MathTex(r"K", color = BLACK).next_to(kp, LEFT).shift(0.2 * RIGHT)
		median2 = Line(pb.get_center(), kp.get_center(), color = BLACK)
		mark2_1 = add_hash_mark(Line(kp.get_center(), pa.get_center(), color = BLACK), 0.15, 2)
		mark2_2 = add_hash_mark(Line(kp.get_center(), pc.get_center(), color = BLACK), 0.15, 2)
		txt2 = MathTex(r"AK = CK", color = BLACK).next_to(txt1, DOWN)
		med2_g = VGroup(kp, median2, mark2_1, mark2_2)

		lp = Dot(0.5 * (pa.get_center() + pb.get_center()), radius = 0.06, color = BLACK)
		lp_t = MathTex(r"L", color = BLACK).next_to(lp, DOWN).shift(0.2 * UP)
		median3 = Line(pc.get_center(), lp.get_center(), color = BLACK)
		mark3_1 = add_hash_mark(Line(lp.get_center(), pa.get_center(), color = BLACK), 0.15, 3)
		mark3_2 = add_hash_mark(Line(lp.get_center(), pb.get_center(), color = BLACK), 0.15, 3)
		txt3 = MathTex(r"AL = BL", color = BLACK).next_to(txt2, DOWN)
		med3_g = VGroup(lp, median3, mark3_1, mark3_2)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Create(mp), Write(mp_t), Create(median), run_time = 2)
		self.play(Create(mark1_1, lag_ratio = 0), Create(mark1_2, lag_ratio = 0), run_time = 2)
		self.play(Write(txt1))

		self.wait(2)
		self.play(Create(med2_g, lag_ratio = 0), Write(kp_t), Write(txt2), run_time = 2)
		self.play(Create(med3_g, lag_ratio = 0), Write(lp_t), Write(txt3), run_time = 2)

		self.wait(2)

	def showa2(self):
		pa = Dot(6.2 * LEFT + 2 * DOWN, radius = 0.06, color = BLACK)
		pb = Dot(1.7 * LEFT, radius = 0.06, color = BLACK)
		pc = Dot(4.7 * LEFT + 3 * UP, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK).next_to(pa, DOWN).shift(0.2 * LEFT + 0.3 * UP)
		pb_t = MathTex("B", color = BLACK).next_to(pb, DOWN).shift(0.2 * RIGHT + 0.3 * UP)
		pc_t = MathTex("C", color = BLACK).next_to(pc, UP).shift(0.2 * DOWN)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lb = Line(pa.get_center(), pc.get_center(), color = BLACK)
		lc = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lines = VGroup(la, lb, lc)

		la_t = MathTex("a", color = BLACK).next_to(la, RIGHT).shift(1.5 * LEFT)
		lb_t = MathTex("b", color = BLACK).next_to(lb, LEFT).shift(0.8 * RIGHT)
		lc_t = MathTex("c", color = BLACK).next_to(lc, DOWN).shift(1 * UP)
		lines_t = VGroup(la_t, lb_t, lc_t)

		mp = Dot(0.5 * (pa.get_center() + pb.get_center()), radius = 0.06, color = BLACK)
		mp_t = MathTex(r"M", color = BLACK).next_to(mp, UP).shift(0.33 * DOWN + 0.35 * LEFT)
		median = Line(pc.get_center(), mp.get_center(), color = BLACK)
		median_t = MathTex(r"m", color = BLACK).next_to(median, RIGHT).shift(0.5 * LEFT)
		mark1 = add_hash_mark(Line(mp.get_center(), pa.get_center(), color = BLACK), 0.13, 1)
		mark2 = add_hash_mark(Line(mp.get_center(), pb.get_center(), color = BLACK), 0.13, 1)

		ang = Angle(Line(mp.get_center(), pb.get_center()), Line(mp.get_center(), pc.get_center()), radius = 0.5,
			 color = BLACK)
		ang_t = MathTex(r"\alpha", color = BLACK).next_to(ang, RIGHT).shift(0.5 * LEFT + 0.3 * UP)

		txt1 = MathTex(r"\angle{CMB} = \alpha", color = BLACK).shift(3 * UP + 3 * RIGHT)
		txt2 = MathTex(r"\angle{CMA} = 180^\circ - \alpha", color = BLACK).next_to(txt1, DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(lines_t, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Create(mp), Write(mp_t), Create(median), Write(median_t), run_time = 2)
		self.play(Create(mark1, lag_ratio = 0), Create(mark2, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(ang), Write(ang_t), run_time = 2)
		self.play(Write(txt1), Write(txt2), run_time = 2)

		txt3 = MathTex(r"\triangle{BMC}", color = BLACK).next_to(txt2, DOWN).shift(0.3 * DOWN)
		txt4 = MathTex(r"a^2 = (\frac{c}{2})^2 + m^2 - 2\frac{c}{2}m\cos(\alpha)", color = BLACK)\
			.next_to(txt3, DOWN)

		txt5 = MathTex(r"\triangle{AMC}", color = BLACK).next_to(txt4, DOWN).shift(0.3 * DOWN)
		txt6 = MathTex(r"b^2 = (\frac{c}{2})^2 + m^2 - 2\frac{c}{2}m\cos(180 - \alpha)", color = BLACK)\
			.next_to(txt5, DOWN)

		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.play(Write(txt4), run_time = 2)
		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.play(Write(txt6), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt1), FadeOut(txt2), FadeOut(txt3), FadeOut(txt5), run_time = 2)
		self.play(txt4.animate.shift(2.5 * UP), txt6.animate.shift(3.35 * UP), run_time = 2)

		txt6.target = MathTex(r"b^2 = (\frac{c}{2})^2 + m^2 + 2\frac{c}{2}m\cos(\alpha)", color = BLACK)\
			.move_to(txt6.get_center())

		txt7 = MathTex(r"a^2 + b^2 = \tfrac{c^2}{4} + m^2 + \tfrac{c^2}{4} + m^2", color = BLACK)\
			.next_to(txt6, DOWN).shift(0.1 * DOWN)
		
		txt8 = MathTex(r"2m^2 = a^2 + b^2 - \tfrac{c^2}{2}", color = BLACK).next_to(txt7, DOWN).shift(0.1 * DOWN)

		txt9 = MathTex(r"m = \sqrt{\frac{2a^2 + 2b^2 - c^2}{4}}", color = BLACK).next_to(txt8, DOWN)\
			.shift(0.2 * DOWN)
		sur_box = SurroundingRectangle(txt9).set_color(color_gradient([BLUE, YELLOW], 100))\
			.set_stroke(width = 5)

		self.wait(3)
		self.play(ReplacementTransform(txt6, txt6.target), run_time = 2)
		self.wait(2)
		self.play(Write(txt7), run_time = 2)
		self.wait(2)
		self.play(Write(txt8), run_time = 2)
		self.wait(2)
		self.play(Write(txt9), run_time = 2)
		self.play(Create(sur_box), run_time = 2)

		self.wait(2)

	def showa3(self):
		pa = Dot(6.2 * LEFT + 2 * DOWN, radius = 0.06, color = BLACK)
		pb = Dot(1.7 * LEFT, radius = 0.06, color = BLACK)
		pc = Dot(4.7 * LEFT + 3 * UP, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK).next_to(pa, DOWN).shift(0.2 * LEFT + 0.3 * UP)
		pb_t = MathTex("B", color = BLACK).next_to(pb, DOWN).shift(0.2 * UP)
		pc_t = MathTex("C", color = BLACK).next_to(pc, UP).shift(0.2 * DOWN)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lb = Line(pa.get_center(), pc.get_center(), color = BLACK)
		lc = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lines = VGroup(la, lb, lc)
		
		pa_coord_t = MathTex(r"A = (x_1, y_1)", font_size = 40, color = BLACK)
		pb_coord_t = MathTex(r"B = (x_2, y_2)", font_size = 40, color = BLACK)
		pc_coord_t = MathTex(r"C = (x_3, y_3)", font_size = 40, color = BLACK)
		points_coords_t = VGroup(pa_coord_t, pb_coord_t, pc_coord_t).arrange(RIGHT, buff = 0.4)\
			.shift(2.7 * RIGHT + 3 * UP)

		pl = Dot((pa.get_center() + pc.get_center()) / 2, radius = 0.05, color = BLACK)
		pl_t = MathTex(r"L", color = BLACK).next_to(pl, LEFT).shift(0.2 * RIGHT)
		l_bl = Line(pl.get_center(), pb.get_center(), color = BLACK)
		mark1_1 = add_hash_mark(Line(pl.get_center(), pa.get_center(), color = BLACK), 0.13, 1)
		mark1_2 = add_hash_mark(Line(pl.get_center(), pc.get_center(), color = BLACK), 0.13, 1)

		pk = Dot((pa.get_center() + pb.get_center()) / 2, radius = 0.05, color = BLACK)
		pk_t = MathTex(r"K", color = BLACK).next_to(pk, DOWN).shift(0.2 * UP)
		l_ck = Line(pk.get_center(), pc.get_center(), color = BLACK)
		mark2_1 = add_hash_mark(Line(pk.get_center(), pa.get_center(), color = BLACK), 0.13, 2)
		mark2_2 = add_hash_mark(Line(pk.get_center(), pb.get_center(), color = BLACK), 0.13, 2)

		pp = line_intersection(l_bl, l_ck)
		pp_t = MathTex(r"P", color = BLACK).next_to(pp, RIGHT).shift(0.4 * UP + 0.35 * LEFT)

		txt1_1 = MathTex(r"BP:LP = 2:1", font_size = 40, color = BLACK)
		txt1_2 = MathTex(r"CP:KP = 2:1", font_size = 40, color = BLACK)
		txt1_g = VGroup(txt1_1, txt1_2).arrange(RIGHT, buff = 0.9).next_to(points_coords_t, DOWN).shift(0.5 * DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Write(points_coords_t, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(pl), Write(pl_t), Create(l_bl), Create(mark1_1), Create(mark1_2), run_time = 2)
		self.play(Create(pk), Write(pk_t), Create(l_ck), Create(mark2_1), Create(mark2_2), run_time = 2)
		self.wait(2)
		self.play(Create(pp), Write(pp_t), run_time = 2)
		self.wait(2)
		self.play(Write(txt1_g, lag_ratio = 0), run_time = 2)

		txt2 = MathTex(r"L = \tfrac{A + C}{2} = (\tfrac{x_1 + x_3}{2}; \tfrac{y_1 + y_3}{2})", font_size = 40,
				color = BLACK).next_to(points_coords_t, DOWN)
		txt3 = MathTex(r"K = \tfrac{A + B}{2} = (\tfrac{x_1 + x_2}{2}; \tfrac{y_1 + y_2}{2})", font_size = 40,
				color = BLACK).next_to(txt2, DOWN)

		pp_bl = Dot(l_bl.point_from_proportion(0.25), radius = 0.05, color = BLACK)
		pp_bl_t = MathTex(r"P_{BL}", font_size = 25, color = BLACK).next_to(pp_bl, UP).shift(0.2 * DOWN)
		txt4_1 = MathTex(r"BP_{BL}:LP_{BL} = 2:1", font_size = 40, color = BLACK).next_to(txt3, DOWN)\
			.shift(0.2 * DOWN)
		txt4_2 = MathTex(r"P_{BL} = \tfrac{1}{3}B + \tfrac{2}{3}L", font_size = 40, color = BLACK)\
			.next_to(txt4_1, DOWN)
		txt4_3 = MathTex(r"P_{BL} = \tfrac{1}{3}(x_2; y_2) + \tfrac{2}{3}(\tfrac{x_1 + x_3}{2};"
				   r"\tfrac{y_1 + y_3}{2})", font_size = 40, color = BLACK).next_to(txt4_2, DOWN)
		txt4_4 = MathTex(r"P_{BL} = (\tfrac{x_1 + x_2 + x_3}{3}; \tfrac{y_1 + y_2 + y_3}{3})",
						 font_size = 40, color = BLACK).next_to(txt4_3, DOWN)
		sur_box_txt4 = SurroundingRectangle(txt4_4).set_color(GREEN).set_stroke(width = 3)
		txt4_g = VGroup(txt4_4, sur_box_txt4)

		pp_ck = Dot(l_ck.point_from_proportion(0.25), radius = 0.05, color = BLACK)
		pp_ck_t = MathTex(r"P_{CK}", font_size = 25, color = BLACK).next_to(pp_ck, LEFT).shift(0.2 * RIGHT)
		txt5_1 = MathTex(r"CP_{CK}:KP_{CK} = 2:1", font_size = 40, color = BLACK).next_to(txt4_g, DOWN)\
			.shift(2.1 * UP)
		txt5_2 = MathTex(r"P_{CK} = \tfrac{1}{3}C + \tfrac{2}{3}K", font_size = 40, color = BLACK)\
			.next_to(txt5_1, DOWN)
		txt5_3 = MathTex(r"P_{CK} = \tfrac{1}{3}(x_3; y_3) + \tfrac{2}{3}(\tfrac{x_1 + x_2}{2};"
				   r"\tfrac{y_1 + y_2}{2})", font_size = 40, color = BLACK).next_to(txt5_2, DOWN)
		txt5_4 = MathTex(r"P_{CK} = (\tfrac{x_1 + x_2 + x_3}{3}; \tfrac{y_1 + y_2 + y_3}{3})",
				   font_size = 40, color = BLACK).next_to(txt5_3, DOWN)
		sur_box_txt5 = SurroundingRectangle(txt5_4).set_color(GREEN).set_stroke(width = 3)
		txt5_g = VGroup(txt5_4, sur_box_txt5)

		self.wait(2)
		self.play(FadeOut(txt1_g), run_time = 2)
		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.play(Write(txt3), run_time = 2)

		self.wait(2)
		self.play(Create(pp_bl), Write(pp_bl_t), Write(txt4_1), run_time = 2)
		self.wait(2)
		self.play(Write(txt4_2), run_time = 2)
		self.wait(2)
		self.play(Write(txt4_3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4_4), run_time = 2)
		self.wait(2)
		self.play(Create(sur_box_txt4), run_time = 2)
		self.play(FadeOut(txt4_1), FadeOut(txt4_2), FadeOut(txt4_3), run_time = 2)
		self.play(txt4_g.animate.shift(2.1 * UP), run_time = 2)
		self.wait(3)
		self.play(Create(pp_ck), Write(pp_ck_t), Write(txt5_1), run_time = 2)
		self.wait(2)
		self.play(Write(txt5_2), run_time = 2)
		self.wait(2)
		self.play(Write(txt5_3), run_time = 2)
		self.wait(2)
		self.play(Write(txt5_4), run_time = 2)
		self.wait(2)
		self.play(Create(sur_box_txt5), run_time = 2)
		self.play(FadeOut(txt5_1), FadeOut(txt5_2), FadeOut(txt5_3), run_time = 2)
		self.play(txt5_g.animate.shift(2.1 * UP), run_time = 2)

		txt6 = MathTex(r"P_{BL} = (\tfrac{x_1 + x_2 + x_3}{3}; \tfrac{y_1 + y_2 + y_3}{3}) = P_{CK}", 
				 font_size = 40, color = BLACK).next_to(txt5_g, DOWN).shift(0.2 * DOWN)
		txt7 = MathTex(r"P = (\tfrac{x_1 + x_2 + x_3}{3}; \tfrac{y_1 + y_2 + y_3}{3})", font_size = 40,
				color = BLACK).next_to(txt6, DOWN).shift(0.2 * DOWN)

		self.wait(3)
		self.play(Write(txt6), run_time = 2)
		self.play(pp_bl.animate.move_to(pp.get_center()), pp_ck.animate.move_to(pp.get_center()), FadeOut(pp_bl_t),
			FadeOut(pp_ck_t), run_time = 2)
		self.wait(2)
		self.play(Write(txt7), run_time = 2)

		pm = Dot((pb.get_center() + pc.get_center()) / 2, radius = 0.05, color = BLACK)
		pm_t = MathTex(r"M", font_size = 40, color = BLACK).next_to(pm, RIGHT).shift(0.3 * LEFT + 0.2 * UP)
		l_am = Line(pa.get_center(), pm.get_center(), color = BLACK)
		mark3_1 = add_hash_mark(Line(pm.get_center(), pb.get_center(), color = BLACK), 0.13, 3)
		mark3_2 = add_hash_mark(Line(pm.get_center(), pc.get_center(), color = BLACK), 0.13, 3)

		txt8 = MathTex(r"P_{AM} = (\tfrac{x_1 + x_2 + x_3}{3}; \tfrac{y_1 + y_2 + y_3}{3})", 
				 font_size = 40, color = BLACK).next_to(txt5_g, DOWN).shift(0.02 * DOWN)
		sur_box_txt8 = SurroundingRectangle(txt8).set_color(GREEN).set_stroke(width = 3)

		self.wait(2)
		self.play(FadeOut(txt6), run_time = 2)
		self.wait(2)
		self.play(Create(pm), Write(pm_t), Create(l_am), Create(mark3_1, lag_ratio = 0),
			Create(mark3_2, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Write(txt8), run_time = 2)
		self.play(Create(sur_box_txt8), run_time = 2)

		sur_box_p = SurroundingRectangle(txt7).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Create(sur_box_p), run_time = 2)

		self.wait(2)

	def showa4(self):
		pa = Dot(5.8 * LEFT + 2 * DOWN, radius = 0.06, color = BLACK)
		pb = Dot(-0.3 * RIGHT, radius = 0.06, color = BLACK)
		pc = Dot(3.3 * LEFT + 3 * UP, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK).next_to(pa, DOWN).shift(0.2 * LEFT + 0.3 * UP)
		pb_t = MathTex("B", color = BLACK).next_to(pb, DOWN).shift(0.2 * RIGHT + 0.3 * UP)
		pc_t = MathTex("C", color = BLACK).next_to(pc, UP).shift(0.2 * DOWN)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lb = Line(pa.get_center(), pc.get_center(), color = BLACK)
		lc = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lines = VGroup(la, lb, lc)

		la_t = MathTex("a", color = BLACK).next_to(la, RIGHT).shift(1.5 * LEFT)
		lb_t = MathTex("b", color = BLACK).next_to(lb, LEFT).shift(1.3 * RIGHT)
		lc_t = MathTex("c", color = BLACK).next_to(lc, DOWN).shift(1.1 * UP)
		lines_t = VGroup(la_t, lb_t, lc_t)

		pm = Dot((pb.get_center() + pc.get_center()) / 2, radius = 0.05, color = BLACK)
		pm_t = MathTex(r"M", font_size = 40, color = BLACK).next_to(pm, DOWN).shift(0.05 * UP + 0.05 * LEFT)
		l_am = Line(pa.get_center(), pm.get_center(), color = BLACK)
		mark1_1 = add_hash_mark(Line(pm.get_center(), pb.get_center(), color = BLACK), 0.13, 1)
		mark1_2 = add_hash_mark(Line(pm.get_center(), pc.get_center(), color = BLACK), 0.13, 1)

		pl = Dot((pa.get_center() + pc.get_center()) / 2, radius = 0.05, color = BLACK)
		pl_t = MathTex(r"L", color = BLACK).next_to(pl, DOWN).shift(0.2 * UP + 0.1 * RIGHT)
		l_bl = Line(pl.get_center(), pb.get_center(), color = BLACK)
		mark2_1 = add_hash_mark(Line(pl.get_center(), pa.get_center(), color = BLACK), 0.13, 2)
		mark2_2 = add_hash_mark(Line(pl.get_center(), pc.get_center(), color = BLACK), 0.13, 2)

		pk = Dot((pa.get_center() + pb.get_center()) / 2, radius = 0.05, color = BLACK)
		pk_t = MathTex(r"K", color = BLACK).next_to(pk, LEFT).shift(0.2 * RIGHT + 0.2 * UP)
		l_ck = Line(pk.get_center(), pc.get_center(), color = BLACK)
		mark3_1 = add_hash_mark(Line(pk.get_center(), pa.get_center(), color = BLACK), 0.13, 3)
		mark3_2 = add_hash_mark(Line(pk.get_center(), pb.get_center(), color = BLACK), 0.13, 3)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), run_time = 2)
		self.play(Create(lines, lag_ratio = 0), Write(lines_t, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Create(pm), Write(pm_t), Create(l_am), Create(mark1_1, lag_ratio = 0),
		   Create(mark1_2, lag_ratio = 0), run_time = 2)
		self.play(Create(pl), Write(pl_t), Create(l_bl), Create(mark2_1, lag_ratio = 0),
		   Create(mark2_2, lag_ratio = 0), run_time = 2)
		self.play(Create(pk), Write(pk_t), Create(l_ck), Create(mark3_1, lag_ratio = 0),
		   Create(mark3_2, lag_ratio = 0), run_time = 2)

		am_len = MathTex(r"AM = \sqrt{\frac{2b^2 + 2c^2 - a^2}{4}}", color = BLACK).shift(3.5 * RIGHT + 3 * UP)
		bl_len = MathTex(r"BL = \sqrt{\frac{2a^2 + 2c^2 - b^2}{4}}", color = BLACK).next_to(am_len, DOWN)
		ck_len = MathTex(r"CK = \sqrt{\frac{2a^2 + 2b^2 - c^2}{4}}", color = BLACK).next_to(bl_len, DOWN)

		self.wait(2)
		self.play(Write(am_len), run_time = 2)
		self.play(Write(bl_len), run_time = 2)
		self.play(Write(ck_len), run_time = 2)

		pp = Dot((pa.get_center() + pb.get_center() + pc.get_center()) / 3, radius = 0.08, color = BLACK)
		pp_t = MathTex(r"P", color = BLACK).next_to(pp, UP).shift(0.1 * DOWN + 0.2 * RIGHT)

		formula = MathTex(r"P = (\tfrac{x_1 + x_2 + x_3}{3}; \tfrac{y_1 + y_2 + y_3}{3})", color = BLACK)\
			.shift(3.5 * RIGHT + 2 * DOWN)

		self.wait(2)
		self.play(Create(pp), Write(pp_t), run_time = 2)
		self.play(Write(formula), run_time = 2)

		self.wait(3)

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