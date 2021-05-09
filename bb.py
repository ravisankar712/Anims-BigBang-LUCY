from manimlib.imports import *
from scipy.optimize import curve_fit


class GraphDensity(GraphScene):
    CONFIG = {
        "x_axis_label" : "$t$",
        "y_axis_label" : "$\\rho(t)$",
        "x_label_direction": DOWN,
        "y_label_direction": LEFT,
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
    }
    def construct(self):
        self.setup_axes(True)

        the_equation = TexMobject("\\rho(", "t", ")", "=", "k", "\\left(", "t_0", "\\over", "t",  "\\right)", "^2")
        the_equation[1].set_color(RED)
        the_equation[8].set_color(RED)
        the_equation.shift(UP*2 + RIGHT*3)
        self.play(
            Write(the_equation)
        )

        self.wait()

        def get_density_graph(t0=10.0, K=1.0):
            def density(t):
                return K * (t0/t)**(2.0)
            return density

        rho = self.get_graph(get_density_graph(t0=2.0, K=1.0), x_min=0.01, step_size=0.0001, color="#f8961e")
        rho.shift(UP * 0.3) #fudge to make it look nicer
        self.play(
            ShowCreation(rho.reverse_points()), run_time=3.0
        )
        self.wait()

class GraphScaleFactor(GraphScene):
    CONFIG = {
        "x_axis_label" : "$t$",
        "y_axis_label" : "$a(t)$",
        "x_label_direction": DOWN,
        "y_label_direction": LEFT,
    }
    def construct(self):
        self.setup_axes(True)

        the_equation = TexMobject("a(", "t", ")", "=","\\left(", "t", "\\over", "t_0",  "\\right)", "^{\\frac{2}{3}}")
        the_equation[1].set_color(RED)
        the_equation[5].set_color(RED)
        the_equation.shift(UP*2 + RIGHT*3)
        self.play(
            Write(the_equation)
        )

        self.wait()

        def get_scalefactor_graph(t0=10.0, K=1.0):
            def scalefactor(t):
                return K * (t/t0)**(2/3.0)
            return scalefactor

        rho = self.get_graph(get_scalefactor_graph(t0=0.6), x_min=0.01, step_size=0.0001, color="#9a031e")
        self.play(
            ShowCreation(rho.reverse_points()), run_time=3.0
        )
        self.wait()
        origin = self.coords_to_point(0, 0)
        self.play(
            FocusOn(origin, color="#e36414")
        )
        arrow = Arrow(origin + UP*2 + RIGHT, origin, color="#fb8b24")
        self.play(
            GrowArrow(arrow)
        )
        a_at_O = TexMobject("a", "(", "t", "=", "0", ")", "=", "0").scale(0.7).move_to(origin + UP*2 + RIGHT)
        a_at_O[2].set_color(RED)
        self.play(
            Write(a_at_O)
        )
        self.wait()

