import math
from manim import *

def get_dist(dot, line):
	p = np.array(dot.get_center())
	a = np.array(line.get_start())
	b = np.array(line.get_end())
	
	ab = b - a
	ap = p - a

	projection = np.dot(ap, ab) / np.dot(ab, ab) * ab

	d = ap - projection

	return np.linalg.norm(d)

def project_point_to_line(dot, line):
    p = np.array(dot.get_center())
    a = np.array(line.get_start())
    b = np.array(line.get_end())

    ab = b - a
    ap = p - a

    projection = np.dot(ap, ab) / np.dot(ab, ab) * ab
    projection_point = a + projection

    return projection_point

def intersection(line1: Line, line2: Line):
	start1, end1 = line1.get_start_and_end()
	start2, end2 = line2.get_start_and_end()

	direction1 = end1 - start1
	direction2 = end2 - start2

	slope1 = direction1[1] / direction1[0] if direction1[0] != 0 else np.inf
	slope2 = direction2[1] / direction2[0] if direction2[0] != 0 else np.inf

	c1 = start1[1] - slope1 * start1[0]
	c2 = start2[1] - slope2 * start2[0]

	if slope1 == slope2:
		return None
	elif slope1 == np.inf:
		x = start1[0]
		y = slope2 * x + c2
	elif slope2 == np.inf:
		x = start2[0]
		y = slope1 * x + c1
	else:
		x = (c2 - c1) / (slope1 - slope2)
		y = slope1 * x + c1

	return np.array([x, y, 0])

def get_bisector(a, b, c):
	ba = b - a
	ca = c - a
	ba_unit = ba / np.linalg.norm(ba)
	ca_unit = ca / np.linalg.norm(ca)
	bisector_dir = ba_unit + ca_unit

	temp_l = a + bisector_dir

	return intersection(Line(a, temp_l), Line(b, c))

def proof2_get_p(a, b, c):
	ap = (a - c) / np.linalg.norm(a - c)
	return a + ap * np.linalg.norm(b - a)

def add_hash_mark(line, offset, n_hashes):
	angle = line.get_angle() + PI * 0.35
	hash_marks = VGroup()
	
	for i in range(n_hashes):
		pos = line.point_from_proportion(0.43 + (i + 1) / (n_hashes + 1) * 0.14)
		mark = Line(pos - offset * rotate_vector(RIGHT, angle), pos + offset * rotate_vector(RIGHT, angle),
					color=line.get_color(), stroke_width = 2)
		hash_marks.add(mark)
	
	return hash_marks

