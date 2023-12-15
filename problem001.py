from manim import *

class VMobjectDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]),  # start of first curve
            np.array([-3, 1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]),  # end of first curve
            np.array([1, 3, 0]),  # start of second curve
            np.array([0, 1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0]),  # end of second curve
        ]
        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]
        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]
        self.add(plane, *handles, *handle_lines, my_vmobject)


class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()


# from manim import *

# class MathProblem(Scene):
#     def construct(self):
#         # Problem
#         problem_text = MathTex(r"\int \frac{\sin ^2 x}{1+\sin ^2 x} \mathrm{~d} x").scale(0.8)
#         self.play(Write(problem_text))
#         self.wait(1)

#         # Solution
#         solution_text = MathTex(r"\begin{aligned} & \int \frac{\sin ^2 x}{1+\sin ^2 x} \mathrm{~d} x = \int\left(1-\frac{1}{1+\sin ^2 x}\right) \mathrm{d} x \\ & = x - \int \frac{\mathrm{d}(\tan x)}{\sec ^2 x+\tan ^2 x} = x - \int \frac{\mathrm{d}(\tan x)}{1+2 \tan ^2 x} \\ & = x - \frac{1}{\sqrt{2}} \arctan (\sqrt{2} \tan x) + C \end{aligned}").scale(0.7)
#         solution_text.next_to(problem_text, DOWN, buff=1)
#         self.play(Write(solution_text))
#         self.wait(2)

#         # Highlight important steps
#         steps_to_highlight = [1, 3, 5]
#         for step_num in steps_to_highlight:
#             self.play(solution_text[step_num].animate.set_color(YELLOW))
#             self.wait(2)
#             self.play(solution_text[step_num].animate.set_color(WHITE))
#             self.wait(1)

#         self.wait(2)

#         # Final result
#         final_result_text = MathTex(r"\text{The final result is } x - \frac{1}{\sqrt{2}} \arctan (\sqrt{2} \tan x) + C").scale(0.8)
#         final_result_text.next_to(solution_text, DOWN, buff=1)
#         self.play(Write(final_result_text))
#         self.wait(2)




class MathIntegral(Scene):
    def construct(self):
       
        # Problem text
        problem_text = MathTex(r"\int \frac{\sin ^2 x}{1+\sin ^2 x} \mathrm{~d} x").scale(0.8)

        # Additional text
        additional_text = Text("What's the solution of this problem?").scale(0.6)
        
        # Move the text to the left-upper corner
        text_group = VGroup(additional_text, problem_text)
        text_group.arrange(DOWN)
        #text_group.to_corner(UL)  # Move to the upper-left corner
        text_group.to_corner(UL) 

        # Calculate the dimensions of the problem_text
        width = problem_text.get_width() + 0.2
        height = problem_text.get_height() + 0.2

        # Create a yellow rectangle and set its position
        mob = Rectangle(width=width, height=height, color=YELLOW)
        mob.move_to(problem_text)  # Set the position to align with the problem_text
        self.play(Write(text_group))
        self.play(Create(mob))      

        self.wait(10.5)
        # Solution text
        solution_text1 = MathTex(
        r"=& \int \frac{1 + \sin ^2 x - 1}{1+\sin ^2 x} \mathrm{~d} x"
        ).scale(0.7)

        # Position the solution_text below the problem_text
        solution_text1.next_to(problem_text, DOWN, buff=0.5)
        
        solution_text2 = MathTex(
        r"=&\int\left(1-\frac{1}{1+\sin ^2 x} \right) \mathrm{~d} x"
        ).scale(0.7)

        solution_text2.next_to(solution_text1, DOWN, buff=0.5)

        solution_text3 = MathTex(
        r"=&x-\int \left( \frac{1}{1+\sin ^2 x} \right) \mathrm{d} x"
        ).scale(0.7)
        
        solution_text3.next_to(solution_text2, DOWN, buff=0.5)




        self.play(Write(solution_text1))
        self.play(Write(solution_text2))
        self.play(Write(solution_text3))

        mob2 = Rectangle(width=width*5, height=height*5, color=WHITE)
        mob2.to_corner(UR)  # Move to the upper-left corner  # Set the position to align with the problem_text
        self.play(Create(mob2))

        self.wait(10)