class Findingrho(Scene):

    def construct(self):

        temp = TexMobject("\\rho", "=")
        rho_of_a = VGroup(temp, TexMobject("k", "\\over", "a", "^3" ).next_to(temp, RIGHT).shift(UP*0.1)).shift(UP)
        # rho_of_a[1][2].set_color(ORANGE)
        a_of_t = TexMobject("a", "=", "\\left(", "t", "\\over", "t_0", "\\right)", "^{\\frac{2}{3}}" ).shift(DOWN)
        a_of_t[3].set_color(RED)

        self.play(
            Write(rho_of_a)
        )
        self.play(
            Write(a_of_t)
        )
        self.wait()
        self.play(
            ApplyMethod(rho_of_a.shift, LEFT*4),
            ApplyMethod(a_of_t.shift, LEFT*4)
        )
        brace = Brace(VGroup(rho_of_a, a_of_t), RIGHT)
        self.play(
            GrowFromCenter(brace)
        )
        implies = TexMobject("\\Rightarrow").next_to(brace, RIGHT)
        self.play(
            FadeInFrom(implies, LEFT)
        )
        rho_of_t_lhs = TexMobject("\\rho", "(", "t", ")", "=")
        rho_of_t_lhs[2].set_color(RED)
        rho_of_t_lhs.next_to(implies, RIGHT)
        self.play(
            TransformFromCopy(rho_of_a[0], rho_of_t_lhs[0]),
        )
        self.play(
            Write(rho_of_t_lhs[1:])
        )
        rho_t_rhs1 = TexMobject("k", "\\over", "\\left[","\\left(", "t", "\\over", "t_0", "\\right)", "^{\\frac{2}{3}}", "\\right]", "^3").next_to(rho_of_t_lhs)
        rho_t_rhs1.shift(DOWN*0.4)
        rho_t_rhs1[4].set_color(RED)
        self.play(
            TransformFromCopy(rho_of_a[1][0], rho_t_rhs1[0]),
        )
        self.play(
            Write(rho_t_rhs1[1]),
            TransformFromCopy(a_of_t, rho_t_rhs1[3:9])
        )
        self.play(
            Write(rho_t_rhs1[2]),
            Write(rho_t_rhs1[-2:])
        )
        rho_t = TexMobject("=", "k", "\\left(", "t_0", "\\over", "t", "\\right)", "^2").next_to(rho_t_rhs1).shift(UP*0.5)
        rho_t[5].set_color(RED)
        self.play(
            Write(rho_t[:2])
        )
        self.play(
            Write(rho_t[2:])
        )

        self.wait()
        
        self.wait()

class Friedmann(Scene):

    def construct(self):
        
        lhs = TexMobject("\\left(", "\\dot{a}", "\\over", "a", "\\right)", "^2", color="#fdfcdc")
        eq = TexMobject("=", color="#fdfcdc").next_to(lhs, RIGHT)
        rhs = TexMobject("\\left(", "8", "\\pi", "G", "\\over", "3", "\\right)", "\\rho", color="#fdfcdc").next_to(eq, RIGHT)
        friedmann = VGroup(lhs, eq, rhs).scale(1.5).move_to(ORIGIN)
        title = TextMobject("Friedmann Equation", color="#fb8b24").scale(1.5).to_edge(UP)
        self.play(
            FadeInFromDown(title)
        )
        self.wait()
        self.play(
            Write(lhs)
        )
        self.play(
            Write(eq)
        )
        self.play(
            Write(rhs[:-1])
        )
        self.play(
            Write(rhs[-1])
        )
        self.wait()

        #explain terms
        self.play(
            Indicate(lhs[3], color="#00afb9", scale_factor=2)
        )
        scale_factor = TextMobject("Scale", " Factor", color="#f4d58d").shift(DOWN*2).scale(1.5)
        self.play(
            ShowIncreasingSubsets(scale_factor)
        )
        self.play(
            FadeOut(scale_factor)
        )
        self.wait(0.5)
        self.play(
            Indicate(lhs[1], color="#00afb9", scale_factor=2)
        )
        dadt = TextMobject("Rate", " of", " Change", color="#f4d58d").shift(DOWN*2).scale(1.5)
        self.play(
            ShowIncreasingSubsets(dadt)
        )
        self.play(
            FadeOut(dadt)
        )
        self.wait(0.5)
        self.play(
            Indicate(rhs[3], color="#00afb9", scale_factor=2)
        )
        G = TextMobject("Newton's", " Constant", color="#f4d58d").shift(DOWN*2).scale(1.5)
        self.play(
            ShowIncreasingSubsets(G)
        )
        self.play(
            FadeOut(G)
        )
        self.wait(0.5)
        self.play(
            Indicate(rhs[-1], color="#00afb9", scale_factor=2)
        )
        density = TextMobject("Energy", " Density", color="#f4d58d").shift(DOWN*2).scale(1.5)
        self.play(
            ShowIncreasingSubsets(density)
        )
        self.play(
            FadeOut(density)
        )
        self.wait()

