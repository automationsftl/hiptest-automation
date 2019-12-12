# encoding: UTF-8
import unittest

from framework.browser import WebApp
from hiptest.actionwords import Actionwords


class TestFYM(unittest.TestCase):
    def setUp(self):
        self.webApp = WebApp()
        self.actionwords = Actionwords(self.webApp)

    def tearDown(self):
        self.webApp.quit()

    def smoke__as_a_teacher_i_can_login_in_the_application(self, username, password, subject):
        # Tags: status priority_P0 test_case_level_Smoke JIRA:FY-11
        # Given a teacher on the login page
        self.actionwords.a_teacher_on_the_login_page()
        # When teacher enters in the login page "<username>" and "<password>"
        self.actionwords.teacher_enters_in_the_login_page_p1_and_p2(p1 = username, p2 = password)
        # And teacher clicks Submit button
        self.actionwords.teacher_clicks_submit_button()
        # Then logs in and lands on the Homepage and sees "<subject>"
        self.actionwords.logs_in_and_lands_on_the_homepage_and_sees(p1 = subject)

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uid2bd7e766ab97489198cfa1cdb2e89eda(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.worldhistory@testschool.org', password = 'password', subject = 'AP World History: Modern')

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uid9059fd48d38747f4bc60d075fd948042(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.calculus@testschool.org', password = 'password', subject = 'Calculus')

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uid81cd450f4c534fc4981d2534d19c871f(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.apbiology@testschool.org', password = 'password', subject = 'AP Insight Biology')

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uid9991f942ced542a6967c4ad668576ef2(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.biology@testschool.org', password = 'password', subject = 'Biology')

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uida2b8d1864a1b410a85339042dd170765(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.ushistory@testschool.org', password = 'password', subject = 'U.S. History')

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uid917b5c37df7840578fe648abf172f7b2(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.calculusphysics@testschool.org', password = 'password', subject = 'Calculus')

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uid68bd2a4686f240c6b84d1751df18bed3(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.physicsEMphysicsM@testschool.org', password = 'password', subject = 'Physics C: Electricity & Magnetism')

    def test_Smoke__As_a_teacher_I_can_login_in_the_application__uid808eebea55a14e85bc969b72a8f5dfc8(self):
        self.smoke__as_a_teacher_i_can_login_in_the_application(username = 'teacher.physicschemistry@testschool.org', password = 'password', subject = 'Physics C: Electricity & Magnetism')


    def smoke__ap_only_teacher_multiple_ap_subjects_onscreen(self):
        # Tags: priority_P1 test_case_level_Smoke JIRA:PREAP-51 JIRA:PREAP-50 JIRA:PREAP-275 Regression
        # Given a teacher with multiple AP subjects on the login page
        self.actionwords.a_teacher_with_multiple_ap_subjects_on_the_login_page()
        # But no Pre-AP subjects
        self.actionwords.no_pre_ap_subjects()
        # When the teacher logs in
        self.actionwords.the_teacher_logs_in()
        # Then he lands on My Subjects page where he can see the AP courses he has access to onscreen
        self.actionwords.he_lands_on_my_subjects_page_where_he_can_see_the_ap_courses_he_has_access_to_onscreen()
        # And the Pre-AP section is not displayed
        self.actionwords.the_pre_ap_section_is_not_displayed()

    def test_Smoke__AP_only_teacherMultiple_AP_subjects_onscreen__uid87d9a5fdb4c240d9937cbcb66c6bd880(self):
        self.smoke__ap_only_teacher_multiple_ap_subjects_onscreen()



    def smoke__homepage_has_the_correct_subject_displayed_in_the_dropdownheader(self, subject):
        # Tags: priority_P0 Regression JIRA:FY-5474
        # Given teacher is "<subject>" teacher
        self.actionwords.teacher_is_p1_teacher(p1 = subject)
        # When he clicks on "<subject>"
        self.actionwords.he_clicks_on_p1(p1 = subject, free_text = "", datatable = "||")
        # Then teacher lands on the Course Homepage and sees "<subject>" in the page header
        self.actionwords.teacher_lands_on_the_course_homepage_and_sees_p1_in_the_page_header(p1 = subject)

    def test_Smoke__Homepage_has_the_correct_subject_displayed_in_the_dropdownheader__uid77cac202d8a3456e846e00e87da36e2e(self):
        self.smoke__homepage_has_the_correct_subject_displayed_in_the_dropdownheader(subject = 'AP Calculus AB')

    def test_Smoke__Homepage_has_the_correct_subject_displayed_in_the_dropdownheader__uid53978cea9f2e4ceab15e5ed914ae2c71(self):
        self.smoke__homepage_has_the_correct_subject_displayed_in_the_dropdownheader(subject = 'AP Calculus BC')

    def test_Smoke__Homepage_has_the_correct_subject_displayed_in_the_dropdownheader__uidd407f5f3e1c046838e1026b9ea46bf8e(self):
        self.smoke__homepage_has_the_correct_subject_displayed_in_the_dropdownheader(subject = 'AP Calculus AB and BC')



    def smoke__teacher_units_display_on_the_homepage(self, cond, env, browser):
        # Tags: JIRA:FY-5152 priority_P0 test_case_level_Smoke JIRA:FY-5154
        # Given a teacher on the login page opened on "<env>" using "<browser>"
        self.actionwords.a_teacher_on_the_login_page_opened_on_p2_using_p3(p2 = env, p3 = browser)
        # When he logs in and navigates to the homepage of a "<cond>" subject
        self.actionwords.he_logs_in_and_navigates_to_the_homepage_of_a_p1_subject(p1 = cond)
        # Then he sees each unit and its content displayed in a tab
        self.actionwords.he_sees_each_unit_and_its_content_displayed_in_a_tab()

    def test_Smoke__Teacher_Units_display_on_the_homepage__uidb0ea04a958ed4cd4b237f149cd4736ba(self):
        self.smoke__teacher_units_display_on_the_homepage(cond = 'AP', env = 'desktop', browser = 'Chrome')

    def test_Smoke__Teacher_Units_display_on_the_homepage__uidf87bc90037e3483d9484c6f82dbfc3f7(self):
        self.smoke__teacher_units_display_on_the_homepage(cond = 'Pre-AP', env = 'mobile', browser = 'Safari')

    def test_Smoke__Teacher_Units_display_on_the_homepage__uid056590396aca413889abb2c6006b62e9(self):
        self.smoke__teacher_units_display_on_the_homepage(cond = 'AP', env = 'tablet', browser = 'Mozilla')

    def test_Smoke__Teacher_Units_display_on_the_homepage__uid865c51631fcf4d3295c89e38c12c43c9(self):
        self.smoke__teacher_units_display_on_the_homepage(cond = 'AP', env = 'desktop', browser = 'IE')



    def test_smoke__teacher_selected_unit_tab_highlight_state_uida93f8928820d4d4fbafffbf5061d277a(self):
        # Tags: JIRA:FY-5152 priority_P2 test_case_level_Functional_GUI
        # Given a teacher on the homepage of a subject
        self.actionwords.a_teacher_on_the_homepage_of_a_subject()
        # When he clicks on a unit tab
        self.actionwords.he_clicks_on_a_unit_tab()
        # Then that tab becomes highlighted on white
        self.actionwords.that_tab_becomes_highlighted_on_white()

    def smoke__teacher_unit_resources_within_unit_tabs_are_functional(self, subj, resources, result):
        # Tags: JIRA:FY-5152 test_case_level_Functional priority_P1
        # Given a teacher on the homepage of a "<subj>" subject
        self.actionwords.a_teacher_on_the_homepage_of_a_p1_subject(p1 = subj)
        # When he clicks on "<resources>" resource under a unit tab within Units section
        self.actionwords.he_clicks_on_p2_resource_under_a_unit_tab_within_units_section(p2 = resources)
        # Then the following happens: "<result>"
        self.actionwords.the_following_happens_p3(p3 = result)

    def test_Smoke__Teacher_Unit_resources_within_unit_tabs_are_functional__uidfaa6a230a1ed4b9caa4b23f9ae634356(self):
        self.smoke__teacher_unit_resources_within_unit_tabs_are_functional(subj = 'AP', resources = 'Unit Guide', result = 'Unit Guide pdf opens in a new tab')

    def test_Smoke__Teacher_Unit_resources_within_unit_tabs_are_functional__uid7393df5f7a1b46829f86e31a1a416c1b(self):
        self.smoke__teacher_unit_resources_within_unit_tabs_are_functional(subj = 'Pre-AP', resources = 'Sample Quiz Questions', result = 'Sample Quiz Questions pdf opens in a new tab')

    def test_Smoke__Teacher_Unit_resources_within_unit_tabs_are_functional__uid8421688c72eb4bf0b9ff6d9e1afee66a(self):
        self.smoke__teacher_unit_resources_within_unit_tabs_are_functional(subj = 'AP', resources = 'Teacher Module', result = 'Teacher Module page opens in a new tab')

    def test_Smoke__Teacher_Unit_resources_within_unit_tabs_are_functional__uidc7598e018b4946b5b3279a103e90c334(self):
        self.smoke__teacher_unit_resources_within_unit_tabs_are_functional(subj = 'AP', resources = 'Question Bank', result = 'Question Bank page opens in a new tab having the filter set to the unit number')



    def smoke__skills_associated_with_subunits_are_visible_for_all_types_of_users(self, col, result):
        # Tags: JIRA:FY-5149 priority_P1 test_case_level_Functional story_priority_p0
        # Given a "<col>" logs in and navigates to the above subject homepage
        self.actionwords.a_p1_logs_in_and_navigates_to_the_above_subject_homepage(p1 = col)
        # When clicks on a unit tab from Units section
        self.actionwords.clicks_on_a_unit_tab_from_units_section()
        # Then he sees a new column containing skills associated to the sub-units on the left side
        self.actionwords.he_sees_a_new_column_containing_skills_associated_to_the_subunits_on_the_left_side()

    def test_Smoke__Skills_associated_with_subunits_are_visible_for_all_types_of_users__uidc7259663b0074389b48df61421b65d66(self):
        self.smoke__skills_associated_with_subunits_are_visible_for_all_types_of_users(col = 'teacher', result = 'AP')

    def test_Smoke__Skills_associated_with_subunits_are_visible_for_all_types_of_users__uidf75cd8e4b9b84c4d9796f77efc79f535(self):
        self.smoke__skills_associated_with_subunits_are_visible_for_all_types_of_users(col = 'student', result = 'Pre-AP')

    def test_Smoke__Skills_associated_with_subunits_are_visible_for_all_types_of_users__uidb7d62e04aa804d64865287253fcdf3e1(self):
        self.smoke__skills_associated_with_subunits_are_visible_for_all_types_of_users(col = 'coord/admin', result = 'AP')



    def smoke__latest_unit_tab_is_remembered_when_returning_from_another_page_of_the_same_subject(self, user, type):
        # Tags: test_case_level_Functional priority_P1 JIRA:FY-5153 story_priority_p0
        # Given a "<user>" on the homepage of a "<type>" subject with units
        self.actionwords.a_p1_on_the_homepage_of_a_p2_subject_with_units(p1 = user, p2 = type)
        # And a unit tab has been accessed
        self.actionwords.a_unit_tab_has_been_accessed()
        # When he navigate to a different page of the same subject
        self.actionwords.he_navigate_to_a_different_page_of_the_same_subject()
        # And then returns to homepage
        self.actionwords.then_returns_to_homepage()
        # Then he sees the latest unit tab accessed opened along with its content
        self.actionwords.he_sees_the_latest_unit_tab_accessed_opened_along_with_its_content()

    def test_Smoke__Latest_unit_tab_is_remembered_when_returning_from_another_page_of_the_same_subject__uid5132a2d9c34b40f9ac8a9cecd42cded1(self):
        self.smoke__latest_unit_tab_is_remembered_when_returning_from_another_page_of_the_same_subject(user = 'teacher', type = 'Pre-AP')

    def test_Smoke__Latest_unit_tab_is_remembered_when_returning_from_another_page_of_the_same_subject__uid5591336c2fa841c29d5f94873275cd95(self):
        self.smoke__latest_unit_tab_is_remembered_when_returning_from_another_page_of_the_same_subject(user = 'student', type = 'AP')

    def test_Smoke__Latest_unit_tab_is_remembered_when_returning_from_another_page_of_the_same_subject__uid9ab434ea677b4dc69fe8e5ff11d2b3e5(self):
        self.smoke__latest_unit_tab_is_remembered_when_returning_from_another_page_of_the_same_subject(user = 'coord/admin', type = 'AP')



    def test_smoke__clicking_on_class_name_redirect_user_to_my_classes_uidaf276416dea3494995331120f50cdec9(self):
        # Tags: JIRA:FY-6440 priority_P1 test_case_level_Functional
        # Given a teacher on Homepage
        self.actionwords.a_teacher_on_homepage()
        # And a class is already created for the teacher
        self.actionwords.a_class_is_already_created_for_the_teacher()
        # When he clicks in the widget header on class name
        self.actionwords.he_clicks_in_the_widget_header_on_class_name()
        # Then he is redirected to My Classes with the associated class selected (https://myap.collegeboard.org/course/ {test_cd}/section/{APRO_section_id})
        self.actionwords.he_is_redirected_to_my_classes_with_the_associated_class_selected_httpsmyapcollegeboardorgcourse_test_cdsection_apro_section_id()

    def test_smoke__navigate_through_classes_using_arrows_uiddec73bc6bfbb469187c55748a9c7c4c3(self):
        # Tags: JIRA:FY-6440 priority_P2 test_case_level_Functional
        # Given a teacher on Homepage
        self.actionwords.a_teacher_on_homepage()
        # And multiple classes are created for that teacher
        self.actionwords.multiple_classes_are_created_for_that_teacher()
        # When he clicks on ">" or "<" arrows in the widget header
        self.actionwords.he_clicks_on_p1_or_p2_arrows_in_the_widget_header(p1 = ">", p2 = "<")
        # Then he is able to navigate through the classes
        self.actionwords.he_is_able_to_navigate_through_the_classes()

    def test_smoke__class_widget_default_number_of_quizzes_on_screen_uid4ce0221cae5e43a680df1c5e55817473(self):
        # Tags: priority_P1 test_case_level_Functional JIRA:FY-6441
        # Given a teacher has assigned more than 6 quizzes to a class
        self.actionwords.a_teacher_has_assigned_more_than_6_quizzes_to_a_class()
        # When he navigates to that specific class in the Class widget
        self.actionwords.he_navigates_to_that_specific_class_in_the_class_widget()
        # Then by default the first 6 quizzes(sorting rules applied)are displayed on the screen
        self.actionwords.by_default_the_first_6_quizzessorting_rules_appliedare_displayed_on_the_screen()
        # And the others are hidden
        self.actionwords.the_others_are_hidden()

    def smoke__class_widget_results_bar_precedes_progress_bars(self, cond):
        # Tags: priority_P1 test_case_level_Functional JIRA:FY-6441
        # Given a teacher has assigned multiple "<cond>" to a class
        self.actionwords.a_teacher_has_assigned_multiple_p1_to_a_class(p1 = cond)
        # And some of the assignments are in progress and some have already results
        self.actionwords.some_of_the_assignments_are_in_progress_and_some_have_already_results()
        # When the teacher navigates to that specific class in the Class widget
        self.actionwords.the_teacher_navigates_to_that_specific_class_in_the_class_widget()
        # Then he sees first the bars for results, then progress bars
        self.actionwords.he_sees_first_the_bars_for_results_then_progress_bars()

    def test_Smoke__Class_widget_results_bar_precedes_progress_bars__uid1f406912bdb247da834696613fe838ff(self):
        self.smoke__class_widget_results_bar_precedes_progress_bars(cond = 'PPCs')

    def test_Smoke__Class_widget_results_bar_precedes_progress_bars__uid07d0915d74fa477394d9fbff97e6cd5d(self):
        self.smoke__class_widget_results_bar_precedes_progress_bars(cond = 'QBs')



    def smoke__class_widget_progress_bars_when_less_than_80_of_students_have_submitted(self, cond, state):
        # Tags: priority_P1 test_case_level_Functional JIRA:FY-6441
        # Given a teacher has assigned an MCQ "<cond>"only to a class
        self.actionwords.a_teacher_has_assigned_an_mcq_p1only_to_a_class(p1 = cond)
        # And less than 80% of students have submitted the quiz
        self.actionwords.less_than_80_of_students_have_submitted_the_quiz()
        # And the quiz in "<state>" state
        self.actionwords.the_quiz_in_p2_state(p2 = state)
        # When the teacher navigates to that specific class in the Class widget
        self.actionwords.the_teacher_navigates_to_that_specific_class_in_the_class_widget()
        # Then he sees the quiz row having a Progress bar(second column) + View Progress button(third column)
        self.actionwords.he_sees_the_quiz_row_having_a_progress_barsecond_column__view_progress_buttonthird_column()

    def test_Smoke__Class_widget_Progress_bars_when_less_than_80_of_students_have_submitted__uid9eed01140a914f3f964b06bbd43fd61e(self):
        self.smoke__class_widget_progress_bars_when_less_than_80_of_students_have_submitted(cond = 'PPC', state = 'opened')

    def test_Smoke__Class_widget_Progress_bars_when_less_than_80_of_students_have_submitted__uid40111f871bf641769967f60c23e11da5(self):
        self.smoke__class_widget_progress_bars_when_less_than_80_of_students_have_submitted(cond = 'QB', state = 'locked')



    def smoke__class_widget_results_bars_when__80_of_students_have_submitted(self, cond, state, condit):
        # Tags: priority_P1 test_case_level_Functional JIRA:FY-6441
        # Given a teacher has assigned a "<cond>" to a class
        self.actionwords.a_teacher_has_assigned_a_p1_to_a_class(p1 = cond)
        # And >= 80% of students have "<condit>"
        self.actionwords._80_of_students_have_p3(p3 = condit)
        # And the quiz in "<state>" state
        self.actionwords.the_quiz_in_p2_state(p2 = state)
        # When the teacher navigates to that specific class in the Class widget
        self.actionwords.the_teacher_navigates_to_that_specific_class_in_the_class_widget()
        # Then he sees the quiz row having a Results bar(second column) + View Results button(third column)
        self.actionwords.he_sees_the_quiz_row_having_a_results_barsecond_column__view_results_buttonthird_column()

    def test_Smoke__Class_widget_Results_bars_when__80_of_students_have_submitted__uidb08cfcacbb174222b09b517b0303080f(self):
        self.smoke__class_widget_results_bars_when__80_of_students_have_submitted(cond = 'an MCQ PPC', state = 'opened', condit = 'submitted the quiz')

    def test_Smoke__Class_widget_Results_bars_when__80_of_students_have_submitted__uid210dc0ddf08e4da291fcb15410bda9fe(self):
        self.smoke__class_widget_results_bars_when__80_of_students_have_submitted(cond = 'a mixed QB', state = 'locked', condit = 'submitted the quiz and were scored')

    def test_Smoke__Class_widget_Results_bars_when__80_of_students_have_submitted__uid768d38a51761466dacd065aa394025c8(self):
        self.smoke__class_widget_results_bars_when__80_of_students_have_submitted(cond = 'an FRQ PPC', state = 'completed', condit = 'submitted the quiz and were scored')



    def smoke__class_widget_x_submissions_to_score_button_display(self, cond):
        # Tags: priority_P1 test_case_level_Functional JIRA:FY-6441
        # Given a teacher on the homepage of a subject
        self.actionwords.a_teacher_on_the_homepage_of_a_subject()
        # And there is a "<cond>" quiz assigned with students in progress > 0
        self.actionwords.there_is_a_p1_quiz_assigned_with_students_in_progress__0(p1 = cond)
        # And submitted (available to score) = X > 0
        self.actionwords.submitted_available_to_score__x__0()
        # When the teacher inspect the Class widget for the above quiz
        self.actionwords.the_teacher_inspect_the_class_widget_for_the_above_quiz()
        # Then he sees the quiz row having a “x submissions to score”button displayed in Actions column
        self.actionwords.he_sees_the_quiz_row_having_a_x_submissions_to_scorebutton_displayed_in_actions_column()

    def test_Smoke__Class_widget_X_submissions_to_score_button_display__uid67e80c27e3fe4057bf2555ec241e9fa5(self):
        self.smoke__class_widget_x_submissions_to_score_button_display(cond = 'locked FRQ')

    def test_Smoke__Class_widget_X_submissions_to_score_button_display__uid70fd997b3d7a49e58e50ae3ba29149c8(self):
        self.smoke__class_widget_x_submissions_to_score_button_display(cond = 'opened mixed')



    def test_smoke__as_a_teacher_i_want_to_be_able_to_assign_a_unit_test_to_my_class_uid24bc21d1a24244178609f7fdf67035bd(self):
        # Given the teacher is logged into the application
        self.actionwords.the_teacher_is_logged_into_the_application()
        # And teacher navigates to Progress Checks page
        self.actionwords.teacher_navigates_to_progress_checks_page()
        # And teacher navigates to Assign tab
        self.actionwords.teacher_navigates_to_assign_tab()
        # Then the teacher is able to see the Assign button for a progress check
        self.actionwords.the_teacher_is_able_to_see_the_assign_button_for_a_progress_check()

    def test_smoke__as_a_teacher_i_want_to_be_able_to_assign_an_assessment_to_a_class_uid0130ea0ec89b42a4a3eacc6a6c854a6f(self):
        # Tags: priority_P1 test_case_level_Functional
        # Given a teacher on Assign tab from Progress Checks page
        self.actionwords.a_teacher_on_assign_tab_from_progress_checks_page()
        # When clicks Assign button for an assessment
        self.actionwords.clicks_assign_button_for_an_assessment()
        # And selects a class
        self.actionwords.selects_a_class()
        # And clicks on Assign button
        self.actionwords.clicks_on_assign_button()
        # Then the assessment/quiz is assigned to that class
        self.actionwords.the_assessmentquiz_is_assigned_to_that_class()
        # And is redirected to Progress tab
        self.actionwords.is_redirected_to_progress_tab()

    def test_smoke__assign_modal_window_quick_assign_section_unlock_the_assessment_now_uid2b7a81f44bf24462a100f00e6b84dc41(self):
        # Tags: story_priority_p0 JIRA:FY-4855
        # Given the teacher is already in the UA->Assign->Assign modal window->Quick Assign section
        self.actionwords.the_teacher_is_already_in_the_ua_assign_assign_modal_window_quick_assign_section()
        # When the teacher looks at the Unlock the Assessment Now? toggle
        self.actionwords.the_teacher_looks_at_the_unlock_the_assessment_now_toggle()
        # Then he sees on the right side, a button for switching on/off
        self.actionwords.he_sees_on_the_right_side_a_button_for_switching_onoff()
        # And bellow appears the text: Your students can begin the assessment immediately and will see this assignment when they log into AP Classroom.
        self.actionwords.bellow_appears_the_text_your_students_can_begin_the_assessment_immediately_and_will_see_this_assignment_when_they_log_into_ap_classroom()

    def test_smoke__ap_subject_student_login_uid4905abcc9c3e439da91a9142a8304f0d(self):
        # Tags: priority_P1 test_case_level_Smoke JIRA:PREAP-19
        # Given a student with only one AP subject on the login page
        self.actionwords.a_student_with_only_one_ap_subject_on_the_login_page(datatable = "||", free_text = "")
        # When the student enters the correct credentials and clicks on the Sign In button
        self.actionwords.the_student_enters_the_correct_credentials_and_clicks_on_the_sign_in_button()
        # Then he logs in and lands on the Homepage and sees his subject
        self.actionwords.he_logs_in_and_lands_on_the_homepage_and_sees_his_subject()

    def test_smoke__as_a_student_i_want_to_log_out_of_the_application_uid4b7abe30b3634501ab2401f90d15a1fa(self):
        # Tags: priority_P0 test_case_level_Smoke JIRA:FY-3659
        # Given a user logged in the application (APC)
        self.actionwords.a_user_logged_in_the_application_apc()
        # When the user logs out of the application
        self.actionwords.the_user_logs_out_of_the_application()
        # Then the user is logged out
        self.actionwords.the_user_is_logged_out()
        # And redirected to the ROS login page
        self.actionwords.redirected_to_the_ros_login_page()

    def test_smoke__student_assessments_assignments_tab__begin_button_for_opened_assignments_uida6950bfa223c4fd594daf862fdf01557(self):
        # Tags: priority_P1 test_case_level_Functional_GUI JIRA:CB-1789 JIRA:FY-4279
        # Given a teacher opened an assignment to students
        self.actionwords.a_teacher_opened_an_assignment_to_students()
        # When a student goes to Assignments tab form Assessment page
        self.actionwords.a_student_goes_to_assignments_tab_form_assessment_page()
        # Then he sees the assignment having "Opened" status
        self.actionwords.he_sees_the_assignment_having_opened_status(opened = "Opened")
        # And in the Action column a Begin button is available for the opened assignment
        self.actionwords.in_the_action_column_a_begin_button_is_available_for_the_opened_assignment()

    def smoke__student_assessments_assign_tab__start_an_assignment(self, place):
        # Tags: priority_P1 test_case_level_Functional JIRA:FY-4279
        # Given a student on Assignments tab from Assessments
        self.actionwords.a_student_on_assignments_tab_from_assessments()
        # When student clicks on "<place>"
        self.actionwords.student_clicks_on_p1(p1 = place)
        # Then the quiz player is displayed
        self.actionwords.the_quiz_player_is_displayed()

    def test_Smoke__Student_Assessments_Assign_tab__start_an_assignment__uida6f71b127f4c4a959e47f16995634d0a(self):
        self.smoke__student_assessments_assign_tab__start_an_assignment(place = 'title')

    def test_Smoke__Student_Assessments_Assign_tab__start_an_assignment__uidcd3a9927853b4a88a634948382c04a80(self):
        self.smoke__student_assessments_assign_tab__start_an_assignment(place = 'Begin button')

    def test_Smoke__Student_Assessments_Assign_tab__start_an_assignment__uid3ebeb37f7b544f6a90c3addf48b2fcc1(self):
        self.smoke__student_assessments_assign_tab__start_an_assignment(place = 'Continue button')



    def test_smoke__student__save_and_exit_popup_yes_button_uid297f85c25e4d416c95971dbcac4907e7(self):
        # Tags: JIRA:FY-5620 priority_P1 test_case_level_Functional
        # Given a student on the 'Save and Exit' popup for exiting a quiz
        self.actionwords.a_student_on_the_save_and_exit_popup_for_exiting_a_quiz()
        # When he clicks on the Yes button
        self.actionwords.he_clicks_on_the_yes_button()
        # Then the popup closes and he is taken back to Assignments tab (URL: .... /assessments/assignments)
        self.actionwords.the_popup_closes_and_he_is_taken_back_to_assignments_tab_url__assessmentsassignments()

    def test_smoke__student__save_and_exit_popup_reopening_a_quiz_after_leaving_it_uidd8a5ed779c6c4dd593cc42df4e1c1e46(self):
        # Tags: JIRA:FY-5620 priority_P1 test_case_level_Functional
        # Given a student has started working on a quiz
        self.actionwords.a_student_has_started_working_on_a_quiz()
        # When he leaves the quiz by clicking on X button and then on Yes
        self.actionwords.he_leaves_the_quiz_by_clicking_on_x_button_and_then_on_yes()
        # And then re-opens the quiz
        self.actionwords.then_reopens_the_quiz()
        # Then the quiz player is re-opened
        self.actionwords.the_quiz_player_is_reopened()
        # And all the work previously done by the student is saved and displayed
        self.actionwords.all_the_work_previously_done_by_the_student_is_saved_and_displayed()

    def test_smoke__student_assessments__submit_answers_uidcf44e521bbac4b678e1b277da3eb26b4(self):
        # Tags: priority_P0 test_case_level_Smoke JIRA:CB-1789
        # Given a student on Assignments tab from Assessments
        self.actionwords.a_student_on_assignments_tab_from_assessments()
        # When student begins a quiz
        self.actionwords.student_begins_a_quiz()
        # And gives answers for all the questions and clicks Submit button
        self.actionwords.gives_answers_for_all_the_questions_and_clicks_submit_button()
        # Then the quiz is submitted
        self.actionwords.the_quiz_is_submitted()
        # And is no longer displayed in Assignments tab
        self.actionwords.is_no_longer_displayed_in_assignments_tab()

    def test_smoke__score_page_and_response_displayed_uid9ff61d6fd23341f88aaf71726fa1c07a(self):
        # Tags: JIRA:FY-6285 test_case_level_Functional test_case_level_Smoke priority_P0
        # Given a teacher on Progress Check -> Progress page -> FRQ assessment
        self.actionwords.a_teacher_on_progress_check__progress_page__frq_assessment()
        # And the assessment was submitted by at least one student
        self.actionwords.the_assessment_was_submitted_by_at_least_one_student()
        # When the teacher clicks on Score button
        self.actionwords.the_teacher_clicks_on_score_button()
        # Then the scoring page is displayed
        self.actionwords.the_scoring_page_is_displayed()
        # And he sees the Response on the left side of the page
        self.actionwords.he_sees_the_response_on_the_left_side_of_the_page()

    def test_smoke__score_page__score_autosave_in_feedback_popup_uid678fb5e9d88a4c36972804db0b5a5e60(self):
        # Tags: test_case_level_Functional JIRA:FY-6370
        # Given a teacher on Progress Check -> Progress page -> FRQ assessment
        self.actionwords.a_teacher_on_progress_check__progress_page__frq_assessment()
        # And he scores an assessment
        self.actionwords.he_scores_an_assessment()
        # When the teacher is adding some student feedback
        self.actionwords.the_teacher_is_adding_some_student_feedback()
        # And he saves the feedback popup
        self.actionwords.he_saves_the_feedback_popup()
        # Then the score is saved automatically displaying a pop-up with timestamp
        self.actionwords.the_score_is_saved_automatically_displaying_a_popup_with_timestamp()
        # And the popup will disappear after 1 second
        self.actionwords.the_popup_will_disappear_after_1_second()

    def test_smoke__score_page__submit_scores_visible_for_student_uide1aa54172db74915a8e7caef8c472c37(self):
        # Tags: test_case_level_Functional JIRA:FY-6370
        # Given a teacher on Progress Check -> Progress page -> FRQ assessment
        self.actionwords.a_teacher_on_progress_check__progress_page__frq_assessment()
        # And he scores an assessment
        self.actionwords.he_scores_an_assessment()
        # When he scores all parts and questions
        self.actionwords.he_scores_all_parts_and_questions()
        # Then he is able to click Submit button
        self.actionwords.he_is_able_to_click_submit_button()

    def smoke__results_tab_student_performance_sub_tab_submitted_frq_assessments(self, place):
        # Tags: JIRA:FY-3209 priority_P1 test_case_level_Functional Regression
        # Given a teacher on "<place>" page -> Results tab
        self.actionwords.a_teacher_on_p1_page__results_tab(p1 = place)
        # When he clicks on a scored FRQ assessment title -> Student Performance sub-tab ->click on a student
        self.actionwords.he_clicks_on_a_scored_frq_assessment_title__student_performance_subtab_click_on_a_student()
        # Then he sees red X for No Credit, yellow circle for Partial Credit, green check for Full Credit, Awaiting Scoring for not scored; for sub-scores of an FRQ, the same but faded slightly
        self.actionwords.he_sees_red_x_for_no_credit_yellow_circle_for_partial_credit_green_check_for_full_credit_awaiting_scoring_for_not_scored_for_subscores_of_an_frq_the_same_but_faded_slightly()

    def test_Smoke__Results_tab_Student_performance_sub_tab_submitted_FRQ_assessments__uidf446223bef184007b059dbda803aad30(self):
        self.smoke__results_tab_student_performance_sub_tab_submitted_frq_assessments(place = 'Unit Assessments')

    def test_Smoke__Results_tab_Student_performance_sub_tab_submitted_FRQ_assessments__uide8a1a03a3aa1425f8c58544f502a714b(self):
        self.smoke__results_tab_student_performance_sub_tab_submitted_frq_assessments(place = 'Question Bank')



    def test_smoke__results_tab_feedback_box_in_student_performance_when_feedback_was_given_from_progress_tab_uid78f0e62103624630bc99db076d706050(self):
        # Tags: JIRA:FY-4159 story_priority_p0 test_case_level_Functional JIRA:FY-4144
        # Given a teacher on the Results page for a specific quiz
        self.actionwords.a_teacher_on_the_results_page_for_a_specific_quiz()
        # When the teacher opens Student Performance for a specific student
        self.actionwords.the_teacher_opens_student_performance_for_a_specific_student()
        # And there is feedback already given for that student from Progress tab
        self.actionwords.there_is_feedback_already_given_for_that_student_from_progress_tab()
        # Then he should see the feedback box with the actual feedback
        self.actionwords.he_should_see_the_feedback_box_with_the_actual_feedback()

    def test_smoke__student_performance_pdf_printing_uid8b59e169c85549248b8d4c96b441ea43(self):
        # Tags: JIRA:FY-924 Regression
        # Given a teacher has class assignments for students
        self.actionwords.a_teacher_has_class_assignments_for_students()
        # And student has completed assignments
        self.actionwords.student_has_completed_assignments()
        # When the teacher is on the Results page for a specific assignment
        self.actionwords.the_teacher_is_on_the_results_page_for_a_specific_assignment()
        # And selects the individual student
        self.actionwords.selects_the_individual_student()
        # Then teacher will be able to generate a PDF for the individual student.
        self.actionwords.teacher_will_be_able_to_generate_a_pdf_for_the_individual_student()

    def smoke__student_assessments__results_page(self, info):
        # Tags: priority_P2 test_case_level_GUI JIRA:CB-1789
        # Given a student on subject Homepage
        self.actionwords.a_student_on_subject_homepage()
        # When clicks on Assessment tab in the navigation menu
        self.actionwords.clicks_on_assessment_tab_in_the_navigation_menu()
        # And clicks on Results tab
        self.actionwords.clicks_on_results_tab()
        # Then the Results page is displayed and the following "<info>" is available
        self.actionwords.the_results_page_is_displayed_and_the_following_p1_is_available(p1 = info)

    def test_Smoke__Student_Assessments__Results_page__uide82e4333f51b4a1db69eaa7adddffd1a(self):
        self.smoke__student_assessments__results_page(info = 'Title')

    def test_Smoke__Student_Assessments__Results_page__uid261bf4d7ac6949efab703ede3f43ed5b(self):
        self.smoke__student_assessments__results_page(info = 'Assigned')

    def test_Smoke__Student_Assessments__Results_page__uid6930fbd864ee46c998ef4eb8e77c31c3(self):
        self.smoke__student_assessments__results_page(info = 'Performance')



    def test_smoke__student_assessments__performance_column_in_results_tab_uidfb7a754b5a8144478c3cd5c72f506a4c(self):
        # Tags: priority_P2 test_case_level_GUI JIRA:CB-1789
        # Given a student on subject homepage
        self.actionwords.a_student_on_subject_homepage()
        # When clicks on Assessment tab in the navigation menu
        self.actionwords.clicks_on_assessment_tab_in_the_navigation_menu()
        # And clicks on Results tab
        self.actionwords.clicks_on_results_tab()
        # Then sees in Performance column the results for each quiz
        self.actionwords.sees_in_performance_column_the_results_for_each_quiz()
        # And is displayed the number of points overall
        self.actionwords.is_displayed_the_number_of_points_overall()

    def test_smoke__student_assessments__specific_quiz_results_page_uid14a832050da944e1b4c7ea144bc31133(self):
        # Tags: priority_P1 test_case_level_GUI JIRA:CB-1789
        # Given a student on Results tab from assessments
        self.actionwords.a_student_on_results_tab_from_assessments()
        # When clicks on a quiz
        self.actionwords.clicks_on_a_quiz()
        # Then The quiz's Results page is displayed
        self.actionwords.the_quizs_results_page_is_displayed()
        # And contains the student performance, the overall points and the list of questions
        self.actionwords.contains_the_student_performance_the_overall_points_and_the_list_of_questions()
        # And next to each question is shown the scored points from the total number of points
        self.actionwords.next_to_each_question_is_shown_the_scored_points_from_the_total_number_of_points()

    def test_student_assessments__specific_question_results_tab_1_copy_uid0699c0587ba949a5a2853f734106cd52(self):
        # Tags: priority_P2 test_case_level_GUI JIRA:CB-1789
        # Given a student on the Results tab from Assessments
        self.actionwords.a_student_on_the_results_tab_from_assessments()
        # When clicks on a quizz
        self.actionwords.clicks_on_a_quizz()
        # And clicks on a question
        self.actionwords.clicks_on_a_question()
        # Then sees the question having the correct answer letter colored in green
        self.actionwords.sees_the_question_having_the_correct_answer_letter_colored_in_green()
        # And a Next button is available to navigate to the next question
        self.actionwords.a_next_button_is_available_to_navigate_to_the_next_question()

    def test_smoke__as_a_teacher_i_want_to_be_able_to_set_an_assignment_to_complete_uida22c15e6ad0e4363b2c01fba0bf560a4(self):
        # Tags: status priority_P1 test_case_level_Functional JIRA:CB-1789
        # Given a teacher on Homepage
        self.actionwords.a_teacher_on_homepage()
        # When teacher navigates to Progress Checks->Progress tab
        self.actionwords.teacher_navigates_to_progress_checks_progress_tab()
        # And clicks on an assignment
        self.actionwords.clicks_on_an_assignment()
        # And clicks on Complete button
        self.actionwords.clicks_on_complete_button()
        # Then the assignment is set to complete
        self.actionwords.the_assignment_is_set_to_complete()