class AngleBisector(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		pa = Dot(5.5 * LEFT + 1 * DOWN, radius = 0.05, color = BLACK)
		pb = Dot(0.5 * RIGHT + 2.5 * UP, radius = 0.05, color = BLACK)
		pc = Dot(2.5 * LEFT + 2 * DOWN, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex(r"A", color = BLACK).next_to(pa, LEFT).shift(0.2 * RIGHT)
		pb_T = MathTex(r"B", color = BLACK).next_to(pb, UP).shift(0.2 * DOWN)
		pc_t = MathTex(r"C", color = BLACK).next_to(pc, DOWN).shift(0.2 * UP)
		points_t = VGroup(pa_t, pb_T, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK)
		lines = VGroup(lab, lbc, lca)

		ang_a = Angle(Line(pa.get_center(), pc.get_center()), Line(pa.get_center(), pb.get_center()),
			   radius = 0.5, color = BLACK)
		ang_b = Angle(Line(pb.get_center(), pa.get_center()), Line(pb.get_center(), pc.get_center()),
				radius = 0.5, color = BLACK)
		ang_c = Angle(Line(pc.get_center(), pb.get_center()), Line(pc.get_center(), pa.get_center()),
				radius = 0.5, color = BLACK)

		pl = Dot(get_bisector(pa.get_center(), pb.get_center(), pc.get_center()), radius = 0.05, color = BLACK)
		pl_t = MathTex(r"L", color = BLACK).next_to(pl, RIGHT).shift(0.1 * DOWN + 0.25 * LEFT)
		lal = Line(pa.get_center(), pl.get_center(), color = BLACK)

		pk = Dot(get_bisector(pb.get_center(), pa.get_center(), pc.get_center()), radius = 0.05, color = BLACK)
		pk_t = MathTex(r"K", color = BLACK).next_to(pk, DOWN).shift(0.2 * UP + 0.05 * LEFT)
		lbk = Line(pb.get_center(), pk.get_center(), color = BLACK)

		pn = Dot(get_bisector(pc.get_center(), pb.get_center(), pa.get_center()), radius = 0.05, color = BLACK)
		pn_t = MathTex(r"N", color = BLACK).next_to(pn, UP).shift(0.2 * DOWN + 0.1 * LEFT)
		lcn = Line(pc.get_center(), pn.get_center(), color = BLACK)

		txt1 = MathTex(r"\angle{A} = \angle{BAC} = \alpha", color = BLACK).shift(3.5 * RIGHT + 2 * UP)		
		txt2 = MathTex(r"\angle{BAL} = \angle{CAL} = \tfrac{\alpha}{2}", color = BLACK).next_to(txt1, DOWN)

		txt3 = MathTex(r"\angle{B} = \angle{ABC} = \beta", color = BLACK).next_to(txt2, DOWN).shift(0.2 * DOWN)
		txt4 = MathTex(r"\angle{ABK} = \angle{CBK} = \tfrac{\beta}{2}", color = BLACK).next_to(txt3, DOWN)

		txt5 = MathTex(r"\angle{C} = \angle{BCA} = \gamma", color = BLACK).next_to(txt4, DOWN).shift(0.2 * DOWN)
		txt6 = MathTex(r"\angle{ACN} = \angle{BCN} = \tfrac{\gamma}{2}", color = BLACK).next_to(txt5, DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Create(lines, lag_ratio = 0), Write(points_t, lag_ratio = 0),
		   run_time = 2)
		self.wait(2)
		self.play(Write(txt1), Create(ang_a), run_time = 2)
		self.wait(2)
		self.play(Create(pl), Create(lal), Write(pl_t), run_time = 2)
		self.play(Write(txt2))

		self.wait(2)
		self.play(Create(ang_b), Create(ang_c), Write(txt3), Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Create(pk), Create(lbk), Write(pk_t), Create(pn), Create(lcn), Write(pn_t), run_time = 2)
		self.play(Write(txt4), Write(txt6), run_time = 2)

		self.wait(2)

	def showa2(self):
		pa = Dot(5.5 * LEFT + 0.0 * DOWN, radius = 0.05, color = BLACK)
		pb = Dot(0.0 * RIGHT + 2.5 * UP, radius = 0.05, color = BLACK)
		pc = Dot(2.5 * LEFT + 2 * DOWN, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex(r"A", color = BLACK, font_size = 40).next_to(pa, LEFT).shift(0.2 * RIGHT)
		pb_T = MathTex(r"B", color = BLACK, font_size = 40).next_to(pb, UP).shift(0.2 * DOWN)
		pc_t = MathTex(r"C", color = BLACK, font_size = 40).next_to(pc, DOWN).shift(0.2 * UP)
		points_t = VGroup(pa_t, pb_T, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK, stroke_width = 2)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK, stroke_width = 2)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK, stroke_width = 2)
		lines = VGroup(lab, lbc, lca)

		pl = Dot(get_bisector(pa.get_center(), pb.get_center(), pc.get_center()), radius = 0.05, color = BLACK)
		pl_t = MathTex(r"L", color = BLACK).next_to(pl, RIGHT).shift(0.1 * DOWN + 0.25 * LEFT)
		lal = Line(pa.get_center(), pl.get_center(), color = BLACK)

		pk = Dot(get_bisector(pb.get_center(), pa.get_center(), pc.get_center()), radius = 0.05, color = BLACK)
		pk_t = MathTex(r"K", color = BLACK).next_to(pk, DOWN).shift(0.2 * UP + 0.05 * LEFT)
		lbk = Line(pb.get_center(), pk.get_center(), color = BLACK)

		pp = Dot(get_bisector(pc.get_center(), pb.get_center(), pa.get_center()), radius = 0.05, color = BLACK)
		pp_t = MathTex(r"P", color = BLACK).next_to(pp, UP).shift(0.2 * DOWN + 0.1 * LEFT)
		lcp = Line(pc.get_center(), pp.get_center(), color = BLACK)

		po = Dot(intersection(lbk, lcp), radius = 0.05, color = BLACK)
		po_t = MathTex(r"O", color = BLACK, font_size = 40).next_to(po, DOWN).shift(0.1 * LEFT)
		r_val = get_dist(po, lbc)
		circ = Circle(radius = r_val, color = BLACK, stroke_width = 2).move_to(po.get_center())

		pm = Dot(project_point_to_line(po, lab), radius = 0.05, color = BLACK)
		pm_t = MathTex(r"M", color = BLACK, font_size = 40).next_to(pm, UP).shift(0.2 * DOWN)

		pn = Dot(project_point_to_line(po, lca), radius = 0.05, color = BLACK)
		pn_t = MathTex(r"N", color = BLACK, font_size = 40).next_to(pn, DOWN).shift(0.18 * UP + 0.1 * LEFT)

		lom = Line(po.get_center(), pm.get_center(), color = BLACK)
		lon = Line(po.get_center(), pn.get_center(), color = BLACK)
		loa = Line(po.get_center(), pa.get_center(), color = BLACK)

		txt1 = MathTex(r"\triangle{AOM} \; \; \; \triangle{AON}", font_size = 50, color = BLACK)\
			.shift(3.5 * RIGHT + 2.5 * UP)
		
		ra1 = RightAngle(Line(pm.get_center(), po.get_center()), Line(pm.get_center(), pa.get_center()),
				   length = 0.2, color = BLACK)
		ra2 = RightAngle(Line(pn.get_center(), po.get_center()), Line(pn.get_center(), pa.get_center()),
				   length = 0.2, color = BLACK)

		txt2_1 = MathTex(r"AM^2 = OA^2 - OM^2", font_size = 40, color = BLACK)
		txt2_2 = MathTex(r"= OA^2 - ON^2", font_size = 40, color = BLACK)
		txt2_g = VGroup(txt2_1, txt2_2).arrange(RIGHT).next_to(txt1, DOWN).shift(0.2 * DOWN)

		txt3_1 = MathTex(r"AN^2 = OA^2 - ON^2", font_size = 40, color = BLACK)
		txt3_2 = MathTex(r"= OA^2 - OM^2", font_size = 40, color = BLACK)
		txt3_g = VGroup(txt3_1, txt3_2).arrange(RIGHT).next_to(txt2_g, DOWN)

		txt4 = MathTex(r"\triangle{AOM} \triangleq \triangle{AON}", font_size = 50, color = BLACK)\
			.next_to(txt3_g, DOWN).shift(0.2 * DOWN)

		txt5 = MathTex(r"\angle{OAM} = \angle{OAN}", font_size = 50, color = BLACK).next_to(txt4, DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Create(lines, lag_ratio = 0), Write(points_t, lag_ratio = 0),
		   run_time = 2)
		self.wait(2)
		self.play(Create(po), Write(po_t), Create(circ), run_time = 2)
		self.wait(2)
		self.play(Create(pm), Create(pn), Write(pm_t), Write(pn_t), run_time = 2)
		
		self.wait(2)
		self.play(Create(lom), Create(lon), Create(loa), run_time = 2)
		self.wait(2)
		self.play(Write(txt1), run_time = 2)
		self.wait(2)
		self.play(Create(ra1), Create(ra2), run_time = 2)
		self.wait(2)
		self.play(Write(txt2_1), Write(txt3_1), run_time = 2)
		self.wait(2)
		self.play(Write(txt2_2), Write(txt3_2), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.wait(2)
		self.play(Write(txt5), run_time = 2)

		self.wait(3)
		self.play(FadeOut(txt4), FadeOut(txt3_1), FadeOut(txt3_2), FadeOut(txt2_1), FadeOut(txt2_2), FadeOut(txt1),
		   FadeOut(lom), FadeOut(lon), FadeOut(ra1), FadeOut(ra2), FadeOut(pn), FadeOut(pm), FadeOut(txt5),
		   FadeOut(pn_t), FadeOut(pm_t), run_time = 2)

		lob = Line(po.get_center(), pb.get_center(), color = BLACK)
		loc = Line(po.get_center(), pc.get_center(), color = BLACK)

		txt6 = MathTex(r"\angle{OAB} = \angle{OAC}", font_size = 50, color = BLACK).shift(3.5 * RIGHT + 2 * UP)
		txt7 = MathTex(r"\angle{OBA} = \angle{OBC}", font_size = 50, color = BLACK).next_to(txt6, DOWN)
		txt8 = MathTex(r"\angle{OCA} = \angle{OCB}", font_size = 50, color = BLACK).next_to(txt7, DOWN)

		self.wait(2)
		self.play(Create(lob), Create(loc), run_time = 2)
		self.play(Write(txt6), Write(txt7), Write(txt8), run_time = 2)

		self.wait(2)

	def showa3(self):
		pa = Dot(4.5 * LEFT + 0.5 * UP, radius = 0.05, color = BLACK)
		pb = Dot(1.5 * LEFT + 2.5 * DOWN, radius = 0.05, color = BLACK)
		pc = Dot(6.5 * LEFT + 1.0 * DOWN, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex(r"A", color = BLACK, font_size = 40).next_to(pa, LEFT).shift(0.2 * RIGHT + 0.15 * UP)
		pb_t = MathTex(r"B", color = BLACK, font_size = 40).next_to(pb, DOWN).shift(0.2 * UP)
		pc_t = MathTex(r"C", color = BLACK, font_size = 40).next_to(pc, DOWN).shift(0.2 * UP)
		points_t = VGroup(pa_t, pb_t, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK)
		lines = VGroup(lab, lbc, lca)

		pl = Dot(get_bisector(pa.get_center(), pb.get_center(), pc.get_center()), radius = 0.05, color = BLACK)
		pl_t = MathTex(r"L", color = BLACK).next_to(pl, DOWN).shift(0.2 * UP)
		lal = Line(pa.get_center(), pl.get_center(), color = BLACK)

		ang_a1 = Angle(Line(pa.get_center(), pc.get_center()), Line(pa.get_center(), pl.get_center()), radius = 0.3,
				 color = BLACK)
		ang_a1_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_a1, DOWN)\
			.shift(0.15 * UP + 0.13 * LEFT)

		ang_a2 = Angle(Line(pa.get_center(), pl.get_center()), Line(pa.get_center(), pb.get_center()), radius = 0.3,
				 color = BLACK)
		ang_a2_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_a2, DOWN)\
			.shift(0.15 * UP + 0.1 * RIGHT)

		pp = Dot(proof2_get_p(pa.get_center(), pb.get_center(), pc.get_center()), radius = 0.05, color = BLACK)
		pp_t = MathTex(r"P", color = BLACK).next_to(pp, LEFT).shift(0.1 * UP + 0.25 * RIGHT)

		lap = Line(pa.get_center(), pp.get_center(), color = BLACK)
		lpb = Line(pb.get_center(), pp.get_center(), color = BLACK)

		ang_abp = Angle(Line(pb.get_center(), pp.get_center()), Line(pb.get_center(), pa.get_center()), radius = 0.3,
				  color = BLACK)
		ang_abp_t = MathTex(r"\beta", color = BLACK, font_size = 35).next_to(ang_abp, UP)\
			.shift(0.2 * DOWN + 0.03 * LEFT)
		ang_abp_t.target = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_abp, UP)\
			.shift(0.2 * DOWN + 0.03 * LEFT)

		ang_apb = Angle(Line(pp.get_center(), pa.get_center()), Line(pp.get_center(), pb.get_center()), radius = 0.3,
				  color = BLACK)
		ang_apb_t = MathTex(r"\beta", color = BLACK, font_size = 35).next_to(ang_apb, DOWN)\
			.shift(0.2 * UP + 0.1 * LEFT)
		ang_apb_t.target = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang_apb, DOWN)\
			.shift(0.2 * UP + 0.1 * LEFT)

		mark1 = add_hash_mark(Line(pa.get_center(), pb.get_center(), color = BLACK), 0.1, 1)
		mark2 = add_hash_mark(Line(pa.get_center(), pp.get_center(), color = BLACK), 0.1, 1)

		txt1 = MathTex(r"\angle{CAL} = \angle{BAL} = \alpha", font_size = 50, color = BLACK)\
			.shift(3.5 * RIGHT + 2.5 * UP)
		txt2 = MathTex(r"\frac{AC}{CL} = \frac{AB}{BL}", font_size = 50, color = BLACK).shift(3.5 * RIGHT + 0.5 * UP)
		txt3 = MathTex(r"\angle{ABP} = \angle{APB} = \beta", font_size = 50, color = BLACK).next_to(txt1, DOWN)
		txt3.target = MathTex(r"\angle{ABP} = \angle{APB} = \alpha", font_size = 50, color = BLACK)\
			.next_to(txt1, DOWN)
		txt4 = MathTex(r"2 \cdot \alpha = 2 \cdot \beta", font_size = 50, color = BLACK).next_to(txt3, DOWN)
		txt4.target = MathTex(r"\alpha = \beta", font_size = 50, color = BLACK).next_to(txt3, DOWN)

		txt5 = MathTex(r"AL \| PB", font_size = 50, color = BLACK).next_to(txt3, DOWN).shift(0.3 * DOWN)

		txt6 = MathTex(r"\frac{AC}{CL} = \frac{AP}{BL}", font_size = 50, color = BLACK).next_to(txt5, DOWN)

		txt7 = MathTex(r"\frac{AC}{CL} = \frac{AB}{BL}", font_size = 50, color = BLACK).next_to(txt6, DOWN)\
			.shift(0.2 * DOWN)

		sur_box_p = SurroundingRectangle(txt7).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), Create(lines, lag_ratio = 0),
			run_time = 2)
		self.play(Create(pl), Write(pl_t), Create(lal), run_time = 2)
		self.wait(2)
		self.play(Write(txt1), Create(ang_a1), Write(ang_a1_t), Create(ang_a2), Write(ang_a2_t), run_time = 2)

		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.wait(3)
		self.play(FadeOut(txt2), run_time = 2)

		self.wait(2)
		self.play(Create(pp), Create(lap), Write(pp_t), run_time = 2)
		self.play(Create(mark1), Create(mark2), run_time = 2)
		
		self.wait(2)
		self.play(Create(lpb), Create(ang_abp), Create(ang_apb), Write(ang_abp_t), Write(ang_apb_t), run_time = 2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4), run_time = 2)
		self.wait(2)
		self.play(Transform(txt4, txt4.target), Transform(txt3, txt3.target), run_time = 2)
		self.wait(2)
		self.play(Transform(ang_abp_t, ang_abp_t.target), Transform(ang_apb_t, ang_apb_t.target), run_time = 2)
		self.wait(2)
		self.play(FadeOut(txt4), run_time = 2)

		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Write(txt6), run_time = 2)
		self.wait(2)
		self.play(Write(txt7), run_time = 2)
		self.play(Create(sur_box_p), run_time = 2)

		self.wait(2)

	def showa4(self):
		pa = Dot(3 * LEFT + 0.5 * UP, radius = 0.05, color = BLACK)
		pb = Dot(6.5 * LEFT + 2.5 * DOWN, radius = 0.05, color = BLACK)
		pc = Dot(5 * LEFT + 3.0 * UP, radius = 0.05, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex(r"A", color = BLACK, font_size = 40).next_to(pa, DOWN).shift(0.2 * UP)
		pb_t = MathTex(r"B", color = BLACK, font_size = 40).next_to(pb, DOWN).shift(0.2 * UP)
		pc_t = MathTex(r"C", color = BLACK, font_size = 40).next_to(pc, UP).shift(0.2 * DOWN)
		points_t = VGroup(pa_t, pb_t, pc_t)

		lab = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lbc = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lca = Line(pc.get_center(), pa.get_center(), color = BLACK)
		lines = VGroup(lab, lbc, lca)

		lab_t = MathTex(r"c", color = BLACK, font_size = 40).next_to(lab, DOWN).shift(1.6 * UP)
		lbc_t = MathTex(r"a", color = BLACK, font_size = 40).next_to(lbc, LEFT).shift(0.9 * RIGHT)
		lca_t = MathTex(r"b", color = BLACK, font_size = 40).next_to(lca, RIGHT).shift(1.05 * LEFT)
		lines_t = VGroup(lab_t, lbc_t, lca_t)

		pl = Dot(get_bisector(pc.get_center(), pa.get_center(), pb.get_center()), radius = 0.05, color = BLACK)
		pl_t = MathTex(r"L", color = BLACK, font_size = 40).next_to(pl, DOWN).shift(0.2 * UP)
		lcl = Line(pc.get_center(), pl.get_center(), color = BLACK)
		lcl_t = MathTex(r"l", color = BLACK, font_size = 40).next_to(lcl, RIGHT).shift(0.5 * LEFT)

		ang1 = Angle(Line(pc.get_center(), pb.get_center()), Line(pc.get_center(), pl.get_center()),
			  radius = 0.5, color = BLACK)
		ang1_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang1, DOWN).shift(0.15 * UP)
		ang2 = Angle(Line(pc.get_center(), pl.get_center()), Line(pc.get_center(), pa.get_center()),
			  radius = 0.5, color = BLACK)
		ang2_t = MathTex(r"\alpha", color = BLACK, font_size = 35).next_to(ang2, DOWN).shift(0.2 * UP + 0.1 * RIGHT)

		lbl_t = MathTex(r"m", color = BLACK, font_size = 40).next_to(Line(pb.get_center(), pl.get_center()), UP)\
			.shift(1.0 * DOWN)
		lal_t = MathTex(r"n", color = BLACK, font_size = 40).next_to(Line(pa.get_center(), pl.get_center()), UP)\
			.shift(0.55 * DOWN)

		txt1 = MathTex(r"BL = m \;\;\; AL = n = c - m", font_size = 40, color = BLACK).shift(3.3 * UP + 2 * RIGHT)

		txt2 = MathTex(r"\frac{a}{m} = \frac{b}{n}", font_size = 40, color = BLACK).next_to(txt1, DOWN)
		txt2.target = MathTex(r"\frac{a}{m} = \frac{b}{c - m}", font_size = 40, color = BLACK).next_to(txt1, DOWN)

		txt3 = MathTex(r"ac - am = bm", font_size = 40, color = BLACK).next_to(txt2, DOWN)

		txt4_1 = MathTex(r"m = \frac{a c}{a + b}", font_size = 40, color = BLACK)
		txt4_2 = MathTex(r"n = \frac{b c}{a + b}", font_size = 40, color = BLACK)
		txt4_g = VGroup(txt4_1, txt4_2).arrange(RIGHT, buff = 1.0).next_to(txt3, DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), Create(lines, lag_ratio = 0),
		   Write(lines_t, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(pl), Create(lcl), Write(pl_t), Write(lcl_t), Create(ang1), Write(ang1_t), Create(ang2),
		   Write(ang2_t), run_time = 2)

		self.wait(2)
		self.play(Write(lbl_t), Write(lal_t), Write(txt1), run_time = 2)

		self.wait(2)
		self.play(Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Transform(txt2, txt2.target), run_time = 2)
		self.wait(2)
		self.play(Write(txt3), run_time = 2)
		self.wait(2)
		self.play(Write(txt4_1), run_time = 2)
		self.play(Write(txt4_2), run_time = 2)

		self.wait(3)
		self.play(FadeOut(txt2), FadeOut(txt3), run_time = 2)
		self.play(txt4_g.animate.shift(1.5 * UP), run_time = 2)

		txt5 = MathTex(r"(\frac{a c}{a + b})^2 = a^2 + l^2 - 2al\cos(\alpha)", font_size = 35, color = BLACK)\
			.next_to(txt4_g, DOWN).shift(0.2 * DOWN)
		txt6 = MathTex(r"(\frac{b c}{a + b})^2 = b^2 + l^2 - 2bl\cos(\alpha)", font_size = 35, color = BLACK)\
			.next_to(txt5, DOWN)

		self.wait(2)
		self.play(Write(txt5), run_time = 2)
		self.wait(2)
		self.play(Write(txt6), run_time = 2)

		txt7 = MathTex(r"\frac{\frac{a^2c^2}{(a+b)^2} - a^2 - l^2}{\frac{b^2c^2}{(a+b)^2} - b^2 - l^2} =" 
				 r"\frac{-2al\cos(\alpha)}{-2bl\cos(\alpha)}", font_size = 35, color = BLACK).next_to(txt6, DOWN)

		self.wait(2)
		self.play(Write(txt7), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt5), FadeOut(txt6), run_time = 2)
		self.play(txt7.animate.shift(2 * UP), run_time = 2)

		txt8 = MathTex(r"\frac{\frac{a^2c^2}{(a+b)^2} - a^2 - l^2}{\frac{b^2c^2}{(a+b)^2} - b^2 - l^2} =" 
				 r"\frac{a}{b}", font_size = 35, color = BLACK).next_to(txt7, DOWN)
		txt9 = MathTex(r"(\frac{a^2c^2}{(a+b)^2} - a^2)b - bl^2 = (\frac{b^2c^2}{(a+b)^2} - b^2)a - al^2",
				 font_size = 35, color = BLACK).next_to(txt8, DOWN)
		txt10 = MathTex(r"(\frac{a^2c^2}{(a+b)^2} - a^2)b - (\frac{b^2c^2}{(a+b)^2} - b^2)a = l^2(b - a)",
				 font_size = 35, color = BLACK).next_to(txt9, DOWN)

		self.wait(2)
		self.play(Write(txt8), run_time = 2)
		self.wait(2)
		self.play(Write(txt9), run_time = 2)
		self.wait(2)
		self.play(Write(txt10), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt7), FadeOut(txt8), FadeOut(txt9), run_time = 2)
		self.play(txt10.animate.shift(4.1 * UP), run_time = 2)

		txt11 = MathTex(r"\frac{abc^2(b-a)}{(a+b)^2} + ab(b-a) = l^2(b-a)", font_size = 35, color = BLACK)\
			.next_to(txt10, DOWN)
		txt12 = MathTex(r"l^2 = \frac{abc^2}{(a+b)^2} + ab", font_size = 45, color = BLACK).next_to(txt11, DOWN)
		
		self.wait(2)
		self.play(Write(txt11), run_time = 2)
		self.wait(2)
		self.play(Write(txt12), run_time = 2)

		self.wait(2)
		self.play(FadeOut(txt10), FadeOut(txt11), run_time = 2)
		self.play(txt12.animate.shift(2.5 * UP), run_time = 2)
		
		txt13 = MathTex(r"l = \sqrt{\frac{abc^2}{(a+b)^2} + ab}", font_size = 45, color = BLACK)\
			.next_to(txt12, DOWN).shift(0.15 * DOWN)
		txt14 = MathTex(r"l = \sqrt{\frac{ac}{a+b} \cdot \frac{bc}{a+b} + ab} = \sqrt{mn + ab}", font_size = 45,
				 color = BLACK).next_to(txt13, DOWN).shift(0.15 * DOWN)

		sur_box_p1 = SurroundingRectangle(txt13).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)
		sur_box_p2 = SurroundingRectangle(txt14).set_color(color_gradient([BLUE, YELLOW], 100)).set_stroke(width = 5)

		self.wait(2)
		self.play(Write(txt13), run_time = 2)
		self.play(Create(sur_box_p1), run_time = 2)
		self.wait(2)
		self.play(Write(txt14), run_time = 2)
		self.play(Create(sur_box_p2), run_time = 2)

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