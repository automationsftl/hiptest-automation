# encoding: UTF-8

from framework.pages.homePage import HomePage
from framework.pages.loginPage import LoginPage
from framework.pages.subjectsPage import SubjectsPage

class Actionwords:
    def __init__(self, webApp):
        self.loginPage = LoginPage(webApp)
        self.homePage = HomePage(webApp)
        self.subjectsPage = SubjectsPage(webApp)

    def clicks_assign_button_for_an_assessment(self):
        #find button
        position = 8
        self.title = self.homePage.get_title()
        self.homePage.click_assign_button()


    def selects_a_class(self):
        #get title from popup
        assert  self.homePage.is_valid_popup(self.title) is True
        #click on checkbox

        #click on unlock toggle



    def clicks_on_assign_button(self):
        #click on update button

    def the_assessmentquiz_is_assigned_to_that_class(self):
        #check for redirect to progress page

    def is_redirected_to_progress_tab(self):
        pass

    def a_teacher_on_homepage(self):
        pass

    def clicks_on_a_question(self):
        pass

    def clicks_on_an_assignment(self):
        pass

    def clicks_on_complete_button(self):
        pass

    def the_assignment_is_set_to_complete(self):
        pass

    def teacher_clicks_submit_button(self):
        self.loginPage.click_login()

    def a_teacher_on_the_login_page(self):
        self.loginPage.go_to()

    def teacher_enters_in_the_login_page_p1_and_p2(self, p1 = "", p2 = ""):
        self.loginPage.enter_username(p1)
        self.loginPage.enter_password(p2)

    def a_student_on_subject_homepage(self):
        pass

    def clicks_on_a_quiz(self):
        pass

    def a_teacher_on_the_results_page_for_a_specific_quiz(self):
        pass

    def sees_the_question_having_the_correct_answer_letter_colored_in_green(self):
        pass

    def he_sees_the_assignment_having_opened_status(self, opened = "Opened"):
        pass

    def in_the_action_column_a_begin_button_is_available_for_the_opened_assignment(self):
        pass

    def a_student_on_assignments_tab_from_assessments(self):
        pass

    def student_clicks_on_p1(self, p1 = "p1"):
        pass

    def clicks_on_assessment_tab_in_the_navigation_menu(self):
        pass

    def clicks_on_results_tab(self):
        pass

    def sees_in_performance_column_the_results_for_each_quiz(self):
        pass

    def is_displayed_the_number_of_points_overall(self):
        pass

    def a_student_on_results_tab_from_assessments(self):
        pass

    def the_quizs_results_page_is_displayed(self):
        pass

    def contains_the_student_performance_the_overall_points_and_the_list_of_questions(self):
        pass

    def next_to_each_question_is_shown_the_scored_points_from_the_total_number_of_points(self):
        pass

    def a_class_is_already_created_for_the_teacher(self):
        pass

    def he_clicks_in_the_widget_header_on_class_name(self):
        pass

    def he_is_redirected_to_my_classes_with_the_associated_class_selected_httpsmyapcollegeboardorgcourse_test_cdsection_apro_section_id(self):
        pass

    def multiple_classes_are_created_for_that_teacher(self):
        pass

    def he_clicks_on_p1_or_p2_arrows_in_the_widget_header(self, p1 = "", p2 = ""):
        pass

    def he_is_able_to_navigate_through_the_classes(self):
        pass

    def logs_in_and_lands_on_the_homepage_and_sees(self, p1 = ""):
        homepage_single_subject = self.homePage.is_homepage() and self.homePage.has_subject(p1)
        subjects_multiple = self.subjectsPage.is_multiple_subjects_page() and self.subjectsPage.has_subject_in_list(p1)

        assert (homepage_single_subject or subjects_multiple) is True

    def a_teacher_opened_an_assignment_to_students(self):
        pass

    def student_begins_a_quiz(self):
        pass

    def gives_answers_for_all_the_questions_and_clicks_submit_button(self):
        pass

    def the_quiz_is_submitted(self):
        pass

    def the_results_page_is_displayed_and_the_following_p1_is_available(self, p1 = ""):
        pass

    def clicks_on_a_quizz(self):
        pass

    def a_student_on_the_results_tab_from_assessments(self):
        pass

    def a_next_button_is_available_to_navigate_to_the_next_question(self):
        pass

    def is_no_longer_displayed_in_assignments_tab(self):
        pass

    def a_user_logged_in_the_application_apc(self):
        pass

    def the_user_logs_out_of_the_application(self):
        pass

    def the_user_is_logged_out(self):
        pass

    def redirected_to_the_ros_login_page(self):
        pass

    def a_teacher_on_the_homepage_of_a_p1_subject(self, p1 = "p1"):
        pass

    def a_teacher_with_multiple_ap_subjects_on_the_login_page(self):
        pass

    def no_pre_ap_subjects(self):
        pass

    def he_lands_on_my_subjects_page_where_he_can_see_the_ap_courses_he_has_access_to_onscreen(self):
        pass

    def the_pre_ap_section_is_not_displayed(self):
        pass

    def he_clicks_on_p1(self, p1 = "", free_text = "", datatable = "||"):
        pass

    def a_student_with_only_one_ap_subject_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def the_student_enters_the_correct_credentials_and_clicks_on_the_sign_in_button(self):
        pass

    def he_logs_in_and_lands_on_the_homepage_and_sees_his_subject(self):
        pass

    def the_teacher_logs_in(self):
        pass

    def a_teacher_on_p1_page__results_tab(self, p1 = "p1"):
        pass

    def he_clicks_on_a_scored_frq_assessment_title__student_performance_subtab_click_on_a_student(self):
        pass

    def he_sees_red_x_for_no_credit_yellow_circle_for_partial_credit_green_check_for_full_credit_awaiting_scoring_for_not_scored_for_subscores_of_an_frq_the_same_but_faded_slightly(self):
        pass

    def a_teacher_has_class_assignments_for_students(self):
        pass

    def student_has_completed_assignments(self):
        pass

    def the_teacher_is_on_the_results_page_for_a_specific_assignment(self):
        pass

    def selects_the_individual_student(self):
        pass

    def teacher_will_be_able_to_generate_a_pdf_for_the_individual_student(self):
        pass

    def the_teacher_opens_student_performance_for_a_specific_student(self):
        pass

    def he_should_see_the_feedback_box_with_the_actual_feedback(self):
        pass

    def there_is_feedback_already_given_for_that_student_from_progress_tab(self):
        pass

    def a_student_goes_to_assignments_tab_form_assessment_page(self):
        pass

    def the_teacher_is_logged_into_the_application(self):
        pass

    def teacher_navigates_to_assign_tab(self):
        pass

    def the_teacher_is_already_in_the_ua_assign_assign_modal_window_quick_assign_section(self):
        pass

    def the_teacher_looks_at_the_unlock_the_assessment_now_toggle(self):
        pass

    def bellow_appears_the_text_your_students_can_begin_the_assessment_immediately_and_will_see_this_assignment_when_they_log_into_ap_classroom(self):
        pass

    def he_sees_on_the_right_side_a_button_for_switching_onoff(self):
        pass

    def he_logs_in_and_navigates_to_the_homepage_of_a_p1_subject(self, p1 = "p1"):
        pass

    def a_teacher_on_the_homepage_of_a_subject(self):
        pass

    def he_clicks_on_a_unit_tab(self):
        pass

    def that_tab_becomes_highlighted_on_white(self):
        pass

    def a_teacher_on_the_login_page_opened_on_p2_using_p3(self, p2 = "p2", p3 = "p3"):
        pass

    def he_clicks_on_p2_resource_under_a_unit_tab_within_units_section(self, p2 = "p3"):
        pass

    def the_following_happens_p3(self, p3 = ""):
        pass

    def clicks_on_a_unit_tab_from_units_section(self):
        pass

    def a_p1_logs_in_and_navigates_to_the_above_subject_homepage(self, p1 = "p1"):
        pass

    def he_sees_a_new_column_containing_skills_associated_to_the_subunits_on_the_left_side(self):
        pass

    def a_unit_tab_has_been_accessed(self):
        # find unit tab
        # save unit text in variable
        # click unit tab
        self.unit_text = self.homePage.select_unit_tab()

    def he_navigate_to_a_different_page_of_the_same_subject(self):
        self.homePage.navigate_to_dashboard()

        assert self.homePage.is_homepage() is False

    def then_returns_to_homepage(self):
        self.homePage.navigate_to_homePage()
        assert self.homePage.is_homepage() is True

    def a_p1_on_the_homepage_of_a_p2_subject_with_units(self, p1 = "p1", p2 = "p2"):
        # login
        self.loginPage.go_to()
        self.loginPage.enter_username("teacher.worldhistory@testschool.org")
        self.loginPage.enter_password("password")
        self.loginPage.click_login()

        # is home page
        assert self.homePage.is_homepage() is True

        self.user = p1

    def he_sees_the_latest_unit_tab_accessed_opened_along_with_its_content(self):
        current_unit_text = self.homePage.get_selected_unit()

        print(current_unit_text)
        print(self.unit_text)

        assert (self.unit_text == current_unit_text) is True

    def he_sees_each_unit_and_its_content_displayed_in_a_tab(self):
        pass

    def a_teacher_on_progress_check__progress_page__frq_assessment(self):
        pass

    def the_assessment_was_submitted_by_at_least_one_student(self):
        pass

    def the_teacher_clicks_on_score_button(self):
        pass

    def the_scoring_page_is_displayed(self):
        pass

    def he_scores_an_assessment(self):
        pass

    def he_sees_the_response_on_the_left_side_of_the_page(self):
        pass

    def the_popup_will_disappear_after_1_second(self):
        pass

    def the_score_is_saved_automatically_displaying_a_popup_with_timestamp(self):
        pass

    def the_teacher_is_adding_some_student_feedback(self):
        pass

    def he_saves_the_feedback_popup(self):
        pass

    def he_scores_all_parts_and_questions(self):
        pass

    def a_student_on_the_save_and_exit_popup_for_exiting_a_quiz(self):
        pass

    def he_clicks_on_the_yes_button(self):
        pass

    def then_reopens_the_quiz(self):
        pass

    def a_student_has_started_working_on_a_quiz(self):
        pass

    def he_leaves_the_quiz_by_clicking_on_x_button_and_then_on_yes(self):
        pass

    def the_quiz_player_is_reopened(self):
        pass

    def all_the_work_previously_done_by_the_student_is_saved_and_displayed(self):
        pass

    def the_popup_closes_and_he_is_taken_back_to_assignments_tab_url__assessmentsassignments(self):
        pass

    def teacher_is_p1_teacher(self, p1 = ""):
        pass

    def he_navigates_to_that_specific_class_in_the_class_widget(self):
        pass

    def by_default_the_first_6_quizzessorting_rules_appliedare_displayed_on_the_screen(self):
        pass

    def the_others_are_hidden(self):
        pass

    def the_teacher_navigates_to_that_specific_class_in_the_class_widget(self):
        pass

    def a_teacher_has_assigned_multiple_p1_to_a_class(self, p1 = ""):
        pass

    def some_of_the_assignments_are_in_progress_and_some_have_already_results(self):
        pass

    def he_sees_first_the_bars_for_results_then_progress_bars(self):
        pass

    def a_teacher_has_assigned_an_mcq_p1only_to_a_class(self, p1 = ""):
        pass

    def less_than_80_of_students_have_submitted_the_quiz(self):
        pass

    def the_quiz_in_p2_state(self, p2 = ""):
        pass

    def _80_of_students_have_p3(self, p3 = "p3"):
        pass

    def he_sees_the_quiz_row_having_a_results_barsecond_column__view_results_buttonthird_column(self):
        pass

    def a_teacher_has_assigned_a_p1_to_a_class(self, p1 = ""):
        pass

    def the_teacher_inspect_the_class_widget_for_the_above_quiz(self):
        pass

    def he_sees_the_quiz_row_having_a_progress_barsecond_column__view_progress_buttonthird_column(self):
        pass

    def there_is_a_p1_quiz_assigned_with_students_in_progress__0(self, p1 = "p1"):
        pass

    def submitted_available_to_score__x__0(self):
        pass

    def he_sees_the_quiz_row_having_a_x_submissions_to_scorebutton_displayed_in_actions_column(self):
        pass

    def a_teacher_has_assigned_more_than_6_quizzes_to_a_class(self):
        pass

    def teacher_lands_on_the_course_homepage_and_sees_p1_in_the_page_header(self, p1 = ""):
        pass

    def teacher_navigates_to_progress_checks_page(self):
        pass

    def the_teacher_is_able_to_see_the_assign_button_for_a_progress_check(self):
        pass

    def a_teacher_on_assign_tab_from_progress_checks_page(self):
        self.loginPage.go_to()
        self.loginPage.enter_username("teacher.worldhistory@testschool.org")
        self.loginPage.enter_password("password")
        self.loginPage.click_login()

        #check if homepage
        #assert is homepage is true
        #go to progress checks paage
        self.homePage.navigate_to_progress_check()
        #check if progress checks page

    def the_quiz_player_is_displayed(self):
        pass

    def he_is_able_to_click_submit_button(self):
        pass

    def teacher_navigates_to_progress_checks_progress_tab(self):
        pass