class ScaleFactorIntro(VectorScene, ZoomedScene):

    def construct(self):
        self.add_plane(animate=True, background_line_style= {
            "stroke_color": GREEN,
            "stroke_width": 1,
            "stroke_opacity": 0.4,
        },
        axis_config = {
            "stroke_color" : GREEN,
            "stroke_width" : 0.
        },
        run_time=2)
        self.wait()
        time = TexMobject("time =", "t_0").to_corner(UR)
        self.play(
            Write(time)
        )
        us = Dot(color="#0077b6", radius=0.2)
        
        self.play(
            FocusOn(us, color=BLUE)
        )
        self.play(
            GrowFromCenter(us)
        )
        self.wait()

        galaxy = Dot(color=GOLD, radius=0.2).shift(4*RIGHT)
        
        self.play(
            FocusOn(galaxy, color=GOLD)
        )
        self.play(
            GrowFromCenter(galaxy)
        )
        self.wait()
        lines = VGroup()
        for i in range(4):
            l = Line(UP/2.0, DOWN/2.0, color=GREEN).shift((i+1)*RIGHT)
            lines.add(l)

        self.play(
            AnimationGroup(
                *[ShowCreationThenFadeOut(l) for l in lines], lag_ratio=0.5, run_time=1.0
            )
        )
        self.wait()

        brace = Brace(VGroup(us, galaxy), DOWN)
        self.play(
            FadeInFromDown(brace)
        )
        ell = TexMobject("\\ell", "=", "4").next_to(brace, DOWN)
        self.play(
            Write(ell)
        )
        self.wait()
        self.play(
            FadeOut(brace),
            FadeOut(ell)
        )
        self.wait()
        light = Line(ORIGIN, RIGHT*4, color="#ffd60a", stroke_width=8.0)

        self.play(
            ShowCreationThenDestruction(light)
        )
        self.play(
            ShowCreationThenDestruction(light.reverse_points())
        )
        self.wait()

        d1 = TexMobject("d_{phys}(t_0)").move_to(ell).shift(UP * 2)
        self.play(
            Write(d1)
        )
        self.wait()
        self.play(
            FadeOut(d1)
        )
        def justfortime(m, alpha):
            m.restore()
            m.scale((1 - alpha) + alpha * 9/14.)
            m.shift((RIGHT*3.6 + UP*2.1 - m.get_center())*alpha)
            
        time.save_state()
        self.play(
            ApplyMethod(self.camera_frame.set_width, 9),
            ApplyMethod(us.scale, 9/14.0),
            ApplyMethod(galaxy.scale, 9/14.0),
            UpdateFromAlphaFunc(time, justfortime),
            run_time=2.0
        )
        self.play(
            Transform(time[1], TexMobject("t").scale(9/14.).move_to(time[1]))
        )
        self.wait()
        self.play(
            AnimationGroup(
                *[ShowCreationThenFadeOut(l) for l in lines], lag_ratio=0.5, run_time=1.0
            )
        )
        self.wait()
        ell.scale(9./14.)
        self.play(
            FadeIn(brace),
            Write(ell)
        )
        self.wait()
        self.play(
            FadeOut(brace),
            FadeOut(ell)
        )

        self.wait()
        self.play(
            ShowCreationThenDestruction(light.reverse_points()), run_time=1.5
        )
        self.play(
            ShowCreationThenDestruction(light.reverse_points()), run_time=1.5
        )
        self.wait()

        d2 = TexMobject("d_{phys}(t)", ">", "d_{phys}(t_0)").move_to(ell).shift(UP * 2).scale(9.0/14.0)
        self.play(
            Write(d2)
        )
        self.wait()
        self.play(
            FadeOut(d2)
        )
        self.wait()
        self.play(
            FadeOut(us),
            FadeOut(galaxy),
            FadeOut(time)
        )
        at = TexMobject("d_{phys}", "(", "t", ")", "=", "a", "(","t", ")", "\\ell").scale(9./14)
        self.wait()
        self.play(
            Write(at[0])
        )
        self.play(
            Write(at[-1])
        )
        self.wait()
        self.play(
            Write(at[1:4])
        )
        self.wait()
        self.play(
            Write(at[4:-1])
        )

        self.wait()
        self.play(
            Indicate(at[5:9], color="#38b000", scale_factor=2.0)
        )
        text = TextMobject("Scale", " Factor", color="#1982c4").shift(UP)
        self.play(
            ShowIncreasingSubsets(text)
        )
        self.play(
            FadeOut(text)
        )
        self.wait()
        scale_factor = TexMobject("d_{phys}(t = ","0", ")" "=", "a(t = ", "0", ")", "\\ell").scale(9.0/14)
        scale_factor[1].set_opacity(0.0)
        scale_factor[4].set_opacity(0.0)
        time1 = DecimalNumber(0, num_decimal_places=0).scale(9.0/14).move_to(scale_factor[1])
        time2 = DecimalNumber(0, num_decimal_places=0).scale(9.0/14).move_to(scale_factor[4])
        # self.play(
        #     Write(scale_factor),
            
        # )
        self.play(
            ReplacementTransform(at, scale_factor)
        )
        self.play(
            Write(time1),
            Write(time2)
        )
        self.wait()
        time1.add_updater(lambda m,dt : m.move_to(scale_factor[1]))
        time2.add_updater(lambda m,dt : m.move_to(scale_factor[4]))
        time1.add_updater(lambda m,dt : m.set_value(m.get_value() + dt*2))
        time2.add_updater(lambda m,dt : m.set_value(m.get_value() + dt*2))
        self.add(time1, time2)
 
        self.play(
            ApplyMethod(
                self.camera_frame.set_width, 2
            ),
            ApplyMethod(scale_factor.scale, 2.0/9),
            ApplyMethod(time1.scale, 2.0/9),
            ApplyMethod(time2.scale, 2.0/9),
            run_time=4.5,
            rate_func=linear
        )
        time1.set_value(9)
        time2.set_value(9)
        time1.clear_updaters()
        time2.clear_updaters()
        self.wait()

