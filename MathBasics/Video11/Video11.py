from manim import *
import math

def intersection(line1: Line, line2: Line) -> np.ndarray:
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

def line_intersection(line1, line2) -> Dot:
	xdiff = (line1.get_start()[0] - line1.get_end()[0], line2.get_start()[0] - line2.get_end()[0])
	ydiff = (line1.get_start()[1] - line1.get_end()[1], line2.get_start()[1] - line2.get_end()[1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)

	d = (det(*line1.get_start_and_end()), det(*line2.get_start_and_end()))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return Dot(x * RIGHT + y * UP, color = BLACK, radius = 0.075)

def find_foot_of_perpendicular(line: Line, point: Dot):
	start, end = line.get_start_and_end()
	direction_line = end - start
	slope_line = direction_line[1]/direction_line[0] if direction_line[0] != 0 else np.inf
	slope_perpendicular = -1/slope_line if slope_line != 0 else np.inf

	start_perpendicular = point.get_center()

	if slope_perpendicular != np.inf:
		end_perpendicular = start_perpendicular + np.array([1, slope_perpendicular, 0])
	else:
		end_perpendicular = start_perpendicular + np.array([0, 1, 0])
	
	perpendicular_line = Line(start_perpendicular, end_perpendicular)

	intersection_point = intersection(line, perpendicular_line)

	return Dot(RIGHT * intersection_point[0] + UP * intersection_point[1], radius = 0.06, color = BLACK)

def add_hash_mark(line, offset, n_hashes):
	angle = line.get_angle() + PI * 0.35
	hash_marks = VGroup()
	
	for i in range(n_hashes):
		pos = line.point_from_proportion(0.45 + (i+1)/(n_hashes+1) * 0.1)
		mark = Line(pos - offset * rotate_vector(RIGHT, angle), pos + offset * rotate_vector(RIGHT, angle),
					color=line.get_color(), stroke_width = 2)
		hash_marks.add(mark)
	
	return hash_marks

def find_circumcircle(coords):
	x1, y1 = coords[0]
	x2, y2 = coords[1]
	x3, y3 = coords[2]

	D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

	Ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / D
	Uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / D

	radius = math.sqrt((x1 - Ux)**2 + (y1 - Uy)**2)
	
	return (Ux, Uy), radius


class TriangAltitude(Scene):
	def clearEverything(self):
		self.play(*[FadeOut(mob) for mob in self.mobjects])

	def showa1(self):
		pa = Dot(4.5 * LEFT + 2 * DOWN, radius = 0.06, color = BLACK)
		pb = Dot(1.0 * RIGHT, radius = 0.06, color = BLACK)
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

		hap = find_foot_of_perpendicular(la, pa)
		hap_t = MathTex("H", color = BLACK).next_to(hap, RIGHT).shift(0.2 * LEFT + 0.2 * UP)
		hap_l = Line(pa.get_center(), hap.get_center(), color = BLACK)
		ha_ra = RightAngle(Line(hap.get_center(), pa.get_center()), Line(hap.get_center(), pb.get_center()), 
					 length = 0.3, color = BLACK)

		hbp = find_foot_of_perpendicular(lb, pb)
		hbp_t = MathTex("G", color = BLACK).next_to(hbp, LEFT).shift(0.15 * UP + 0.15 * RIGHT)
		hbp_l = Line(pb.get_center(), hbp.get_center(), color = BLACK)
		hb_ra = RightAngle(Line(hbp.get_center(), pb.get_center()), Line(hbp.get_center(), pc.get_center()), 
					 length = 0.3, color = BLACK)

		hcp = find_foot_of_perpendicular(lc, pc)
		hcp_t = MathTex("V", color = BLACK).next_to(hcp, DOWN).shift(0.15 * UP)
		hcp_l = Line(pc.get_center(), hcp.get_center(), color = BLACK)
		hc_ra = RightAngle(Line(hcp.get_center(), pc.get_center()), Line(hcp.get_center(), pa.get_center()), 
					 length = 0.3, color = BLACK)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), Create(lines, lag_ratio = 0),
			run_time = 2)
		self.wait(2)
		self.play(Create(hap), Write(hap_t), Create(hap_l), Create(ha_ra), run_time = 2)
		self.wait(2)
		self.play(Create(hbp), Write(hbp_t), Create(hbp_l), Create(hb_ra), run_time = 2)
		self.play(Create(hcp), Write(hcp_t), Create(hcp_l), Create(hc_ra), run_time = 2)

		self.wait(2)

	def showa2(self):
		pa = Dot(-4 * RIGHT + 0 * UP, radius = 0.06, color = BLACK).set_z_index(1)
		pb = Dot(-1 * RIGHT + 2 * UP, radius = 0.06, color = BLACK).set_z_index(1)
		pc = Dot(0 * RIGHT + -1 * UP, radius = 0.06, color = BLACK).set_z_index(1)
		points1 = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK, font_size = 40).next_to(pa, DOWN).shift(0.2 * LEFT + 0.35 * UP)
		pb_t = MathTex("B", color = BLACK, font_size = 40).next_to(pb, UP).shift(0.2 * DOWN)
		pc_t = MathTex("C", color = BLACK, font_size = 40).next_to(pc, DOWN).shift(0.2 * UP)
		points1_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = RED)
		lb = Line(pa.get_center(), pc.get_center(), color = GREEN)
		lc = Line(pa.get_center(), pb.get_center(), color = BLUE)
		lines1 = VGroup(la, lb, lc)

		anga = Angle(Line(pa.get_center(), pc.get_center()), Line(pa.get_center(), pb.get_center()),
			  radius = 0.37, color = '#FDFD4B')
		angb = Angle(Line(pb.get_center(), pa.get_center()), Line(pb.get_center(), pc.get_center()),
			   radius = 0.45, color = '#55F7A6')
		angc = Angle(Line(pc.get_center(), pb.get_center()), Line(pc.get_center(), pa.get_center()),
			   radius = 0.53, color = '#F7A6F7')
		angles1 = VGroup(anga, angb, angc)

		pf = Dot(pa.get_center() + pb.get_center() - pc.get_center(), radius = 0.06, color = BLACK)
		pd = Dot(pb.get_center() + pc.get_center() - pa.get_center(), radius = 0.06, color = BLACK)
		pe = Dot(pc.get_center() + pa.get_center() - pb.get_center(), radius = 0.06, color = BLACK)
		points2 = VGroup(pf, pd, pe)

		pf_t = MathTex("F", color = BLACK, font_size = 40).next_to(pf, LEFT).shift(0.2 * RIGHT)
		pd_t = MathTex("D", color = BLACK, font_size = 40).next_to(pd, UP).shift(0.2 * DOWN)
		pe_t = MathTex("E", color = BLACK, font_size = 40).next_to(pe, LEFT).shift(0.2 * RIGHT)
		points2_t = VGroup(pf_t, pd_t, pe_t)

		la1 = Line(pf.get_center(), pe.get_center(), color = RED)
		lb1 = Line(pd.get_center(), pf.get_center(), color = GREEN)
		lc1 = Line(pe.get_center(), pd.get_center(), color = BLUE)
		lines2 = VGroup(la1, lb1, lc1)

		anga_2 = Angle(Line(pb.get_center(), pf.get_center()), Line(pb.get_center(), pa.get_center()),
				 radius = 0.37, color = '#FDFD4B')
		anga_3 = Angle(Line(pc.get_center(), pa.get_center()), Line(pc.get_center(), pe.get_center()),
				 radius = 0.37, color = '#FDFD4B')
		angb_2 = Angle(Line(pa.get_center(), pb.get_center()), Line(pa.get_center(), pf.get_center()),
				 radius = 0.45, color = '#55F7A6')
		angb_3 = Angle(Line(pc.get_center(), pd.get_center()), Line(pc.get_center(), pb.get_center()),
				 radius = 0.45, color = '#55F7A6')
		angc_2 = Angle(Line(pa.get_center(), pe.get_center()), Line(pa.get_center(), pc.get_center()),
				 radius = 0.53, color = '#F7A6F7')
		angc_3 = Angle(Line(pb.get_center(), pc.get_center()), Line(pb.get_center(), pd.get_center()),
				 radius = 0.53, color = '#F7A6F7')
		angles2 = VGroup(anga_2, anga_3, angb_2, angb_3, angc_2, angc_3)

		text1_1 = MathTex("AB \| ED", color = BLACK, font_size = 40).shift(4.5 * RIGHT + 3 * UP)
		text1_2 = MathTex("BC \| FE", color = BLACK, font_size = 40).next_to(text1_1, DOWN)
		text1_3 = MathTex("AC \| FD", color = BLACK, font_size = 40).next_to(text1_2, DOWN)
		text1_g = VGroup(text1_1, text1_2, text1_3)

		text2_1 = MathTex(r"\triangle{ABC} \triangleq \triangle{BAF}", color = BLACK, font_size = 40)\
			.next_to(text1_g, DOWN).shift(1.5 * DOWN)
		text2_2 = MathTex(r"\triangle{ABC} \triangleq \triangle{DCB}", color = BLACK, font_size = 40)\
			.next_to(text2_1, DOWN)
		text2_3 = MathTex(r"\triangle{ABC} \triangleq \triangle{CEA}", color = BLACK, font_size = 40)\
			.next_to(text2_2, DOWN)
		text2_g = VGroup(text2_1, text2_2, text2_3)

		mark1_1 = add_hash_mark(Line(pa.get_center(), pb.get_center(), color = BLACK), 0.12, 1)
		mark1_2 = add_hash_mark(Line(pe.get_center(), pc.get_center(), color = BLACK), 0.12, 1)
		mark1_3 = add_hash_mark(Line(pc.get_center(), pd.get_center(), color = BLACK), 0.12, 1)
		mark1_g = VGroup(mark1_1, mark1_2, mark1_3)

		mark2_1 = add_hash_mark(Line(pb.get_center(), pc.get_center(), color = BLACK), 0.12, 2)
		mark2_2 = add_hash_mark(Line(pf.get_center(), pa.get_center(), color = BLACK), 0.12, 2)
		mark2_3 = add_hash_mark(Line(pa.get_center(), pe.get_center(), color = BLACK), 0.12, 2)
		mark2_g = VGroup(mark2_1, mark2_2, mark2_3)

		mark3_1 = add_hash_mark(Line(pa.get_center(), pc.get_center(), color = BLACK), 0.12, 3)
		mark3_2 = add_hash_mark(Line(pf.get_center(), pb.get_center(), color = BLACK), 0.12, 3)
		mark3_3 = add_hash_mark(Line(pb.get_center(), pd.get_center(), color = BLACK), 0.12, 3)
		mark3_g = VGroup(mark3_1, mark3_2, mark3_3)

		self.wait(2)
		self.play(Create(points1, lag_ratio = 0), Write(points1_t, lag_ratio = 0), Create(lines1, lag_ratio = 0),
			run_time = 2)
		self.wait(2)
		self.play(Create(angles1, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Create(lines2, lag_ratio = 0), run_time = 2)
		self.play(Create(points2, lag_ratio = 0), Write(points2_t, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Write(text1_g, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(angles2, lag_ratio = 0), run_time = 2)

		self.wait(2)
		self.play(Write(text2_g, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(mark1_g, lag_ratio = 0), run_time = 2)
		self.play(Create(mark2_g, lag_ratio = 0), run_time = 2)
		self.play(Create(mark3_g, lag_ratio = 0), run_time = 2)

		hap = find_foot_of_perpendicular(la, pa)
		hap_t = MathTex("H", color = BLACK, font_size = 40).next_to(hap, RIGHT).shift(0.2 * LEFT)
		hap_l = Line(pa.get_center(), hap.get_center(), color = BLACK)
		ha_ra = RightAngle(Line(hap.get_center(), pa.get_center()), Line(hap.get_center(), pc.get_center()), 
					 length = 0.25, color = BLACK)
		ha_ra2 = RightAngle(Line(pa.get_center(), pe.get_center()), Line(pa.get_center(), hap.get_center()),
					  length = 0.25, color = BLACK)

		hbp = find_foot_of_perpendicular(lb, pb)
		hbp_t = MathTex("G", color = BLACK, font_size = 40).next_to(hbp, DOWN).shift(0.2 * UP)
		hbp_l = Line(pb.get_center(), hbp.get_center(), color = BLACK)
		hb_ra = RightAngle(Line(hbp.get_center(), pb.get_center()), Line(hbp.get_center(), pa.get_center()), 
					 length = 0.25, color = BLACK)
		hb_ra2 = RightAngle(Line(pb.get_center(), pf.get_center()), Line(pb.get_center(), hbp.get_center()),
					  length = 0.25, color = BLACK)

		hcp = find_foot_of_perpendicular(lc, pc)
		hcp_t = MathTex("V", color = BLACK, font_size = 40).next_to(hcp, LEFT).shift(0.25 * RIGHT + 0.15 * UP)
		hcp_l = Line(pc.get_center(), hcp.get_center(), color = BLACK)
		hc_ra = RightAngle(Line(hcp.get_center(), pc.get_center()), Line(hcp.get_center(), pb.get_center()), 
					 length = 0.25, color = BLACK)
		hc_ra2 = RightAngle(Line(pc.get_center(), pd.get_center()), Line(pc.get_center(), hcp.get_center()),
					  length = 0.25, color = BLACK)

		pp = line_intersection(hap_l, hbp_l)
		pp_t = MathTex("P", color = BLACK, font_size = 40).next_to(pp, DOWN).shift(0.25 * LEFT + 0.15 * UP)

		self.wait(3)
		self.play(FadeOut(angles2, lag_ratio = 0), FadeOut(angles1, lag_ratio = 0), run_time = 2)
		self.wait(2)
		self.play(Create(hap), Write(hap_t), Create(hap_l), Create(ha_ra), run_time = 2)
		self.wait(2)
		self.play(Create(ha_ra2), run_time = 2)
		self.wait(2)
		self.play(Create(hbp), Write(hbp_t), Create(hbp_l), Create(hb_ra), run_time = 2)
		self.wait(2)
		self.play(Create(hb_ra2), run_time = 2)
		self.wait(2)
		self.play(Create(hcp), Write(hcp_t), Create(hcp_l), Create(hc_ra), run_time = 2)
		self.wait(2)
		self.play(Create(hc_ra2), run_time = 2)

		self.wait(2)
		self.play(Create(pp), Write(pp_t), run_time = 2)

		self.wait(2)

	def showa3(self):
		coords = [[-2.5, 2.5], [-4, -0.5], [2, -0.5]]

		pa = Dot(coords[0][0] * RIGHT + coords[0][1] * UP, radius = 0.06, color = BLACK)
		pb = Dot(coords[1][0] * RIGHT + coords[1][1] * UP, radius = 0.06, color = BLACK)
		pc = Dot(coords[2][0] * RIGHT + coords[2][1] * UP, radius = 0.06, color = BLACK)
		points = VGroup(pa, pb, pc)

		pa_t = MathTex("A", color = BLACK, font_size = 40).next_to(pa, UP).shift(0.2 * DOWN)
		pb_t = MathTex("B", color = BLACK, font_size = 40).next_to(pb, LEFT).shift(0.2 * RIGHT)
		pc_t = MathTex("C", color = BLACK, font_size = 40).next_to(pc, RIGHT).shift(0.2 * LEFT)
		points_t = VGroup(pa_t, pb_t, pc_t)

		la = Line(pb.get_center(), pc.get_center(), color = BLACK)
		lb = Line(pa.get_center(), pc.get_center(), color = BLACK)
		lc = Line(pa.get_center(), pb.get_center(), color = BLACK)
		lines = VGroup(la, lb, lc)

		(cx, cy), cr = find_circumcircle(coords)

		po = Dot(cx * RIGHT + cy * UP, radius = 0.06, color = BLACK)
		circle = Circle(radius = cr, color = BLACK).move_to(po.get_center())

		ph = find_foot_of_perpendicular(la, pa)
		ph_l = Line(pa.get_center(), ph.get_center(), color = BLACK)
		ph_t = MathTex("H", color = BLACK, font_size = 40).next_to(ph, DOWN).shift(0.2 * UP)
		ph_ra = RightAngle(Line(ph.get_center(), pa.get_center()), Line(ph.get_center(), pb.get_center()),
					 length = 0.25, color = BLACK)

		pl2 = Dot(circle.point_from_proportion(0.75), radius = 0.06, color = BLACK)
		pl2_l = Line(pa.get_center(), pl2.get_center(), color = BLACK)
		pl2_t = MathTex("K", color = BLACK, font_size = 40).next_to(pl2, LEFT).shift(0.25 * UP + 0.1 * RIGHT)

		pl = Dot(line_intersection(la, pl2_l).get_center(), radius = 0.06, color = BLACK)
		pl_l = Line(pa.get_center(), pl.get_center(), color = BLACK)
		pl_t = MathTex("L", color = BLACK, font_size = 40).next_to(pl, DOWN).shift(0.15 * UP + 0.15 * LEFT)

		pm = Dot((pb.get_center() + pc.get_center()) / 2, radius = 0.06, color = BLACK)
		pm_l = Line(pa.get_center(), pm.get_center(), color = BLACK)
		pm_t = MathTex("M", color = BLACK, font_size = 40).next_to(pm, UP).shift(0.15 * DOWN + 0.2 * RIGHT)

		mk_l = Line(pm.get_center(), pl2.get_center(), color = BLACK)
		mk_ra = RightAngle(Line(pm.get_center(), pl2.get_center()), Line(pm.get_center(), pc.get_center()),
					 length = 0.25, color = BLACK)

		txt1 = MathTex(r"BM = CM", color = BLACK, font_size = 60).shift(4.5 * RIGHT + 2.5 * UP)
		txt2 = MathTex(r"\angle{BAL} = \angle{CAL}", color = BLACK, font_size = 60).next_to(txt1, DOWN)
		txt3 = MathTex(r"AH \leq AL \leq AM", color = BLACK, font_size = 60).next_to(txt2, DOWN).shift(3 * DOWN)

		self.wait(2)
		self.play(Create(points, lag_ratio = 0), Write(points_t, lag_ratio = 0), Create(lines, lag_ratio = 0),
			run_time = 2)
		self.wait(2)
		self.play(Create(ph), Create(ph_l), run_time = 2)
		self.wait(2)
		self.play(Create(pl), Create(pl_l), run_time = 2)
		self.wait(2)
		self.play(Create(pm), Create(pm_l), run_time = 2)

		self.wait(2)
		self.play(Create(ph_ra), Write(ph_t), run_time = 2)

		self.wait(2)
		self.play(Write(pl_t), Write(pm_t), run_time = 2)

		self.wait(2)
		self.play(Create(circle), run_time = 2)
		self.wait(2)
		self.play(Write(txt1), Write(txt2), run_time = 2)
		self.wait(2)
		self.play(Create(pl2), Create(pl2_l), Write(pl2_t), run_time = 2)
		self.wait(2)
		self.play(Create(mk_l), Write(mk_ra), run_time = 2)

		self.wait(2)
		self.play(Write(txt3), run_time = 2)

		self.wait(3)

	def construct(self):
		self.camera.background_color = WHITE

		self.showa1()
		self.clearEverything()
		self.showa2()
		self.clearEverything()
		self.showa3()
		self.clearEverything()