class HubblesLaw(GraphScene):

    CONFIG = {
        "x_min": -1,
        "x_max": 120,
        "x_axis_width": 10,
        "x_tick_frequency": 10,
        "x_leftmost_tick": 0,  # Change if different from x_min
        "x_labeled_nums": [i for i in range(0, 120, 20)],
        "x_axis_label": "$d (Mpc)$",
        "y_min": -1,
        "y_max": 10000,
        "y_axis_height": 6,
        "y_tick_frequency": 1000,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [i for i in range(2000, 10000, 2000)],
        "y_axis_label": "v (km/s)",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": False,

        #myedits
        "x_label_direction": DOWN,
        "y_label_direction": LEFT,
    }

    def construct(self):
        self.setup_axes(True)

        #data taken from :: https://iopscience.iop.org/article/10.1086/320638/pdf --- table 7
        D = [89.2, 66.7, 114.9, 62.2, 88.4, 45.1, 74.3, 43.2, 68.2, 85.6, 20.7, 39.5, 15.0, 58.3, 31.3, 38.7, 66.6, 57.3, 50.9, 53.3, 19.8]
        v = [6709, 4730, 8930, 4749, 7016, 3106, 4982, 3272, 4820, 7143, 1607, 3149, 1380, 4061, 2304, 3294, 4924, 4869, 4398, 3545, 1088]
        data_dots = VGroup()
        for i in range(len(D)):
            point = self.coords_to_point(D[i], v[i])
            d = Dot(color="#c5d86d").move_to(point)
            data_dots.add(d)

        ##last point is for Ursa Major
        self.wait()
        self.play(
            FocusOn(self.coords_to_point(0, 0), color=GREEN)
        )
        self.wait()
        self.play(
            GrowFromCenter(data_dots[-1])
        )
        self.wait()
        arrow = Arrow(data_dots[-1].get_center() + UR, data_dots[-1], color=BLUE)
        text = TextMobject("Ursa Major", color=DARK_BLUE).next_to(arrow, UP).shift(RIGHT)
        self.play(
            GrowArrow(arrow),
            Write(text)
        )
        self.wait()
        self.play(
            FadeOut(arrow),
            FadeOut(text)
        )
        self.wait()
        x_line = Line(self.coords_to_point(0, 0), self.coords_to_point(D[-1], 0), color=ORANGE, stroke_width=8.0).add_tip()
        y_line = Line(self.coords_to_point(D[-1], 0), self.coords_to_point(D[-1], v[-1]), color=ORANGE, stroke_width=8.0).add_tip()
        self.play(
            ShowCreationThenFadeOut(x_line)
        )
        self.wait()
        self.play(
            ShowCreationThenFadeOut(y_line)
        )
        self.wait(2)
        self.play(
            AnimationGroup(
                *[GrowFromCenter(d) for d in data_dots[:-1]], lag_ratio=0.5, run_time=1.5
            )
        )

        def line(x, m, c):
            return m*x + c

        def get_line(m, c):
            def y(x):
                return m*x + c
            return y

        params,_ = curve_fit(line, D, v)
        fit = self.get_graph(get_line(*params), color="#1b998b")

        self.wait(2)
        self.play(
            ShowCreation(fit)
        )
        # self.add(data_dots)

        self.wait()

class SolutionDust(Scene):

    def construct(self):
        today = TexMobject("\\text{today, }", "t_0").shift(UP*2 + LEFT*4)
        at0 = TexMobject("a", "(", "t_0", ")", "=", "1").next_to(today, DOWN, buff=MED_LARGE_BUFF)
        later = TexMobject("\\text{later, }", "t", "> t_0").shift(UP*2 + RIGHT*4)
        later[1].set_color(RED)
        at = TexMobject("a", "(", "t", ")", ">", "1").next_to(later, DOWN, buff=MED_LARGE_BUFF)
        at[2].set_color(RED)
        self.play(
            FadeInFromDown(today)
        )
        self.play(
            ShowCreation(Underline(today))
        )
        self.play(
            Write(at0)
        )

        self.play(
            FadeInFromDown(later)
        )
        self.play(
            ShowCreation(Underline(later))
        )
        self.play(
            Write(at)
        )
        self.wait()

        dphyst0 = TexMobject("d_{phys}", "(", "t_0", ")", "=", "d").next_to(at0, DOWN, buff=MED_LARGE_BUFF)
        dphyst = TexMobject("d_{phys}", "(", "t", ")", "=", "a(t)", "d").next_to(at, DOWN, buff=MED_LARGE_BUFF)
        dphyst[2].set_color(RED)
        self.play(
            Write(dphyst0)
        )
        self.wait()
        self.play(
            Write(dphyst)
        )
        self.wait()

        Vphyst0 = TexMobject("V", "(", "t_0", ")", "=", "d", "^3").next_to(dphyst0, DOWN, buff=MED_LARGE_BUFF)
        Vphyst = TexMobject("V", "(", "t", ")", "=", "a^3(t)", "d", "^3").next_to(dphyst, DOWN, buff=MED_LARGE_BUFF)
        Vphyst[2].set_color(RED)
        self.play(
            Write(Vphyst0)
        )
        self.wait()
        self.play(
            Write(Vphyst)
        )
        self.wait()

        rhophyst0 = TexMobject("\\rho", "(", "t_0", ")", "\\propto", "\\frac{1}{d^3}").next_to(Vphyst0, DOWN, buff=MED_LARGE_BUFF)
        rhophyst = TexMobject("\\rho", "(", "t", ")", "\\propto", "\\frac{1}{a^3(t)d^3}").next_to(Vphyst, DOWN, buff=MED_LARGE_BUFF)
        rhophyst[2].set_color(RED)
        self.play(
            Write(rhophyst0)
        )
        self.wait()
        self.play(
            Write(rhophyst)
        )
        self.wait()

        self.play(
            AnimationGroup(
                *[Uncreate(m) for m in self.get_top_level_mobjects()], lag_ratio=0.2
            )
        )
        self.wait()
        rhot = TexMobject("\\rho", "\\propto", "\\frac{1}{a^3}").scale(1.5)
        self.play(
            Write(rhot)
        )
        self.wait()
        self.play(
            Transform(rhot[1], TexMobject("=").move_to(rhot[1])),
            Transform(rhot[2], TexMobject("\\frac{k}{a^3}").move_to(rhot[2]).scale(1.5))
        )
        self.wait()
        self.play(
            Uncreate(rhot)
        )

        lhs = TexMobject("\\left(", "\\dot{a}", "\\over", "a", "\\right)", "^2", color=WHITE)
        eq = TexMobject("=", color=WHITE).next_to(lhs, RIGHT)
        rhs = TexMobject("\\left(", "8", "\\pi", "G", "\\over", "3", "\\right)", "\\rho", color=WHITE).next_to(eq, RIGHT)
        friedmann = VGroup(lhs, eq, rhs).move_to(ORIGIN).scale(1.5)
        self.play(
            Write(friedmann)
        )
        self.wait()
        self.play(
            Transform(rhs[-1], TexMobject("\\frac{k}{a^3}").scale(1.5).move_to(rhs[-1]).shift(UP*.15))
        )
        self.wait()
        self.play(
            Uncreate(rhs)
        )
        rhs = TexMobject("\\sqrt{", "D", "\\over", "a^3", "2", "}").scale(1.5).next_to(eq, RIGHT)
        self.play(
            Write(rhs[2:])
        )
        self.wait()
        self.play(
            CircleIndicate(lhs[-1])
        )
        self.play(
            Uncreate(lhs[0]),
            Uncreate(lhs[-2:]),
            ShowCreation(rhs[0]),
            ShowCreation(rhs[1])
        )
        self.wait()
        self.play(
            Uncreate(lhs),
            Uncreate(eq),
            Uncreate(rhs)
        )
        eq = TexMobject("=").scale(1.5)
        lhs = TexMobject("\\int{", "\\sqrt{a} \\, \\, \\, \\,", "\\dot{a}", "\\, \\, \\, \\, \\, \\,\\, \\, }").scale(1.5).next_to(eq, LEFT)
        rhs = TexMobject("\\sqrt{D}", "\\int{",  "dt", "}").scale(1.5).next_to(eq, RIGHT)
        self.play(
            Write(lhs[1:-1])
        )
        self.play(
            Write(eq),
            Write(rhs[0])
        )
        self.wait()
        self.play(
            Transform(lhs[2], TexMobject("da", "\\over", "dt").scale(1.5).move_to(lhs[2]))
        )
        self.wait()
        self.play(
            ApplyMethod(lhs[2][-1].move_to, rhs[-2])
        )
        self.play(
            Uncreate(lhs[2][1]),
            ApplyMethod(lhs[2][0].next_to, lhs[1], buff=0.1)
        )
        self.play(
            Write(lhs[0]),
            Write(rhs[1])
        )
        self.wait()
        self.play(
            Uncreate(lhs),
            Uncreate(rhs),
            FadeOut(eq)
        )
        self.wait()
        lhs = TexMobject("a", "(", "t", ")").scale(1.5).next_to(eq, LEFT)
        lhs[2].set_color(RED)
        rhs = TexMobject("\\left(", "t", "\\over", "t_0", "\\right)", "^{\\frac{2}{3}}").scale(1.5).next_to(eq, RIGHT)
        rhs[1].set_color(RED)
        self.play(
            Write(lhs)
        )
        self.play(
            Write(rhs),
            Write(eq)
        )
        self.wait()

SCENES_IN_ORDER = [
    HubblesLaw,
    ScaleFactorIntro,
    Friedmann,
    SolutionDust,
    GraphScaleFactor,
    Findingrho,
    GraphDensity
]