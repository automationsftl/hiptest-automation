# encoding: UTF-8

from framework.pages.homePage import HomePage
from framework.pages.loginPage import LoginPage
from framework.pages.subjectsPage import SubjectsPage


class Actionwords:
    def __init__(self, webApp):
        self.loginPage = LoginPage(webApp)
        self.homePage = HomePage(webApp)
        self.subjectsPage = SubjectsPage(webApp)

    def a_teacher_on_the_p1_homepage(self, p1 = ""):
        pass

    def clicks_teaching_and_assessing_from_top_navigation_bar(self):
        pass

    def lands_on_the_p1_specific_professional_learning(self, p1 = ""):
        pass

    def the_top_bar_changes_to_a_fym_top_navigation_bar_view(self):
        pass

    def a_teacher_on_the_teaching_and_assessing_page_for_p1(self, p1 = ""):
        pass

    def clicks_home_button(self):
        pass

    def fym_landing_page_is_displayed(self):
        pass

    def clicks_assessments_tab(self):
        pass

    def assessments_page_content_for_p1_is_displayed(self, p1 = ""):
        pass

    def clicks_question_bank_tab(self):
        pass

    def question_bank_page_content_for_p1_is_displayed(self, p1 = ""):
        pass

    def a_teacher_on_a_subject_homepage(self):
        pass

    def verifies_the_top_navigation_bar(self):
        pass

    def sees_that_the_top_navigation_bar_includes_p1(self, p1 = ""):
        pass

    def teacher_changes_the_subject_from_the_subject_menu_and_selects_another_subject(self):
        pass

    def sees_teaching_and_assessing_page_for_the_selected_subject(self):
        pass

    def teacher_changes_the_subject_from_the_subject_menu_and_selects_p1(self, p1 = ""):
        pass

    def sees_p1_homepage(self, p1 = ""):
        pass

    def a_teacher_on_assign_tab_from_assessment_page(self):
        pass

    def clicks_assign_button_for_an_assessment(self):
        pass

    def a_pop_up_is_displayed_where_teacher_can_choose_a_class_and_configure_the_assessment(self):
        pass

    def in_my_classes_area_form_choose_classes_the_teacher_sees_all_the_classes_that_he_is_enrolled_in_for_the_selected_subject(self):
        pass

    def teacher_is_enrolled_only_in_a_class(self):
        pass

    def in_my_classes_area_form_choose_classes_the_class_is_checked_by_default(self):
        pass

    def clicks_assign_button_for_a_quiz_that_was_already_assigned_to_the_class(self):
        pass

    def in_my_classes_area_form_choose_classes_the_class_is_displayed_as_disabled(self):
        pass

    def an_information_icon_appears_next_to_the_class_name(self):
        pass

    def under_my_classes_area_the_following_message_is_displayed_p1(self, p1 = ""):
        pass

    def does_not_select_a_class(self):
        pass

    def the_assign_button_is_not_displayed(self):
        pass

    def a_select_a_classbutton_is_displayed(self, select_a_class_button = "Select a class button"):
        pass

    def selected_classes_area_is_empty(self):
        pass

    def selects_a_class(self):
        pass

    def in_the_selected_classes_area_the_selected_class_name_is_displayed(self):
        pass

    def next_to_the_class_name_a_delete_button_is_available(self):
        pass

    def clicks_on_delete_button_next_to_a_class_in_selected_classes_area(self):
        pass

    def the_class_is_not_displayed_anymore_in_selected_classes_area(self):
        pass

    def the_class_becomes_unchecked_in_my_classes_area(self):
        pass

    def selects_a_more_classes(self):
        pass

    def clicks_to_uncheck_one_of_the_selected_classes(self):
        pass

    def the_rest_of_the_selected_classes_remain_checked(self):
        pass

    def the_select_a_class_button_becomes_assign_button(self):
        pass

    def the_teacher_is_able_to_click_the_assign_button(self):
        pass

    def in_configure_area_the_teacher_is_able_to_enter_a_title_in_student_visible_title_field(self, student_visible_title = "Student visible title"):
        pass

    def in_configure_area_the_teacher_is_able_to_switch_the_toggle_on_for_p1_option(self, p1 = ""):
        pass

    def in_configure_area_switches_the_toggle_on_for_p1_option(self, p1 = ""):
        pass

    def the_teacher_is_able_to_switch_the_toggle_off_for_p1_option(self, p1 = ""):
        pass

    def in_configure_area_switches_the_toggle_on_for_p1_option(self, p1 = ""):
        pass

    def clicks_on_assign_button(self):
        pass

    def the_assessmentquiz_is_assigned_to_that_class(self):
        pass

    def is_redirected_to_progress_tab(self):
        pass

    def a_teacher_having_for_subject_both_assessment_and_question_bank(self):
        pass

    def teacher_creates_a_class_in_my_classes(self):
        pass

    def teacher_goes_to_question_bank(self):
        pass

    def the_class_appears_in_question_bank_my_classes_list(self):
        pass

    def teacher_creates_a_class_in_my_classes_page(self):
        pass

    def teacher_goes_to_assessments_page(self):
        pass

    def the_class_appears_in_assessments_my_classes_list(self):
        pass

    def teacher_creates_a_class_in_my_classes_page(self):
        pass

    def teacher_goes_to_assessments_assign_tab(self):
        pass

    def clicks_on_assign_button_next_to_a_quiz(self):
        pass

    def the_assessment_is_assigned_to_the_created_class(self):
        pass

    def teacher_creates_a_class_in_my_classes(self):
        pass

    def teacher_goes_to_question_bank_assign_tab(self):
        pass

    def teacher_goes_to_assign_tab_from_question_bank(self):
        pass

    def goes_to_assign_tab_from_assessments(self):
        pass

    def a_teacher_on_homepage(self):
        pass

    def clicks_teacher_module_tab(self):
        pass

    def the_teacher_module_page_is_displayed(self):
        pass

    def the_last_expanded_teacher_module_modules_are_remembered_and_the_outline_is_expanded(self):
        pass

    def the_outline_is_collapsed(self):
        pass

    def a_teacher_on_units_page(self):
        pass

    def clicks_teacher_module_link_within_a_unit(self):
        pass

    def the_outline_expands_the_teacher_module_module_associated_with_the_unit(self):
        pass

    def sees_that_the_unit_has_only_one_taa_module_associated_with_it(self):
        pass

    def a_teacher_on_teacher_module_page(self):
        pass

    def clicks_on_a_module_to_expand_it(self):
        pass

    def sees_that_a_teacher_module_can_be_associated_with_more_than_one_unit(self):
        pass

    def a_teacher_on_assessments_results_page(self):
        pass

    def clicks_on_a_quiz_in_class_performance_tab(self):
        pass

    def clicks_on_a_question(self):
        pass

    def khan_academy_resources_are_displayed_on_the_right_side_of_the_page(self):
        pass

    def the_resource_assignment_is_based_on_skills_practice_and_focus_block(self):
        pass

    def clicks_student_performance_tab(self):
        pass

    def clicks_on_a_student(self):
        pass

    def a_teacher_on_question_bank_results_page(self):
        pass

    def a_teacher_on_teaching__assessing_page(self):
        pass

    def clicks_on_historical_periods_tab(self):
        pass

    def clicks_on_resources_button_for_a_module(self):
        pass

    def sees_a_pop_up_containing_the_links_to_the_taa_resources(self):
        pass

    def expands_a_module(self):
        pass

    def clicks_on_resources_button_for_a_unit(self):
        pass

    def sees_a_pop_up_containing_the_link_to_the_taa_resource(self):
        pass

    def clicks_on_mastering_scoring_guideline_tab(self):
        pass

    def a_student_on_assessments_results_page(self):
        pass

    def clicks_on_a_quiz_in_your_performance_tab(self):
        pass

    def a_student_on_question_bank_results_page(self):
        pass

    def clicks_on_resources_tab(self):
        pass

    def sees_the_resources_corresponding_to_the_test(self):
        pass

    def a_teacher_on_the_homepage(self):
        pass

    def he_navigates_to_question_bank(self):
        pass

    def he_is_able_to_see_only_the_following_p1(self, p1 = ""):
        pass

    def a_us_history_teacher_on_the_homepage(self):
        pass

    def a_calculus_teacher_on_the_homepage(self):
        pass

    def a_biology_teacher_on_the_homepage(self):
        pass

    def he_navigates_to_question_bank_create_assign_progress_results_tab(self):
        pass

    def a_wh_teacher_on_the_homepage(self):
        pass

    def he_navigates_to_question_bank_create_tab(self):
        pass

    def he_is_able_to_see_among_filters_practices_skills_and_units(self):
        pass

    def clicks_on_practices_filter(self):
        pass

    def he_is_able_to_see_practices_as_parent_in_the_filter(self):
        pass

    def he_is_able_to_see_under_parent_its_children_and_grandchildren(self):
        pass

    def clicks_on_skills_filter(self):
        pass

    def clicks_on_units_filter(self):
        pass

    def he_is_able_to_see_units_as_parent_in_the_filter(self):
        pass

    def a_list_of_mc_and_fr_published_questions(self):
        pass

    def some_of_them_have_combinations_of_the_3_metadata(self):
        pass

    def teacher_is_in_the_question_bank_create_tab(self):
        pass

    def he_filters_the_qb_items_by_the_parent_skill_orand_by_the_parent_practice_orand_by_the_parent_unit(self):
        pass

    def the_list_is_filtered_properly_and_only_the_items_that_match_all_the_filters_are_listed(self):
        pass

    def a_list_of_mc_and_fr_draft_questions(self):
        pass

    def a_list_of_mc_and_fr_publisheddraft_questions(self):
        pass

    def some_of_them_have_skills_as_metadata_some_practices_some_units_and_combinations(self):
        pass

    def for_some_of_them_their_skills_practices_and_units_are_removed_and_saved(self):
        pass

    def he_filters_the_qb_items_by_the_skills_orand_practices_orand_units_that_were_removed(self):
        pass

    def the_list_is_filtered_properly_and_those_items_are_not_listed_anymore(self):
        pass

    def a_teacher_on_question_bank_tab(self):
        pass

    def clicks_on_manage_classes_tab(self):
        pass

    def sees_on_the_left_side_of_the_page_under_my_classes_label_all_his_classes(self):
        pass

    def a_teacher_on_manage_classes_tab_from_question_bank(self):
        pass

    def chooses_a_school_from_school_dropdown_list_under_add_class_section(self):
        pass

    def clicks_on_create_button(self):
        pass

    def the_class_is_created(self):
        pass

    def appears_unde_my_classes_list(self):
        pass

    def teacher_creates_a_class(self):
        pass

    def under_students_with_accounts_label_sees_the_link_for_students_access(self):
        pass

    def under_firsttime_student_acess_label_sees_the_registration_link_for_students_and_join_code(self):
        pass

    def clicks_on_teacher_button_in_choose_a_role_popup(self):
        pass

    def selected_member_is_enrolled_as_a_teacher_in_the_created_class(self):
        pass

    def is_displayed_on_the_list_as_anrolled_members_as_teacher(self):
        pass

    def clicks_on_supervisor_button_in_choose_a_role_popup(self):
        pass

    def selected_member_is_enrolled_as_a_supervisor_in_the_created_class(self):
        pass

    def is_displayed_on_the_list_as_anrolled_members_as_supervisor(self):
        pass

    def clicks_on_student_button_in_choose_a_role_popup(self):
        pass

    def selected_member_is_enrolled_as_a_student_in_the_created_class(self):
        pass

    def is_displayed_on_the_list_as_anrolled_members_as_student(self):
        pass

    def chooses_fron_subject_dropdown_another_subject_for_the_selected_class(self):
        pass

    def the_class_subject_changes_accordingly(self):
        pass

    def switches_the_toggle_button_from_active_to_archived(self):
        pass

    def the_selected_class_gets_archived(self):
        pass

    def selects_no_option_in_the_active_dropdown(self):
        pass

    def the_system_returns_all_inactive_users_containing_the_entered_name(self):
        pass

    def navigates_to_question_bank_progress_tab(self):
        pass

    def the_teacher_is_able_to_select_a_class_or_all_classes_to_view_the_progress_for_assignments(self):
        pass

    def the_progress_for_that_specific_class_assignments_is_displayed_with_the_following_p1(self, p1 = ""):
        pass

    def to_filter_the_assignments_by_p1(self, p1 = ""):
        pass

    def in_the_progress_column_is_displayed_the_progress_for_each_assignment(self):
        pass

    def there_are_unopenedlocked_assignments(self):
        pass

    def sees_that_in_the_progress_column_the_unopened_assessments_are_marked_as_locked(self):
        pass

    def there_are_opened_assignments_but_the_students_didnt_begin_the_assignment(self):
        pass

    def sees_that_in_the_progress_column_the_not_started_assessments_are_marked_as_not_started(self):
        pass

    def there_are_assignments_that_students_started_but_not_finished_yet(self):
        pass

    def a_teacher_clicks_its_default_quiz_from_the_list_of_quizzes(self):
        pass

    def the_green_color_represents_the_percent_of_how_much_of_the_assignment_is_complete_and_the_grey_color_represents_the_percent_of_how_much_is_left_for_the_assignment_to_be_finished(self):
        pass

    def sees_that_in_the_progress_column_for_the_started_assignments_is_displayed_a_grey_progress_bar(self):
        pass

    def there_are_assignments_completed_by_students(self):
        pass

    def sees_that_in_the_progress_column_the_finished_assignments_are_marked_as_complete(self):
        pass

    def teacher_navigates_to_question_bank_progress_tab(self):
        pass

    def clicks_view_progress_button_in_action_column_for_an_assignment_started_by_the_student(self):
        pass

    def the_progress_page_for_that_specific_assignment_is_displayed(self):
        pass

    def the_teaches_see_an_overview_of_the_assignments_progress_such_as_student_progress_scoring_progress_student_access(self):
        pass

    def also_sees_a_student_list_with_the_status_of_the_assignment_for_every_student(self):
        pass

    def sees_the_student_progress_section_where_is_displayed_the_number_of_submitted_questions_by_the_students_and_also_the_number_of_in_progress_questions(self):
        pass

    def clicks_view_progress_button_in_action_column_for_an_assignment(self):
        pass

    def sees_the_scoring_progress_section_where_is_displayed_the_number_of_entered_and_available_scores(self):
        pass

    def clicks_open_assessment_button_in_action_column_for_a_locked_assignment(self):
        pass

    def then_in_student_access_section_switches_on_the_assignment_toggle_button(self):
        pass

    def the_assignment_is_opened_to_students(self):
        pass

    def the_students_can_begin_or_start_the_assignment(self):
        pass

    def clicks_on_an_assignment_that_is_not_enabled_to_show_scores_to_students(self):
        pass

    def then_in_student_access_section_switches_on_the_results_toggle_button(self):
        pass

    def the_assignment_is_enabled_to_show_scores_to_students(self):
        pass

    def the_students_will_see_the_results_as_they_are_available(self):
        pass

    def clicks_on_an_assignment(self):
        pass

    def clicks_on_delete_button(self):
        pass

    def a_confirmation_popup_is_displayed(self):
        pass

    def the_confirmation_message_says_p1(self, p1 = ""):
        pass

    def clicks_yes_in_the_confirmation_popup(self):
        pass

    def the_assignment_and_all_student_data_associated_with_it_is_deleted(self):
        pass

    def clicks_no_in_the_confirmation_popup(self):
        pass

    def the_delete_action_is_canceled(self):
        pass

    def clicks_on_complete_button(self):
        pass

    def the_assignment_is_set_to_complete(self):
        pass

    def clicks_on_a_closed_assignment(self):
        pass

    def clicks_on_reopen_button(self):
        pass

    def the_assignment_reopened_to_students(self):
        pass

    def clicks_on_enter_scores(self):
        pass

    def the_teacher_can_enter_the_scores_for_every_student_that_submitted_the_answers_for_the_quiz(self):
        pass

    def teacher_navigates_to_question_bank_progress_tabspecific_assignmet_enter_scores_tab(self):
        pass

    def for_a_student_inserts_scores_for_every_question_or_part_of_the_quiz_in_their_specific_column(self):
        pass

    def in_the_total_point_column_for_the_current_user_is_displayed_the_sum_of_the_scores_entered_by_the_teacher(self):
        pass

    def teacher_navigates_to_question_bank_progress_tabspecific_assignment_enter_scores_tab(self):
        pass

    def try_to_insert_a_value_different_that_0_or_1_for_free_text_questions(self):
        pass

    def a_popup_with_the_following_message_is_displayed_p1(self, p1 = ""):
        pass

    def try_to_insert_a_value_different_that_a_b_c_d_or__for_multiple_choice_questions(self):
        pass

    def enter_scores_for_some_or_all_students(self):
        pass

    def clicks_save_scores_button(self):
        pass

    def the_entered_scores_are_saved(self):
        pass

    def navigates_to_question_bank_results_tab(self):
        pass

    def the_teacher_is_able_to_select_a_class_or_all_classes_to_view_the_results_for(self):
        pass

    def the_results_for_that_specific_class_assignments_are_displayed_with_the_following_p1(self, p1 = ""):
        pass

    def a_student_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def student_enters_in_the_login_page_username_and_password(self, username = "", password = ""):
        pass

    def student_clicks_hide_transcript_button(self):
        pass

    def logs_in_and_lands_on_the_homepage_and_sees_p1_subject(self, p1 = ""):
        pass

    def a_student_on_homepage(self):
        pass

    def student_has_p1(self, p1 = ""):
        pass

    def unit_widget_is_displayed_on_homepage(self):
        pass

    def unit_widget_is_not_displayed_on_homepage(self):
        pass

    def student_have_multiple_subjects(self):
        pass

    def clicks_to_expand_the_subjects_menu(self):
        pass

    def the_student_is_able_to_see_his_subjects(self):
        pass

    def student_clicks_to_expand_the_subjects_menu(self):
        pass

    def clicks_on_p1(self, p1 = ""):
        pass

    def the_student_lands_on_p1_homepage(self, p1 = ""):
        pass

    def trying_to_login_with_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def a_student_on_the_class_enrollment_page(self):
        pass

    def student_fills_in_the_join_code_the_email_address_and_password(self):
        pass

    def student_clicks_enroll_button(self):
        pass

    def student_fills_in_a_wrong_join_code_the_email_address_and_password(self):
        pass

    def an_error_message_regarding_the_invalid_join_code_is_thrown_and_the_enroll_button_is_inactive(self):
        pass

    def the_list_of_student_users(self, datatable = ""):
        pass

    def trying_to_enroll_with_correct_join_code_and_with_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def enroll_in_button_is_disabled_and_the_following_p1_should_be_thrown(self, p1 = ""):
        pass

    def clicks_show_transcript_button(self):
        pass

    def student_fills_in_the_join_code_and_the_rest_of_the_required_fields(self):
        pass

    def student_clicks_create_account_button(self):
        pass

    def logs_in_the_created_account_and_sees_the_class_subject(self):
        pass

    def an_error_message_regarding_the_invalid_join_code_is_thrown(self):
        pass

    def the_create_account_button_is_inactive(self):
        pass

    def provides_for_password_and_repeat_password_different_values(self):
        pass

    def an_error_message_regarding_the_passwords_match_is_thrown(self):
        pass

    def provides_an_email_addres_that_is_already_in_use(self):
        pass

    def an_error_message_regarding_the_fact_that_the_email_is_already_used_is_thrown(self):
        pass

    def student_checks_i_dont_have_an_email_address_option_and_fills_the_rest_of_the_required_fields(self):
        pass

    def a_world_history_teacher_on_the_login_page(self):
        pass

    def teacher_fills_in_the_username_and_password(self):
        pass

    def teacher_clicks_submit_button(self):
        self.loginPage.click_login()

    def teacher_logs_in_and_lands_on_the_homepage(self):
        pass

    def a_calculus_teacher_on_the_login_page(self):
        pass

    def a_teacher_on_the_login_page(self):
        self.loginPage.go_to()


    def teacher_enters_in_the_login_page_p1_and_p2(self, p1 = "", p2 = ""):
        self.loginPage.enter_username(p1)
        self.loginPage.enter_password(p2)

    def the_teacher_is_on_the_corresponding_home_page(self):
        pass

    def teacher_clicks_to_expand_the_subjects_menu(self):
        pass

    def p1_is_able_to_see_his_p2(self, p1 = "", p2 = ""):
        pass

    def the_list_of_allowed_teacher_users(self, datatable = ""):
        pass

    def the_following_p1_should_be_thrown(self, p1 = ""):
        pass

    def teacher_clicks_on_p1_hyperlink(self, p1 = ""):
        pass

    def he_is_redirected_to_the_site_terms_and_conditions_page(self):
        pass

    def he_is_redirected_to_the_our_commitment_to_your_privacy_page(self):
        pass

    def teacher_clicks_on_p1(self, p1 = ""):
        pass

    def it_should_be_able_to_recover_its_password_via_email(self):
        pass

    def a_fym_teacher_on_the_login_page(self):
        pass

    def he_logs_in_with_the_correct_credentials(self):
        pass

    def he_lands_on_his_fym_subject_homepage(self):
        pass

    def he_sees_the_fym_homepage_header_corresponding_to_his_subject(self):
        pass

    def a_fym_teacher_on_his_fym_subject_homepage(self):
        pass

    def he_accesses_resources_by_navigating_to_teacher_modules_page(self):
        pass

    def he_sees_the_resources_available_for_his_subject(self):
        pass

    def a_non_pilot_teacher_on_the_login_page(self):
        pass

    def a_nonpilot_teacher_on_his_fym_subject_homepage(self):
        pass

    def he_accesses_resources_by_navigating_to_unit_assessments_page(self):
        pass

    def he_sees_the_quizzes_available_for_his_subject(self):
        pass

    def a_nonpilot_biology_teacher_on_the_login_page(self):
        pass

    def he_sees_unit_assessments_only_in_the_header_menu(self):
        pass

    def the_subject_is_shown_in_the_subject_dropdown(self):
        pass

    def a_nonpilot_chemistry_teacher_on_the_login_page(self):
        pass

    def a_nonpilot_whc_teacher_on_the_login_page(self):
        pass

    def he_sees_only_teacher_modules_and_unit_assessments_in_the_header_menu(self):
        pass

    def a_nonpilot_computer_science_teacher_on_the_login_page(self):
        pass

    def he_sees_only_teacher_modules_in_the_header_menu(self):
        pass

    def a_whc_teacher_on_the_login_page(self):
        pass

    def he_sees_units_teacher_module_unit_assessments_and_question_bank_in_the_header_menu(self):
        pass

    def he_sees_only_teacher_modules_and_question_bank_in_the_header_menu(self):
        pass

    def he_navigates_to_question_bank_assign_tab(self):
        pass

    def a_list_of_quizzes_that_have_mc_and_fr_published_questions_included(self):
        pass

    def some_of_the_quiz_questions_have_skills_as_metadata_some_practices_some_units(self):
        pass

    def teacher_is_in_the_question_bank_assign_tab(self):
        pass

    def he_filters_the_quizzes_by_the_parent_skill_orand_by_the_parent_practice_orand_by_the_parent_unit(self):
        pass

    def the_quizzes_list_is_filtered_properly_and_only_the_items_that_match_all_the_filters_are_listed(self):
        pass

    def a_list_of_quizzes_that_have_mc_and_fr_draft_questions_included(self):
        pass

    def he_clicks_on_each_p1(self, p1 = ""):
        pass

    def he_is_able_to_see_other_p1(self, p1 = ""):
        pass

    def an_admin_on_the_homepage(self):
        pass

    def a_wh_teacher_on_the_question_bank_page(self):
        pass

    def he_clicks_author_new_question(self):
        pass

    def he_chooses_multiple_choice(self):
        pass

    def he_navigates_to_specify_metadata(self):
        pass

    def he_is_able_to_see_skills_practices_and_units_metadata(self):
        pass

    def he_is_in_mc_create_form_specify_metadata_tab(self):
        pass

    def he_clicks_on_skills(self):
        pass

    def he_is_able_to_assign_skills_metadata_to_the_item(self):
        pass

    def he_enters_data_in_all_mandatory_fields(self):
        pass

    def he_assigns_skills_metdata_to_the_item(self):
        pass

    def the_item_is_published_successfully(self):
        pass

    def he_clicks_on_practices(self):
        pass

    def he_is_able_to_assign_practices_metadata_to_the_item(self):
        pass

    def he_assigns_practices_metadata_to_the_item(self):
        pass

    def he_clicks_on_units(self):
        pass

    def he_is_able_to_assign_units_metadata_to_the_item(self):
        pass

    def he_assigns_units_metadata_to_the_item(self):
        pass

    def he_is_editing_an_existing_mc_question(self):
        pass

    def he_clicks_on_practices_skills_and_units_in_specify_metadata_tab(self):
        pass

    def he_is_able_to_assign_practices_skills_and_units_metadata_to_the_item(self):
        pass

    def he_is_in_fr_create_form_specify_metadata_tab(self):
        pass

    def he_is_editing_an_existing_fr_question(self):
        pass

    def the_show_transcript_button_was_clicked(self):
        pass

    def on_homepage_is_displayed_a_to_do_card_for_every_assignment(self):
        pass

    def student_have_assigned_and_opened_tests_but_not_started(self):
        pass

    def checks_the_todo_widgets_list(self):
        pass

    def sees_a_widget_with_headline_p1_the_begin_date_and_the_link_to_the_assignment(self, p1 = ""):
        pass

    def student_have_assignments_in_progress_not_yet_finished(self):
        pass

    def sees_a_widget_with_headline_p1_the_finish_date_and_the_link_to_the_assignment(self, p1 = ""):
        pass

    def student_finishes_an_assignment(self):
        pass

    def the_finished_assignment_is_not_displayed_in_the_to_do_widget_section(self):
        pass

    def sees_a_widget_with_headline_p1_the_date_and_the_link_to_the_quiz(self, p1 = ""):
        pass

    def sees_a_widget_with_headline_p1_the_date_and_the_link_to_the_score_enter_area_of_the_quiz(self, p1 = ""):
        pass

    def the_action_is_logged(self):
        pass

    def the_tracked_information_includes_user_identifier_timestamp_resource_identifier_and_from_where_the_link_was_clicked(self):
        pass

    def a_teacher_on_unit_assessments_results_page(self):
        pass

    def navigates_to_results__test__resource_tab(self):
        pass

    def navigates_to_results__test__question_page_tab(self):
        pass

    def a_teacher_on_question_bank_results_page(self):
        pass

    def a_teacher_on_question_bank_results_page(self):
        pass

    def a_whc_teacher_is_on_homepage(self):
        pass

    def he_clicks_on_the_units_unit_tests_link_under_assessments(self):
        pass

    def he_is_redirected_to_the_assessments_page_with_assign_tab_opened(self):
        pass

    def he_clicks_on_the_units_unit_tests_link_from_units_widget(self):
        pass

    def the_unit_filter_is_set_to_the_corresponding_unit(self):
        pass

    def teacher_can_see_the_assets_associated_with_the_unit(self):
        pass

    def a_whc_teacher_is_on_units_page(self):
        pass

    def he_clicks_on_the_units_unit_test_link_under_assessments(self):
        pass

    def he_clicks_on_the_units_question_bank_link_under_assessments(self):
        pass

    def he_is_redirected_to_the_question_bank_page_page_with_create_tab_opened(self):
        pass

    def teacher_can_see_the_questions_associated_with_the_unit(self):
        pass

    def the_unit_has_quizzes_associated(self):
        pass

    def he_clicks_on_the_units_quiz_link_in_resources(self):
        pass

    def he_is_redirected_to_the_assessments_page_page_with_assign_tab_opened(self):
        pass

    def the_building_blocks_filter_is_set_to_the_corresponding_building_block(self):
        pass

    def teacher_can_see_the_assets_associated_with_the_unit_and_building_block(self):
        pass

    def he_logs_in_the_application_with_correct_credentials(self):
        pass

    def he_is_able_to_see_the_unit_widget(self):
        pass

    def he_is_able_to_see_the_unit_number_in_the_widget(self):
        pass

    def he_sees_unit_guide_hiperlink_under_unit_title(self):
        pass

    def he_sees_teacher_module_khan_academy_unit_tests_question_bank_under_unit_resources_section(self):
        pass

    def he_sees_the_list_of_building_blocks_under_unit_blocks_section_without_their_resources(self):
        pass

    def p1_button_is_available_at_the_bottom_of_the_widget(self, p1 = ""):
        pass

    def a_whc_teacher_is_on_the_homepage(self):
        pass

    def he_clicks_on_unit_guide_in_the_unit_widget(self):
        pass

    def unit_guide_pdf_file_associated_with_the_unit_loads_in_a_new_browser_tab_as_defined_in_the_resources_sheet_of_the_metadata_google_doc(self):
        pass

    def he_clicks_on_khan_academy_from_unit_resources_in_the_unit_widget(self):
        pass

    def user_is_redirected_to_khan_academy_unit_page_associated_with_the_unit_in_a_new_browser_tab_as_defined_in_the_fym_resources_sheet_of_the_metadata_google_doc(self):
        pass

    def specific_khan_resources_are_loaded(self):
        pass

    def he_clicks_on_teacher_module_from_unit_resources_in_the_unit_widget(self):
        pass

    def the_teacher_is_redirected_to_teacher_modules_section_as_defined_in_the_fym_taa_sheet_of_the_metadata_google_doc(self):
        pass

    def specific_teaching_module_is_expanded_to_show_its_content(self):
        pass

    def he_clicks_on_question_bank_from_unit_resources(self):
        pass

    def the_teacher_is_redirected_to_question_bank_page(self):
        pass

    def specific_questiontest_is_displayed_in_the_question_bank_create_section(self):
        pass

    def he_clicks_on_the_right_or_left_arrow_on_the_topright_corner_of_the_screen(self):
        pass

    def the_widget_shows_the_content_for_the_next_unit(self):
        pass

    def he_clicks_on_the_unit_number_unit_name_header_on_the_unit_widget(self):
        pass

    def he_is_redirected_to_units_page(self):
        pass

    def the_unit_section_opens_with_that_unit_expanded(self):
        pass

    def he_clicks_on_the_p1(self, p1 = ""):
        pass

    def all_the_blocks_are_listed(self):
        pass

    def a_whc_teacher_is_on_the_units_page(self):
        pass

    def he_clicks_to_expand_a_unit(self):
        pass

    def he_go_back_to_the_homepage(self):
        pass

    def he_sees_in_the_widget_the_expanded_unit(self):
        pass

    def a_whc_teacher_is_on_the_homepage(self):
        pass

    def he_clicks_a_block_in_the_unit_widget(self):
        pass

    def teacher_is_redirected_to_units_page_with_he_page_anchored_to_the_selected_block(self):
        pass

    def a_whc_teacher_is_on_the_login_page(self):
        pass

    def he_logs_in_the_app_for_the_first_time(self):
        pass

    def he_sees_the_first_unit_from_the_list_displayed_in_the_widget(self):
        pass

    def he_clicks_on_the_units_tab(self):
        pass

    def he_is_able_to_view_all_units_and_resources_for_each_unit_when_expanding_them(self):
        pass

    def the_accordion_drawers_should_all_be_collapsed(self):
        pass

    def he_is_able_to_view_teachers_guide_to_the_units_expand_all_collapse_all(self):
        pass

    def filters_practice__skills_themes__learning_objectives_periods_resource_type_should_appear_in_the_left_side_of_the_page(self):
        pass

    def he_clicks_on_the_arrow_to_expand_the_unit(self):
        pass

    def a_unit_contains_unit_guide(self):
        pass

    def instruction__practice_group_contains_teaching__assessing_khan_academy(self):
        pass

    def assessments_group_contains_unit_tests_question_bank(self):
        pass

    def all_the_unit_building_blocks_are_listed_with_their_resources_in_their_right_side(self):
        pass

    def check_the_resources_for_a_building_block(self):
        pass

    def he_is_able_to_see_combination_of_resources_teacher_lesson_plan_student_lesson_plan_khan_academy_quiz(self):
        pass

    def he_clicks_on_teachers_guide_to_the_units(self):
        pass

    def teachers_guide_to_the_units_pdf_file_should_load_in_a_new_browser_page(self):
        pass

    def he_clicks_on_expand_all(self):
        pass

    def all_drawers_should_be_expanded(self):
        pass

    def he_expanded_all_units(self):
        pass

    def he_clicks_on_collapse_all(self):
        pass

    def all_drawers_should_be_collapsed_with_only_the_unit_names_exposed(self):
        pass

    def an_unit_is_expanded(self):
        pass

    def he_clicks_on_unit_guide(self):
        pass

    def unit_guide_pdf_file_loads_in_a_new_browser_tab(self):
        pass

    def he_clicks_on_khan_academy_from_unit_resources(self):
        pass

    def user_is_redirected_to_khan_academy_website_in_a_new_browser_tab(self):
        pass

    def he_clicks_on_teacher_module_from_unit_resources(self):
        pass

    def the_teacher_is_redirected_to_teacher_modules_section(self):
        pass

    def specific_teaching_module_is_displayed(self):
        pass

    def he_clicks_on_unit_test_from_unit_resources(self):
        pass

    def the_teacher_is_redirected_to_unit_assessments_page_assign_tab(self):
        pass

    def specific_questiontest_is_displayed_in_the_list(self):
        pass

    def filters_set_to_unitp1_and_resource_type__p2(self, p1 = "", p2 = ""):
        pass

    def filters_set_to_unitp1(self, p1 = ""):
        pass

    def there_is_a_bb_that_has_a_teacher_lesson_plan_as_resource(self):
        pass

    def he_clicks_on_teacher_lesson_plan(self):
        pass

    def teacher_lesson_plan_pdf_loads_in_a_new_browser_tab(self):
        pass

    def there_is_a_bb_that_has_a_student_lesson_plan_as_resource(self):
        pass

    def student_lesson_plan_pdf_loads_in_a_new_browser_tab(self):
        pass

    def there_is_a_bb_that_has_a_khan_academy_as_resource(self):
        pass

    def he_clicks_on_khan_academy_for_a_block(self):
        pass

    def khan_academy_pdf_file_loads_in_a_new_browser_tab(self):
        pass

    def there_is_a_bb_that_has_a_quiz_as_resource(self):
        pass

    def he_clicks_on_quiz(self):
        pass

    def the_user_is_redirected_to_assessment_tab_assign_tab(self):
        pass

    def specific_questiontest_is_listed(self):
        pass

    def the_filters_are_set_to_unitp1_and_bb_p2(self, p1 = "", p2 = ""):
        pass

    def all_the_units_are_expanded(self):
        pass

    def there_are_bb_that_have_teacher_and_lesson_plans_as_resource(self):
        pass

    def he_filters_by_lesson_plan_resource_type(self):
        pass

    def only_the_units_with_bb_that_have_lesson_plans_assigned_are_displayed_on_the_screen(self):
        pass

    def a_student_on_welcome_video_page(self, datatable = "||", free_text = ""):
        pass

    def the_button_changes_to_show_transcript(self):
        pass

    def viewing_the_welcome_video_using_screenreaders(self):
        pass

    def the_tab_order_for_show_hide_transcript_button_should_be_immediately_adjacent_to_the_video(self):
        pass

    def a_student_on_the_welcome_video__follow_on_questions_page(self):
        pass

    def clicks_on_respond_later_button(self):
        pass

    def the_student_is_brought_to_the_homepage(self):
        pass

    def a_to_do_card_to_respond_to_the_questions_appears_on_their_homepage(self):
        pass

    def student_responds_to_the_questions(self):
        pass

    def clicks_submit_button(self):
        pass

    def the_final_thank_you_page_is_displayed(self):
        pass

    def student_leaves_the_answer_text_fields_empty(self):
        pass

    def submit_button_is_inactive(self):
        pass

    def student_leaves_one_of_the_answer_text_fields_empty(self):
        pass

    def the_submit_button_is_inactive(self):
        pass

    def the_student_fills_in_the_answer_for_both_questions(self):
        pass

    def the_submit_button_become_active(self):
        pass

    def clicks_watch_video_again_button(self):
        pass

    def the_student_goes_back_to_the_welcome_video_page(self):
        pass

    def student_goes_to_welcome_videofollow_on_questions_page(self):
        pass

    def clicks_the_back_button(self):
        pass

    def the_student_goes_back_to_the_welcome_video_screen(self):
        pass

    def he_expands_an_unit(self):
        pass

    def he_clicks_on_teacher_module_link_under_unit_resources_for_that_unit(self):
        pass

    def the_taa_module_associated_with_that_unit_gets_expanded(self):
        pass

    def clicks_on_respond_to_video_questions_to_do_card(self):
        pass

    def in_the_video_questions_page_clicks_on_the_back_button(self):
        pass

    def the_student_is_redirected_to_the_homepage(self):
        pass

    def a_wh_teacher_is_on_the_units_page(self):
        pass

    def a_calculus_teacher_on_the_units_page(self):
        pass

    def a_student_on_final_thank_you_page(self):
        pass

    def clicks_ok_button(self):
        pass

    def the_student_is_redirected_to_the_subject_homepage(self):
        pass

    def he_is_a_teacher_of_multiple_subjects(self):
        pass

    def he_clicks_on_the_current_subject_to_open_the_dropdown(self):
        pass

    def he_sees_all_the_subjects_the_teacher_teaches_based_on_epl_authorization(self):
        pass

    def he_selects_a_different_subject_from_the_list(self):
        pass

    def the_content_of_the_page_is_updated_according_to_the_selected_subject(self):
        pass

    def a_section_has_been_expanded_for_a_taa(self):
        pass

    def he_navigate_to_a_different_page(self):
        pass

    def then_he_goes_back_to_teacher_module_page(self):
        pass

    def he_sees_the_last_section_accessed_expanded_in_the_subjects_taa(self):
        pass

    def he_navigates_through_different_subjects(self):
        pass

    def in_each_subject_he_expanded_a_section_for_a_taa(self):
        pass

    def he_navigates_back_to_each_subject_to_teacher_module_page(self):
        pass

    def he_uses_the_same_device(self):
        pass

    def he_sees_the_last_section_accessed_expanded_for_each_subject(self):
        pass

    def he_navigates_to_teacher_module_page_for_the_first_time(self):
        pass

    def all_sections_are_collapsed(self):
        pass

    def a_teacher_on_the_assign_assessment_by_class_popup_of_the_p1(self, p1 = "p1"):
        pass

    def he_logs_in_the_application_from_a_different_device_or_browser(self):
        pass

    def he_navigates_to_teacher_module_page(self):
        pass

    def he_wont_see_the_last_accessed_section_from_a_different_device_or_browser(self):
        pass

    def the_student_submitted_responses_on_the_video_follow_on_questions(self):
        pass

    def wants_to_change_the_responses(self):
        pass

    def under_profile_menu_for_the_duration_of_the_enrollment_is_displayed_my_ap_story_link(self):
        pass

    def clicks_on_my_ap_story_link_under_the_profile_menu(self):
        pass

    def the_video_follow_on_question_page_is_opened(self):
        pass

    def the_prior_responses_are_prefilled(self):
        pass

    def student_goes_to_video_follow_on_question_page(self):
        pass

    def modifies_the_prior_response(self):
        pass

    def the_new_response_is_submited(self):
        pass

    def student_goes_to_video_follow_on_question_page_to_edit_the_respons(self):
        pass

    def add_a_response_that_exceeds_the_visible_space(self):
        pass

    def a_scroll_bar_is_displayed_for_the_text_box(self):
        pass

    def a_student_that_submitted_the_response_for_the_video_follow_on_questions(self):
        pass

    def the_student_changes_the_response(self):
        pass

    def a_history_of_their_submitted_responses_is_stored_having_user_info_experimental_condition_time_stamp_and_response(self, datatable = "||"):
        pass

    def the_enrollment_period_has_finnished(self):
        pass

    def the_student_clicks_on_the_profile_menu(self):
        pass

    def sees_that_the_my_ap_story_link_is_not_available_anymore(self):
        pass

    def the_date_is_after_september_15(self):
        pass

    def a_student_logs_in(self):
        pass

    def is_prompted_with_exam_response_page(self):
        pass

    def the_student_clicks_on_the_link_in_the_exam_decision_respond_to_do_card_in_the_subject_homepage(self):
        pass

    def a_student_enrolled_in_more_that_one_subject(self):
        pass

    def the_exam_response_page_is_prompted(self):
        pass

    def sees_all_subjects_for_which_he_was_enrolled(self):
        pass

    def the_subjects_are_displayed_in_alphabetical_order(self):
        pass

    def a_student_on_exam_response_screen(self):
        pass

    def the_student_doesnt_confirm_their_response(self):
        pass

    def a_to_do_card_appears_on_the_homepage_for_each_subject(self):
        pass

    def student_does_not_select_a_response_for_each_course(self):
        pass

    def the_student_cannot_confirm_the_selection(self):
        pass

    def a_student_on_login_page(self):
        pass

    def student_is_not_at_first_login(self):
        pass

    def logged_in_from_a_different_device_for_the_first_time(self):
        pass

    def the_student_lands_on_the_homepage_for_the_first_subject_in_the_list(self):
        pass

    def the_subject_list_is_displayed_alphabetical(self):
        pass

    def the_student_signs_up(self):
        pass

    def the_student_is_first_prompted_with_welcome_video_wizard(self):
        pass

    def student_finishes_watching_the_video(self):
        pass

    def gives_feedback(self):
        pass

    def in_the_homepage_page_is_not_displayed_a_welcome_video_to_do_card(self):
        pass

    def yes_option_is_preselected(self):
        pass

    def student_closes_the_window_without_submitting_a_response(self):
        pass

    def a_to_do_red_card_is_displayed_on_subject_homepage(self):
        pass

    def says_p1(self, p1 = ""):
        pass

    def no_option_is_preselected(self):
        pass

    def the_to_do_card_says_please_indicate_whether_you_are_signing_up_to_take_the_ap_exam(self, please_indicate_whether_you_are_signing_up_to_take_the_ap_exam = "Please indicate whether you are signing up to take the AP exam"):
        pass

    def clicks_confirm_button(self):
        pass

    def the_exam_wizard_closes_and_user_is_signed_up_to_take_the_exam(self):
        pass

    def a_student_on_subject_homepage(self):
        pass

    def the_student_confirmed_the_exam_participation_in_the_exam_wizard(self):
        pass

    def a_white_to_do_card_is_displayed_on_the_subject_homepage(self):
        pass

    def the_card_says_you_re_signed_up_to_take_the_ap_exam(self, you_re_signed_up_to_take_the_ap_exam = "You're signed up to take the AP exam"):
        pass

    def selects_no_i_wish_to_remove_myself_from_taking_this_ap_exam_option(self, no_i_wish_to_remove_myself_from_taking_this_ap_exam = "No, I wish to remove myself from taking this AP exam"):
        pass

    def clicks_on_confirm_button(self):
        pass

    def the_exam_response_reasons_page_is_displayed(self):
        pass

    def student_confirmed_not_to_take_the_exam(self):
        pass

    def a_white_to_do_card_is_displayed_in_the_subject_homepage(self):
        pass

    def the_exam_response_reasons_page_is_displayed(self):
        pass

    def a_student_on_exam_wizard(self):
        pass

    def the_student_chooses_to_not_register_for_the_exam(self):
        pass

    def the_exam_response_reasons_page_is_displayed_with_an_entry_for_each_subject_for_which_the_student_choose_not_to_register_for_the_exam(self):
        pass

    def for_each_subject_is_available_a_dropdown_with_multiple_specific_reasons_and_an_p1choice(self, p1 = ""):
        pass

    def the_student_must_select_for_each_subject_the_reason_for_not_taking_the_exam(self):
        pass

    def a_student_on_subject_homepage(self):
        pass

    def the_student_submitted_his_responses(self):
        pass

    def the_exam_to_do_card_is_not_displayed_anymore_on_subject_homepage(self):
        pass

    def the_student_on_exam_wizard(self):
        pass

    def the_student_chooses_not_to_register_for_the_exam(self):
        pass

    def and_chooses_from_the_dropdown_a_reason_for_not_committing_to_take_the_exam(self):
        pass

    def the_student_submitted_his_responses_and_thank_you_screen_is_displayed(self):
        pass

    def the_student_hasnt_watch_the_welcome_video(self):
        pass

    def decided_not_to_register_to_take_the_exam(self):
        pass

    def giving_a_student_on_subject_homepage(self):
        pass

    def student_watched_the_welcome_video(self):
        pass

    def didnt_register_to_take_the_exam(self):
        pass

    def hasnt_given_feedbak(self):
        pass

    def on_the_subject_homepage_is_displayed_a_to_do_card_for_feedback(self):
        pass

    def a_white_ap_exam_card_saying_p1(self, p1 = ""):
        pass

    def on_the_subject_homepage_is_displayed_a_to_do_card_for_watching_the_video(self):
        pass

    def has_given_feedback(self):
        pass

    def on_subject_homepage_a_white_ap_exam_card_is_displayed_saying_p1(self, p1 = ""):
        pass

    def registered_to_take_the_exam(self):
        pass

    def a_white_ap_exam_card_saying_p1(self, p1 = ""):
        pass

    def on_the_subject_homepage_is_displayed_a_white_ap_exam_card_saying_p1(self, p1 = ""):
        pass

    def closes_the_exam_wizard_having_no_option_selected(self):
        pass

    def a_red_to_do_for_exam_decision_saying_p1(self, p1 = ""):
        pass

    def closes_the_exam_wizard_having_yes_preselected(self):
        pass

    def a_red_to_do_for_exam_decision_saying_p1(self, p1 = ""):
        pass

    def chooses_from_the_dropdown_the_p1_option(self, p1 = ""):
        pass

    def a_text_box_appears_for_the_user_to_enter_his_reason(self):
        pass

    def it_says_p1(self, p1 = ""):
        pass

    def student_changed_the_decision_for_some_subjects_from_no_to_yes(self):
        pass

    def those_subjects_are_not_displayed_in_the_exam_response_screen(self):
        pass

    def exam_response_screen_shows_only_the_subjects_where_no_was_selected(self):
        pass

    def selects_the_class_created_in_my_classes_and_clicks_assign(self):
        pass

    def selects_the_class_created_in_my_classes_and_clicks_on_assign_button(self):
        pass

    def the_quiz_is_assingned_to_the_created_class(self):
        pass

    def the_class_appears_in_choose_classes__my_classes_list_in_the_assign_popup(self):
        pass

    def clicks_the_assign_button_next_to_an_assessment(self):
        pass

    def a_teacher_on_assign_tab_from_question_bank_page(self):
        pass

    def a_pop_up_is_displayed_where_teacher_can_choose_a_class_and_configure_the_quiz(self):
        pass

    def clicks_assign_button_for_a_quiz(self):
        pass

    def p1_button_is_displayed(self, p1 = ""):
        pass

    def the_quiz_is_assigned_to_that_class(self):
        pass

    def clicks_on_question_bank_tab(self):
        pass

    def sees_in_the_performance_column_the_performance_for_each_quiz_displayed_as_a_stack_bar(self):
        pass

    def the_stack_bar_is_split_in_blocks_of_color_for_performance(self, datatable = "||"):
        pass

    def in_each_color_block_is_displayed_the_number_of_students_that_achieved_that_persormance(self):
        pass

    def sees_in_the_overall_column_the_overall_performance_of_the_class(self):
        pass

    def is_displayed_as_geometric_color_for_performance_performance(self, datatable = "||"):
        pass

    def clicks_on_the_class_name_under_my_classes(self):
        pass

    def are_displayed_only_the_quizzes_that_are_assigned_to_the_selected_class(self):
        pass

    def applies_filters_form_p1_section(self, p1 = ""):
        pass

    def are_displayed_only_the_quizzes_that_match_the_applied_filter(self):
        pass

    def clicks_on_a_quiz(self):
        pass

    def sees_that_specific_quiz_results_page(self):
        pass

    def p1_tab_is_displayed_by_default(self, p1 = ""):
        pass

    def a_teacher_on_the_results_page_for_a_specific_quiz(self):
        pass

    def clicks_class_performance_tab(self):
        pass

    def sees_the_group_type_assigned_on_date_unlocked_on_date_the_overall_performance_of_the_class_the_performance_of_the_class_displayed_as_a_stack_bar_and_the_performance_for_each_question(self):
        pass

    def teacher_is_on_class_performance_tab(self):
        pass

    def the_teacher_is_logged_in_the_application(self):
        pass

    def teacher_navigates_to_question_bank_page(self):
        pass

    def teacher_navigates_to_create_tab(self):
        pass

    def teacher_is_able_to_see_the_p1_button_in_the_topright_corner_of_the_screen(self, p1 = ""):
        pass

    def teacher_clicks_on_p1_button(self, p1 = ""):
        pass

    def teacher_is_able_to_choose_the_type_of_the_question_from_two_options_multiple_choice_and_free_response(self):
        pass

    def teacher_clicks_p1_button(self, p1 = ""):
        pass

    def teacher_is_able_to_see_free_response_question_type_page(self):
        pass

    def the_teacher_accesses_the_free_response_question_type_page_in_a_subject_question_bank(self):
        pass

    def teacher_specifies_a_question_name_a_prompt_completes_all_fields_for_one_scoring_category_and_specifies_the_metadata_by_choosing_at_least_one_tag_for_each_of_the_required_tags(self):
        pass

    def the_question_version_gets_published(self):
        pass

    def publish_button_becomes_grayed_out(self):
        pass

    def the_question_can_be_found_in_the_list_of_questions_in_create_tab(self):
        pass

    def teacher_completes_all_mandatory_fields_leaving_the_question_name_empty(self):
        pass

    def teacher_tries_to_click_p1_button(self, p1 = ""):
        pass

    def he_sees_the_button_is_not_available_being_greyed_out(self):
        pass

    def teacher_does_not_complete_all_mandatory_fields(self):
        pass

    def teacher_clicks_on_add_score(self):
        pass

    def a_new_score_is_being_added_to_the_bottom_of_the_form_having_a_score_feedback_field(self):
        pass

    def teacher_clicks_on_add_category(self):
        pass

    def a_new_category_is_added_to_the_bottom_of_the_form(self):
        pass

    def four_fields_can_be_seen_section_title_description_score_feedback_for_0_points_and_score_feedback_for_1_point(self):
        pass

    def a_new_score_has_been_added_to_the_question(self):
        pass

    def teacher_clicks_on_x_button_next_to_the_newly_added_score(self):
        pass

    def the_new_score_section_gets_removed_from_form(self):
        pass

    def a_new_category_has_been_added_to_the_question(self):
        pass

    def teacher_clicks_on_x_button_next_to_the_newly_added_category(self):
        pass

    def the_new_category_section_gets_removed_from_form(self):
        pass

    def he_clicks_on_x_button_next_to_the_default_category_under_scoring_section(self):
        pass

    def nothing_happens_because_x_button_is_not_available_being_greyed_out(self):
        pass

    def teacher_clicks_on_the_arrow_to_move_down_in_the_list_the_first_category(self):
        pass

    def the_first_category_goes_under_the_second_category_the_order_being_changed(self):
        pass

    def teacher_clicks_on_the_arrow_to_move_up_in_the_list_the_second_category(self):
        pass

    def the_second_category_goes_on_top_of_first_category_the_order_being_changed(self):
        pass

    def he_enters_p1_in_question_name_field(self, p1 = ""):
        pass

    def fills_in_the_mandatory_fields(self):
        pass

    def he_publishes_the_question(self):
        pass

    def the_question_is_published(self):
        pass

    def can_be_seen_in_the_list_without_breaking_the_layout(self):
        pass

    def he_enters_p1_in_prompt_field(self, p1 = ""):
        pass

    def the_teacher_has_created_a_frq_item_and_has_multiple_tags(self):
        pass

    def he_edits_the_question(self):
        pass

    def he_removed_some_tags_from_specify_metadata_tab(self):
        pass

    def he_publish_the_question(self):
        pass

    def the_removed_tags_are_no_longer_available(self):
        pass

    def the_question_is_published_without_errors(self):
        pass

    def it_is_no_longer_found_by_filtering_by_removed_tags(self):
        pass

    def the_teacher_has_created_a_frq_item(self):
        pass

    def publish_it_again(self):
        pass

    def a_new_version_is_published_and_the_question_can_be_seen_in_the_create_tab_list_having_the_new_changes(self):
        pass

    def he_edits_all_questions_fields(self):
        pass

    def he_edits_some_tags(self):
        pass

    def clicks_on_update_current_version(self):
        pass

    def the_current_version_gets_updated_and_the_question_can_be_seen_in_the_create_tab_list_having_the_new_changes(self):
        pass

    def he_updates_only_the_question_name(self):
        pass

    def he_updates_only_the_prompt_field(self):
        pass

    def he_clicks_to_update_the_version_after_small_changes(self):
        pass

    def then_he_clicks_on_publish_new_version(self):
        pass

    def choose_to_cancel_the_operation(self):
        pass

    def the_question_does_not_get_published_yet(self):
        pass

    def he_edits_some_fields_in_the_question_by_adding_also_a_new_score(self):
        pass

    def he_clicks_to_update_the_current_version_after_filling_the_new_score_field(self):
        pass

    def the_version_is_not_updated(self):
        pass

    def the_following_message_is_displayed_p1(self, p1 = ""):
        pass

    def he_edits_some_fields_in_the_question_by_adding_also_a_new_category(self):
        pass

    def he_clicks_to_update_the_current_version_after_filling_the_new_category_fields(self):
        pass

    def he_edits_some_fields_in_the_question_by_removing_a_score_from_a_category(self):
        pass

    def teacher_launches_a_subject_question_bank_in_ap_question_bank_section(self):
        pass

    def teacher_is_able_to_see_multiple_choice_question_type_page(self):
        pass

    def the_teacher_accesses_the_multiple_choice_question_type_page_in_a_subject_question_bank(self):
        pass

    def teacher_specifies_a_title_a_question_enters_the_answers_for_the_two_default_questions_and_specifies_the_metadata_by_choosing_at_least_one_tag_from_each_of_the_required_tag_categories(self):
        pass

    def teacher_clicks_p1_button_in_p2_tab(self, p1 = "", p2 = ""):
        pass

    def the_teacher_accesses_the_mc_type_page_in_a_subject_question_bank(self):
        pass

    def he_clicks_on_add_answer_in_edit_question_tab(self):
        pass

    def a_new_answer_is_added_to_the_bottom_having_answer_and_feedback_fields_available(self):
        pass

    def the_teacher_has_created_a_mc_item_having_3_answers(self):
        pass

    def he_deletes_a_score_by_clicking_on_its_x_button(self):
        pass

    def the_added_answer_is_removed_from_the_list_of_answers(self):
        pass

    def he_clicks_on_x_button_next_to_the_default_answers(self):
        pass

    def a_new_answer_has_been_added_to_the_question(self):
        pass

    def teacher_clicks_on_the_arrow_to_move_down_in_the_list_the_first_answer(self):
        pass

    def the_first_answer_goes_under_the_second_answer_the_order_being_changed(self):
        pass

    def teacher_clicks_on_the_arrow_to_move_up_in_the_list_the_second_answer(self):
        pass

    def the_second_answer_goes_on_top_of_first_answer_the_order_being_changed(self):
        pass

    def the_teacher_has_created_a_mc_item_and_has_multiple_tags(self):
        pass

    def he_removes_some_tags_from_specify_metadata_tab(self):
        pass

    def the_teacher_has_created_a_mc_item(self):
        pass

    def he_edits_some_fields_in_the_question_by_adding_also_a_new_answer(self):
        pass

    def he_clicks_to_update_the_current_version_after_filling_the_new_answer_fields(self):
        pass

    def he_edits_the_question_by_choosing_a_different_correct_answer(self):
        pass

    def he_clicks_to_update_the_current_version(self):
        pass

    def he_receives_a_notification_message(self):
        pass

    def the_version_does_not_get_updated(self):
        pass

    def he_edits_the_question_and_removes_an_answer(self):
        pass

    def he_edits_the_question_and_changes_the_answers_order(self):
        pass

    def sees_that_for_each_question_the_result_is_shown_as_a_stack_bar_split_in_blocks_of_color_for_result(self):
        pass

    def in_each_colored_block_is_displayed_the_number_of_students_that_answered(self):
        pass

    def clicks_on_the_performance_stack_bar_next_to_a_question(self):
        pass

    def a_popup_is_displayed_showing_the_students_names_for_correct_and_incorrect_answers(self):
        pass

    def clicks_on_the_performance_stack_bar_next_to_a_quiz(self):
        pass

    def a_popup_is_displayed_showing_the_students_names_for_at_mastery_approaching_mastery_and_below_mastery_performance(self):
        pass

    def clicks_on_p1_button_next_to_a_quiz(self, p1 = ""):
        pass

    def sees_the_question_having_the_correct_answer_letter_colored_in_green(self):
        pass

    def next_to_each_answer_is_displayed_the_number_of_students_that_choose_it(self):
        pass

    def clicks_on_a_question_in_class_performance_tab(self):
        pass

    def on_the_specific_question_results_page_clicks_on_the_right_arrow_button(self):
        pass

    def the_next_question_is_displayed(self):
        pass

    def clicks_on_student_performance_tab(self):
        pass

    def sees_a_for_every_student_the_total_points_and_the_answers_for_every_question_in_the_quiz(self):
        pass

    def clicks_on_a_student_name(self):
        pass

    def sees_the_mc_point_for_every_question_answered_by_the_selected_student(self):
        pass

    def sees_the_overall_points_scored_by_the_selected_student(self):
        pass

    def clicks_the_view_button_next_to_a_question(self):
        pass

    def sees_the_student_answer_and_the_correct_answer(self):
        pass

    def the_user_is_editing_a_question(self):
        pass

    def he_wants_to_exit_the_editor(self):
        pass

    def he_clicks_the_button_p1(self, p1 = ""):
        pass

    def he_should_return_to_the_list_of_questions_on_the_create_tab(self):
        pass

    def he_has_unsaved_changes(self):
        pass

    def he_should_be_alerted_that_they_have_unsaved_changes(self):
        pass

    def he_clicks_ok_in_the_alert_message(self):
        pass

    def he_clicks_cancel_in_the_alert_message(self):
        pass

    def he_should_remain_in_the_editor(self):
        pass

    def a_student_with_assigned_assignments(self):
        pass

    def student_goes_to_assignments_tab_form_assessment(self):
        pass

    def he_sees_the_assignment_having_opened_status(self, opened = "Opened"):
        pass

    def in_the_action_column_a_begin_button_is_available_for_the_opened_assignment(self):
        pass

    def the_teacher_assigned_a_quiz_for_a_class_but_hasnt_opened_it_yet(self):
        pass

    def no_begin_button_is_available(self):
        pass

    def a_student_on_assignments_tab_from_assessments(self):
        pass

    def student_clicks_on_p1(self, p1 = "p1"):
        pass

    def the_teacher_is_on_a_subject_qb_page(self):
        pass

    def teacher_navigates_to_create_tab(self):
        pass

    def teacher_is_able_to_see_the_quiz_create_form_in_the_topright_page(self):
        pass

    def teacher_is_on_create_tab(self):
        pass

    def teacher_clicks_p1_button_under_quiz_name(self, p1 = ""):
        pass

    def teacher_did_not_add_questions_or_a_title_for_the_quiz(self):
        pass

    def quiz_is_not_saved_and_the_user_should_see_p1(self, p1 = ""):
        pass

    def an_empty_quiz_is_previewed_in_a_popup_having_p1_and_p2_buttons(self, p1 = "", p2 = ""):
        pass

    def teacher_added_a_p1_for_the_quiz(self, p1 = ""):
        pass

    def teacher_did_not_add_questions_into_the_quiz(self):
        pass

    def the_teacher_is_on_create_tab_of_a_subject_qb_page(self):
        pass

    def teacher_has_added_2_questions_to_the_quiz(self):
        pass

    def teacher_clicks_p1_button(self, p1 = ""):
        pass

    def the_questions_content_are_previewed_in_a_popup_each_question_on_one_page(self):
        pass

    def p1_button_is_present_to_navigate_to_the_next_question(self, p1 = ""):
        pass

    def the_teacher_is_on_preview_page(self):
        pass

    def the_quiz_contains_at_least_two_questions(self):
        pass

    def the_preview_popup_is_closed(self):
        pass

    def the_list_of_questions_is_displayed(self):
        pass

    def he_already_added_2_questions_to_the_quiz(self):
        pass

    def teacher_clicks_p1_button_for_the_quiz(self, p1 = ""):
        pass

    def quiz_is_saved_and_can_be_seen_in_assign_tab(self):
        pass

    def save_button_becomes_assign(self):
        pass

    def teacher_clicks_on_x_button_next_to_a_question(self):
        pass

    def the_question_is_removed_from_the_list(self):
        pass

    def he_already_saved_a_quiz(self):
        pass

    def teacher_add_a_new_question_to_the_existing_quiz(self):
        pass

    def he_clicks_on_save_quiz_again(self):
        pass

    def quiz_is_saved(self):
        pass

    def it_can_be_seen_in_assign_tab(self):
        pass

    def teacher_removed_a_question_from_the_quiz(self):
        pass

    def quiz_is_saved_properly(self):
        pass

    def the_changes_can_be_seen_in_preview(self):
        pass

    def he_already_added_3_questions_to_a_quiz(self):
        pass

    def teacher_changes_the_order_of_the_questions_by_moving_questions_up_and_down_in_the_list(self):
        pass

    def he_clicks_on_preview(self):
        pass

    def he_sees_the_correct_order_of_the_questions(self):
        pass

    def choose_classes_popup_is_shown(self):
        pass

    def he_selects_a_class(self):
        pass

    def then_clicks_on_assign_button(self):
        pass

    def the_user_is_redirected_to_progress_tab(self):
        pass

    def the_teacher_is_on_assign_tab_of_a_subject_qb_page(self):
        pass

    def he_already_saved_several_quizzes(self):
        pass

    def he_checks_the_assign_tab_list(self):
        pass

    def for_each_quiz_there_are_2_buttons_preview_and_assign(self):
        pass

    def he_clicks_on_preview_button_for_a_quiz(self):
        pass

    def he_can_browse_the_questions_in_the_correct_order_by_clicking_on_next_or_previous_buttons(self):
        pass

    def clicks_on_assign_button_in_the_preview_window(self):
        pass

    def he_is_in_preview_window(self):
        pass

    def the_user_is_redirected_to_progress_tab_with_that_quiz_open(self):
        pass

    def a_popup_message_is_displayed_p1(self, p1 = ""):
        pass

    def he_clicks_cancel(self):
        pass

    def the_quiz_is_not_assigned_to_any_class(self):
        pass

    def the_popup_is_closed_and_user_is_left_on_preview_window(self):
        pass

    def he_is_in_the_preview_window(self):
        pass

    def he_clicks_on_close_preview_button(self):
        pass

    def preview_window_is_closed(self):
        pass

    def teacher_is_redirected_to_assign_tab(self):
        pass

    def he_clicked_assign(self):
        pass

    def he_sets_to_on_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def he_clicks_assign(self):
        pass

    def user_is_redirected_to_progress_tab_with_that_quiz_on_the_screen(self):
        pass

    def assignment_and_results_flags_are_on_with_red_under_student_access_section(self):
        pass

    def a_message_is_displayed_on_the_screen_p1(self, p1 = ""):
        pass

    def clicks_on_assessment_tab_in_the_navigation_menu(self):
        pass

    def clicks_on_progress_tab(self):
        pass

    def sees_that_in_assigned_column_is_displayed_for_each_quiz_the_date_the_quiz_was_assigned_to_the_class(self):
        pass

    def sees_the_status_of_the_quiz_in_the_status_column(self):
        pass

    def the_following_p1_is_displayed_for_p2(self, p1 = "", p2 = ""):
        pass

    def sees_in_the_action_column_a_review_button_displayed_for_started_or_completed_quizzes(self):
        pass

    def sees_that_the_review_button_is_missing_for_not_started_quizzes(self):
        pass

    def a_student_on_progress_tab_form_assessments(self):
        pass

    def clicks_on_the_review_button_in_action_column(self):
        pass

    def for_not_submitted_quizzes_the_answers_can_be_changed_and_the_progress_can_be_saved_or_submitted(self):
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

    def student_performance_tab_is_opened(self):
        pass

    def teacher_clicks_on_a_student(self):
        pass

    def then_clicks_on_print_report(self):
        pass

    def o_popup_appears_p1(self, p1 = ""):
        pass

    def after_pdf_is_generated_print_report_is_changed_to_get_report(self):
        pass

    def a_pdf_file_is_downloaded_and_contains_the_quiz_questions_results_and_points_plus_all_the_questions_listed_with_the_correctincorrect_answer(self):
        pass

    def print_all_reports_button_is_clicked(self):
        pass

    def a_pdf_file_is_downloaded_and_contains_the_quiz_questions_results_and_points_for_all_students_plus_all_the_questions_listed_for_each_student_with_the_correctincorrect_answers(self):
        pass

    def a_popup_appears_generating_pdf_this_make_take_up_to_20_seconds(self, generating_pdf_this_make_take_up_to_20_seconds = "Generating PDF... This make take up to 20 seconds"):
        pass

    def print_all_reports_button_is_changed_to_get_all_reports(self):
        pass

    def a_friendly_message_is_thrown_for_the_user_p1(self, p1 = "", datatable = "||"):
        pass

    def trying_to_login_with_an_email_address_incorrect_format_and_a_correct_password(self):
        pass

    def s_ign_in_button_is_disabled(self):
        pass

    def the_answers_cannot_be_modified_further(self):
        pass

    def he_already_signed_up_or_not_for_his_exams(self):
        pass

    def he_is_enrolled_by_a_teacher_in_another_class_for_another_subject(self):
        pass

    def he_logs_in_the_application_without_a_join_code(self):
        pass

    def a_student_on_the_homepage(self):
        pass

    def teacher_has_enabled_immediate_results_for_an_assignment(self):
        pass

    def a_student_is_on_the_homepage(self):
        pass

    def a_test_is_set_for_student_score_entry(self):
        pass

    def didnt_enter_the_scores_yet(self):
        pass

    def he_sees_khan_academy_resources_link_under_unit_title(self):
        pass

    def a_student_is_on_the_homepage(self):
        pass

    def is_redirected_to_resources_page(self):
        pass

    def a_student_is_on_the_resources_page(self):
        pass

    def a_class_is_already_created_for_the_teacher(self):
        pass

    def he_inspects_the_class_progress_widget(self):
        pass

    def he_sees_the_widget_displayed_between_the_top_banner_and_the_unit_widget(self):
        pass

    def the_widget_has_class_name_as_hyperlinked_nav_arrows_a__button(self):
        pass

    def a_section_for_assignments_information(self):
        pass

    def there_is_a__button_to_create_a_new_class(self):
        pass

    def there_are_4_tiles_in_its_content(self):
        pass

    def there_are_2_buttons_at_the_bottom_of_the_widget_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def teacher_is_redirected_to_assessments_page__results(self):
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

    def classes_are_displayed_in_alphabetical_order(self):
        pass

    def there_is_only_one_class(self):
        pass

    def the_teacher_tries_to_navigate_through_classes_using_arrows(self):
        pass

    def he_sees_the_arrows_are_disabled_since_there_is_only_1_class(self):
        pass

    def there_is_no_assignment_activity_for_that_class(self):
        pass

    def he_check_the_widget_content(self):
        pass

    def he_sees_you_don_t_have_any_assignment_activities_yet_(self, you_don_t_have_any_assignment_activities_yet_ = "You don't have any assignment activities yet."):
        pass

    def a_class_having_a_very_long_name_is_created(self):
        pass

    def the_class_is_displayed_in_the_widget(self):
        pass

    def the_name_is_truncated_with_ellipsis(self):
        pass

    def the_full_name_can_be_seen_via_popover(self):
        pass

    def there_are_fewer_than_the_max_tiles_displayed_in_the_widget(self):
        pass

    def the_2_buttons_p1_and_p2_are_bottom_aligned_to_the_widget(self, p1 = "", p2 = ""):
        pass

    def there_is_assignment_activity_in_that_class(self):
        pass

    def it_is_the_exam_decision_period(self):
        pass

    def teacher_checks_the_class_widget(self):
        pass

    def its_not_the_exam_period(self):
        pass

    def he_does_not_see_the_exam_response_tile(self):
        pass

    def he_sees_the_rest_of_activity_tiles(self):
        pass

    def a_new_student_is_added_to_the_class(self):
        pass

    def he_did_not_respond_to_exam_decision_questions_whether_he_is_taking_exam_or_not(self):
        pass

    def students_name_is_displayed_in_the_popover_under_the_correct_column(self):
        pass

    def the_updated_list_is_still_alphabetized(self):
        pass

    def the_number_of_students_that_responded_to_exam_questions_in_green_and_number_that_have_not_responded_yet_in_red(self):
        pass

    def a_teacher_on_unit_assessments_tab__results(self):
        pass

    def criteria_is_met_for_next_steps_cards_display(self):
        pass

    def teacher_sees_the_cards_ordered_by_priority_of_teacher_attention_based_on_performance_and_number_of_items_assessing_each_block(self):
        pass

    def class_average_performance_percent_correct_of_scored_students_below_49(self):
        pass

    def the_next_step_card_shows_a_red_performance_marker(self):
        pass

    def class_average_performance_percent_correct_of_scored_students_is_between_50_79(self):
        pass

    def the_next_step_card_shows_a_yellow_performance_marker(self):
        pass

    def class_average_performance_is_above_80(self):
        pass

    def no_next_step_card_is_displayed(self):
        pass

    def is_enrolled_in_p1(self, p1 = "p1"):
        pass

    def there_is_an_assessment_available_for_the_students_unlocked_and_not_marked_completed(self):
        pass

    def it_has_not_been_submitted_by_all_students(self):
        pass

    def there_are_still_slots_remaining(self):
        pass

    def he_can_see_monitor_student_assignments_tile(self):
        pass

    def it_has_the_name_p1(self, p1 = ""):
        pass

    def there_is_an_assessment_available_for_the_students(self):
        pass

    def it_has_been_submitted_by_all_students(self):
        pass

    def monitor_student_assignments_tile_is_not_displayed_in_the_widget(self):
        pass

    def is_displayed_a_skill_card_for_teacher_module(self):
        pass

    def all_the_criterias_to_display_the_tile_is_met(self):
        pass

    def there_is_no_slots_remaining(self):
        pass

    def the_correspondent_next_steps_cards_are_sorted_from_lowest_to_highest(self):
        pass

    def there_are_more_assignments_unlocked_for_the_students_and_in_progress(self):
        pass

    def there_are_2_slots_available(self):
        pass

    def he_sees_first_the_assignment_which_has_the_most_tests_to_be_submitted_where_test_is_unlocked_and_is_still_accepting_submissions_unlocked_and_not_marked_as_completed(self):
        pass

    def then_he_sees_the_oldest_assignment(self):
        pass

    def he_sees_from_0_to_how_many_open_slots_remaining_in_the_widget_max_of_4_if_not_in_exam_decision_window_after_exam_decision_view_latest_reports_s_core_student_work_tiles_are_evaluated(self):
        pass

    def an_assignment_is_in_progress(self):
        pass

    def the_submitted_in_progress_no_started_bar_is_displayed_containing_the_their_corresponding_numbers_of_students(self):
        pass

    def the_he_can_see_in_the_upper_right_corner_of_the_tile_unlocked_date(self):
        pass

    def teacher_clicks_on_assignment_name(self):
        pass

    def he_is_redirected_to_the_app_progress_assignment_overview_page_for_the_associated_class(self):
        pass

    def all_criterias_are_met_to_display_all_4_tiles_in_the_widget_in_the_same_time(self):
        pass

    def he_sees_all_4_tiles_displayed_in_the_following_order_exam_decision_view_latest_results_score_student_work_monitor_student_assignments(self):
        pass

    def there_is_an_assessment_that_has_fr_qs_which_are_awaiting_scoring_by_teacher_display_status_submitted_or_s_core_startedaction_button_score(self):
        pass

    def the_criteria_has_been_met(self):
        pass

    def verifies_the_score_student_work_tile_title(self):
        pass

    def he_sees_the_p1_tile(self, p1 = ""):
        pass

    def there_there_is_an_assessment_that_has_fr_qs_which_has_scores_entered_by_students_but_are_awaiting_review_by_the_teacher_status_student_scoredaction_button_review(self):
        pass

    def there_are_some_more_assignments_meeting_the_criteria_in_progress(self):
        pass

    def he_sees_first_the_assignment_that_has_the_most_tests_available_to_score_score_progress_available(self):
        pass

    def then_the_oldest_assignment_determined_by_unlocked_date_test(self):
        pass

    def the_assessment_is_in_progress(self):
        pass

    def the_he_sees_the_entered_available_no_started_progress_bar_with_its_corresponding_students_number(self):
        pass

    def the_number_of_tiles_displayed_are_from_0_to_as_many_as_there_are_available_tile_slots_remaining_in_the_widget_max_4_if_not_in_decision_window_after_exam_decision_and_view_latest_results_are_evaluated(self):
        pass

    def there_is_an_assesment_in_progress_but_it_does_not_have_fr_qs(self):
        pass

    def he_wont_see_the_score_student_work_tile_displayed_in_the_class_widget(self):
        pass

    def he_is_redirected_to_the_app_progress_assignment_overview_page_for_the_asociated_class(self):
        pass

    def he_sees_the_date_unlocked_in_upper_right_corner_of_the_tile(self):
        pass

    def the_criteria_is_met_and_the_next_steps_cards_are_displayed(self):
        pass

    def sees_the_card_title_being_the_block_name_for_blocklevel_resource_cards(self):
        pass

    def under_the_title_sees_resource_links_in_this_order_if_they_exist_for_the_block_teacher_lesson_plan_student_handout_focus_quiz(self):
        pass

    def a_unit_taa_next_steps_card_is_displayed(self):
        pass

    def sees_that_the_next_step_card_header_is_unit(self):
        pass

    def sees_the_card_title_is_the_unit_name(self):
        pass

    def sees_teaching_and_assessing_resources_under_the_card_title(self):
        pass

    def khan_academy_teacher_lesson_plan_student_handout_focus_quiz_resources_links_are_not_displayed_for_this_kind_of_card(self):
        pass

    def clicks_on_a_related_questions_link_on_a_next_step_card(self):
        pass

    def at_least_one_assessment_that_meets_the_criteria_of_having_80_of_the_class_having_the_assignment_fully_scored(self):
        pass

    def he_checks_the_tile_title(self):
        pass

    def he_sees_the_tile_p1_in_the_class_widget(self, p1 = ""):
        pass

    def the_criteria_for_having_80_of_the_class_fully_scored_the_assignment_is_not_met(self):
        pass

    def the_p1_tile_is_not_displayed_in_the_widget(self, p1 = ""):
        pass

    def there_are_some_fr_qs_in_the_assessment(self):
        pass

    def teacher_has_reviewedaccepted_responses_entered_by_student_or_they_have_entered_the_scores_themselves_when_status_of_test_is_scored(self):
        pass

    def only_then_it_is_considered_scored(self):
        pass

    def they_are_represented_in_the_progress_bar(self):
        pass

    def there_are_at_least_2_assessments_meeting_the_80_criteria(self):
        pass

    def he_sees_2_tiles_of_view_latest_results(self):
        pass

    def the_order_is_determined_by_the_most_recent_date_unlocked_available_to_students(self):
        pass

    def the_number_of_tiles_for_p1_can_be_from_0_to_4(self, p1 = ""):
        pass

    def more_than_one_will_be_displayed_only_if_there_are_slots_remaining_after_rules_for_score_student_work_and_monitor_student_assignments(self):
        pass

    def there_are_already_3_tiles_displayed_for_exam_response_score_student_work_and_monitor_student_assignments(self):
        pass

    def he_sees_only_1_tile_for_view_latest_results(self):
        pass

    def he_sees_mastery_approaching_mastery_at_mastery_no_results_performance_bar_from_class_performance_report_red_yellow_green_gray(self):
        pass

    def each_category_contains_the_correct_number_of_students(self):
        pass

    def teacher_clicks_on_the_progress_bar_from_the_view_latest_results_tile_in_the_class_widget(self):
        pass

    def check_the_students_order_from_popover(self):
        pass

    def students_should_be_sorted_by_increasing_performance(self):
        pass

    def a_popover_is_displayed_showing_the_students_fitting_into_each_category_based_on_their_current_status(self):
        pass

    def he_sees_the_unlocked_date_in_the_upper_right_corner_of_the_tile(self):
        pass

    def he_is_redirected_to_the_appresults_assignment_class_performance_page_for_the_associated_class(self):
        pass

    def clicks_on_a_question_in_class_performance_tab(self):
        pass

    def sees_that_the_resources_are_shown_in_the_following_order_khan_resources_teacher_lesson_plan_student_handout(self):
        pass

    def clicks_on_a_question_that_belongs_to_a_focus_block(self):
        pass

    def in_related_resources_section_to_the_right_of_the_question_sees_teacher_lesson_plan_and_student_handout_resources(self):
        pass

    def clicks_on_a_question_that_belongs_to_a_block(self):
        pass

    def in_related_resources_section_to_the_right_of_the_question_are_not_displayed_teacher_lesson_plan_and_student_handout_resources(self):
        pass

    def in_related_resources_section_to_the_right_of_the_question_are_displayed_khan_academy_resources(self):
        pass

    def a_student_on_his_homepage(self):
        pass

    def he_navigates_to_resources_tab(self):
        pass

    def he_can_see_all_the_units(self):
        pass

    def checks_the_resources_page(self):
        pass

    def there_is_no_teachers_guide_element(self):
        pass

    def a_unit_is_expanded(self):
        pass

    def student_checks_the_units_resources(self):
        pass

    def he_only_sees_khan_resources(self):
        pass

    def expand_all_is_clicked(self):
        pass

    def no_filters_are_available_in_the_page(self):
        pass

    def all_the_units_get_collapsed(self):
        pass

    def he_is_able_to_see_units_widget(self):
        pass

    def student_checks_units_widget(self):
        pass

    def he_sees_only_view_all_khan_academy_resources_under_unit_name(self):
        pass

    def he_clicks_on_a_building_block(self):
        pass

    def student_is_redirected_to_resources_page(self):
        pass

    def the_corresponding_unit_is_expanded_and_the_bb_highlighted(self):
        pass

    def he_clicks_on_view_all_blocks_button(self):
        pass

    def he_is_redirected_to_resources_page(self):
        pass

    def the_corresponding_unit_is_expanded_displaying_all_its_building_blocks(self):
        pass

    def there_are_more_units_available(self):
        pass

    def student_clicks_on_arrows_from_topright_corner_of_the_widget(self):
        pass

    def he_can_navigates_through_the_units_using_arrows(self):
        pass

    def a_random_unit_is_expanded_in_resources(self):
        pass

    def the_he_navigates_to_homepage_to_check_the_units_widget(self):
        pass

    def the_last_accessed_unit_is_displayed_in_the_widget(self):
        pass

    def he_clicks_on_unit_name_in_the_widget(self):
        pass

    def he_is_redirected_to_resources(self):
        pass

    def clicked_unit_is_expanded_showing_all_the_units(self):
        pass

    def a_khan_resource_is_opened_in_a_new_tab(self):
        pass

    def student_clicks_on_view_all_khan_resources_for_a_unit_on_the_widget_or_on_the_resources_tab(self):
        pass

    def the_corresponding_higher_level_khan_resource_page_is_opened_in_a_new_tab(self):
        pass

    def he_updates_only_the_question_field(self):
        pass

    def he_enters_p1_in_question_field(self, p1 = ""):
        pass

    def an_educator_admin_user_on_login_page(self):
        pass

    def an_educator_admin_user_logs_in_the_application(self):
        pass

    def the_multisubject_landing_page_is_displayed(self):
        pass

    def sees_a_single_alphabetized_list_containing_all_subjects(self):
        pass

    def he_logs_in(self):
        pass

    def is_given_access_directly_to_am(self):
        pass

    def is_not_authenticated_or_authorized_through_eplsso(self):
        pass

    def selects_a_subject_in_the_subject_landingpage(self):
        pass

    def the_admin_is_redirected_to_selected_subject_homepage(self):
        pass

    def is_redirected_to_subject_homepege(self):
        pass

    def sees_a_blue_bar_on_the_subject_homepage_beneath_the_subject_navigation_that_has_school_and_teacher_dropdowns(self):
        pass

    def an_educator_admin_user_on_the_subject_homepage(self):
        pass

    def school_dropdown_has_only_one_entry(self):
        pass

    def the_value_is_displayed_as_text_not_as_dropdown(self):
        pass

    def teacher_dropdown_has_only_one_entry(self):
        pass

    def selects_from_teacher_dropdown_a_teacher(self):
        pass

    def sees_the_course_experience_for_the_selected_teacher(self):
        pass

    def no_value_is_selected_for_school_and_teacher_filters(self):
        pass

    def the_class_preview_widget_will_display_the_following_message_p1(self, p1 = ""):
        pass

    def selects_values_for_school_and_teacher_dropdowns(self, school = "School", teacher = "Teacher"):
        pass

    def changes_the_subject_from_the_subject_dropdwon(self):
        pass

    def the_school_and_teacher_filters_will_reset_to_the_defaults(self, school = "School", teacher = "Teacher"):
        pass

    def the_educator_admin_belongs_to_only_one_school(self):
        pass

    def the_school_name_is_displayed_and_selected_in_the_school_filter_without_having_the_appearance_of_a_dropdown(self):
        pass

    def educator_admin_user_belongs_to_multiple_schools(self):
        pass

    def the_school_dropdown_defaults_to_select_school(self, select_school = "Select School"):
        pass

    def schools_are_displayed_alphabetically_in_the_dropdown(self):
        pass

    def the_educator_admin_did_not_select_a_value_for_p1_dropdown(self, p1 = ""):
        pass

    def the_p1_dropdown_in_not_active(self, p1 = ""):
        pass

    def is_displayed_as_grayed_out(self):
        pass

    def selects_a_school_from_school_dropdown(self, school = "School"):
        pass

    def clicks_to_expand_p1_dropdown(self, p1 = ""):
        pass

    def sees_the_teacher_name_is_displayed_as_first_name_last_name(self):
        pass

    def selects_a_school_from_p1_dropdown(self, p1 = ""):
        pass

    def there_is_only_one_teacher_at_the_selected_school_for_the_selected_subject(self):
        pass

    def the_teacher_name_is_displayed_and_selected_without_having_the_appearance_of_a_dropdown(self):
        pass

    def for_school_dropdown_is_selected_a_school_that_has_multiple_teachers(self, school = "School"):
        pass

    def the_p1_dropdown_is_active_and_defaulted_to_p2(self, p1 = "", p2 = ""):
        pass

    def there_is_no_teacher_for_the_current_selected_subject_at_the_selected_school(self):
        pass

    def p1_is_displayed(self, p1 = ""):
        pass

    def selects_a_teacher_form_p1_dropdown(self, p1 = ""):
        pass

    def the_p1_widget_populates_as_if_the_selected_teacher_is_viewing_it(self, p1 = ""):
        pass

    def from_p1_dropdown_selects_himself(self, p1 = ""):
        pass

    def the_classes_he_has_created_also_show_in_the_p1_widget(self, p1 = ""):
        pass

    def logs_out(self):
        pass

    def then_logs_back_in(self):
        pass

    def does_not_remember_where_the_educator_admin_left_off(self):
        pass

    def a_class_roster_teacher_educator_on_my_classes_page(self, my_classes = "My Classes"):
        pass

    def a_student_in_a_given_class_has_not_provided_an_exam_response(self):
        pass

    def the_class_rooster_clicks_to_view_that_class_details_in_my_classes_page(self, my_classes = "My Classes"):
        pass

    def p1_column_from_p2_page_has_p3_value_colored_in_red(self, p1 = "", p2 = "", p3 = ""):
        pass

    def a_student_in_a_given_class_has_provided_an_exam_response(self):
        pass

    def p1_column_from_p2_page_has_p3_value_colored_in_green(self, p1 = "", p2 = "", p3 = ""):
        pass

    def some_of_the_students_enrolled_in_a_given_class_have_provided_an_exam_response_and_some_didnt(self):
        pass

    def p1_column_will_have_p2_value_for_the_students_that_provided_an_exam_response(self, p1 = "", p2 = ""):
        pass

    def p1_value_for_the_students_that_havent_provided_an_exam_response(self, p1 = ""):
        pass

    def clicks_on_a_class_to_see_its_details(self):
        pass

    def sees_n_a_value_in_p2_column_correspondent_to_a_teacher(self, n_a = "", p2 = ""):
        pass

    def the_exam_decision__experimental_optout_page_is_prompted(self):
        pass

    def sees_that_the_page_headline_is_you_are_registered_to_take_the_following_ap_exam_s_in_may_2018(self, you_are_registered_to_take_the_following_ap_exam_s_in_may_2018 = "You are registered to take the following AP Exam(s) in May 2018"):
        pass

    def for_each_exam_are_available_the_following_radio_button_labels_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def the_footnote_message_on_policies_is_depending_on_your_schools_policies_there_can_be_fees_associated_with_ap_exams_scholarships_can_be_available_to_eligible_students_to_reduce_some_of_these_fees_if_applicable_exam_fees_will_be_collected_directly_by_your_school_if_you_have_questions_talk_to_your_schools_ap_coordinator_or_to_your_ap_teacher(self, p1 = ""):
        pass

    def the_exam_decision__experimental_optout_page_is_prompted(self):
        pass

    def sees_that_the_default_selection_is_p1(self, p1 = ""):
        pass

    def the_exam_decision__control_optin_page_is_prompted(self):
        pass

    def sees_that_no_default_selection_is_available(self):
        pass

    def exam_decision__control_optin_page_is_prompted(self):
        pass

    def sees_that_the_page_headline_is_do_you_wish_to_register_to_take_the_following_ap_exam_s_in_may_2018_(self, do_you_wish_to_register_to_take_the_following_ap_exam_s_in_may_2018_ = "Do you wish to register to take the following AP Exam(s) in May 2018?"):
        pass

    def for_each_exam_listed_are_available_the_following_radio_button_labels_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def for_each_exam_are_available_the_following_radio_button_labels_confirm_registration_and_no_i_wish_to_remove_myself_from_taking_this_ap_exam(self, confirm_registration = "", no_i_wish_to_remove_myself_from_taking_this_ap_exam = "No, I wish to remove myself from taking this AP Exam"):
        pass

    def the_footnote_message_on_policies_is_p1(self, p1 = ""):
        pass

    def the_exam_window_closed(self):
        pass

    def a_student_register_in_a_class(self):
        pass

    def the_date_is_set_to_be_in_the_exam_window(self):
        pass

    def student_logs_in(self):
        pass

    def exam_response_pops_up(self):
        pass

    def a_student_in_the_exam_window(self):
        pass

    def he_is_already_signed_up_in_2_classes(self):
        pass

    def he_answered_to_the_exam_decision_questions(self):
        pass

    def the_student_registers_in_a_new_class(self):
        pass

    def then_the_exam_window_opens(self):
        pass

    def the_student_logs_in(self):
        pass

    def the_exam_decision_page_pops_up(self):
        pass

    def it_has_prefilled_the_answers_for_the_old_exams(self):
        pass

    def asking_an_answer_for_the_new_class(self):
        pass

    def he_joined_a_class_and_responded_to_exam_decision_questions(self):
        pass

    def he_joined_another_class(self):
        pass

    def the_student_gets_prompted_with_the_exam_decision_question(self):
        pass

    def has_the_answer_for_the_old_exam_prefilled(self):
        pass

    def gives_different_answers_for_the_exams_that_he_is_signed_up(self):
        pass

    def this_user_is_enrolled_to_another_exam(self):
        pass

    def student_logs_in_after_he_is_enrolled_in_the_new_class(self):
        pass

    def he_clicks_close_in_the_exam_decision_window(self):
        pass

    def the_corresponding_to_do_card_is_created_for_the_new_exam(self):
        pass

    def the_card_is_red(self):
        pass

    def the_message_is_please_indicate_whether_you_are_registering_for_the_ap_exam(self, please_indicate_whether_you_are_registering_for_the_ap_exam = "Please indicate whether you are registering for the AP Exam"):
        pass

    def the_old_cards_keep_their_answers_and_selections(self):
        pass

    def he_is_registered_in_a_new_class(self):
        pass

    def responds_to_the_exam_decision_question(self):
        pass

    def the_exam_window_closes(self):
        pass

    def the_corresponding_to_do_card_for_the_exam_decision_are_not_displayed(self):
        pass

    def the_card_is_displayed_under_to_dos_not_under_ap_exam(self):
        pass

    def student_clicks_on_the_ap_exam_card(self):
        pass

    def the_exam_response_pop_up_opens(self):
        pass

    def a_student_clicks_on_ap_exam_card_for_the_current_subject(self):
        pass

    def exam_response_page_opens(self):
        pass

    def sees_that_all_subjects_he_is_enrolled_in_are_shown_not_just_the_one_for_the_subject_he_is_viewing(self):
        pass

    def he_chooses_no_i_wish_to_remove_myself_from_taking_this_ap_exam_option(self, no_i_wish_to_remove_myself_from_taking_this_ap_exam = "No, I wish to remove myself from taking this AP Exam"):
        pass

    def the_reasons_for_no_page_is_displayed_asking_for_the_reason_why_not_taking_the_test_for_each_no_response(self):
        pass

    def he_chooses_the_p1_option(self, p1 = ""):
        pass

    def he_doesnt_change_any_response(self):
        pass

    def clicks_on_p1_button(self, p1 = ""):
        pass

    def has_no_responses(self):
        pass

    def is_taken_to_the_reasons_for_no_page_where_he_can_choose_to_modify_the_existing_reason_for_no(self):
        pass

    def has_do_not_register_responses(self, do_not_register = "Do not register"):
        pass

    def he_sees_the_welcome_video_and_respond_to_exam_decision_questions(self):
        pass

    def clicks_confirm(self):
        pass

    def user_is_redirected_to_a_page_with_a_message_p1(self, p1 = ""):
        pass

    def selects_no_do_not_register__then_confirm(self):
        pass

    def the_student_chooses_a_response(self):
        pass

    def the_responses_are_saved(self):
        pass

    def he_expands_the_reasons_list_by_clicking_the_dropdown(self):
        pass

    def student_sees_page_heading_which_best_describes_your_reason_for_not_registering_to_take_the_exam_at_this_time_(self, which_best_describes_your_reason_for_not_registering_to_take_the_exam_at_this_time_ = "Which best describes your reason for not registering to take the exam at this time?"):
        pass

    def chooses_only_confirm_registration(self):
        pass

    def the_reasons_for_no_page_is_not_displayed_and_they_return_to_the_homepage(self):
        pass

    def chooses_only_register_option(self):
        pass

    def the_dropdown_list_contains_the_following_p1(self, p1 = ""):
        pass

    def the_footnot_text_is(self):
        pass

    def the_student_selects_no_or_do_not_register_in_the_exam_decision_window(self):
        pass

    def student_selects_other_in_the_dropdown(self):
        pass

    def the_instructions_are_displayed_within_the_textbox_p1(self, p1 = ""):
        pass

    def a_district_admin_user_logs_in(self):
        pass

    def click_on_my_groups_menu(self):
        pass

    def my_groups_page_is_displayed_showing_on_the_lefthand_panel_their_district_name(self):
        pass

    def a_district_admin_user_is_on_my_groups_page(self):
        pass

    def clicks_on_district_name(self):
        pass

    def all_schools_associated_with_the_district_are_shown_in_the_primary_display(self):
        pass

    def clicks_on_a_school_name_from_the_lefthand_panel(self):
        pass

    def sees_all_classes_associated_with_the_school(self):
        pass

    def clicks_on_a_school_name(self):
        pass

    def no_classes_have_been_created_by_teachers_in_selected_school(self):
        pass

    def a_message_letting_the_user_know_that_no_class_was_created_for_that_school_is_displayed(self):
        pass

    def clicks_on_a_school_to_see_the_associated_classes(self):
        pass

    def sees_any_classes_he_has_created(self):
        pass

    def clicks_on_a_class_name(self):
        pass

    def the_class_roster_will_display_along_with_the_join_code_information(self):
        pass

    def a_school_admin_user_is_on_my_groups_page(self):
        pass

    def he_joins_a_calculus_class(self):
        pass

    def he_is_prompted_with_exam_decision_page(self):
        pass

    def he_will_be_seeing_next_to_confirm_register_the_which_exam_dropdown(self):
        pass

    def it_has_2_options_ap_calculus_ab_and_ap_calculus_bc(self, ap_calculus_ab = "AP Calculus AB", ap_calculus_bc = "AP Calculus BC"):
        pass

    def he_selects_in_the_exam_decision_page_an_exam_from_dropdown(self):
        pass

    def he_clicks_the_combo_again_and_selects_the_other_option(self):
        pass

    def the_new_option_is_properly_saved(self):
        pass

    def he_clicks_p1(self, p1 = ""):
        pass

    def which_exam_dropdown_becomes_disabled(self):
        pass

    def the_experimental_optout_treatment_is_assigned_to_the_student(self):
        pass

    def he_reaches_exam_decision_page(self):
        pass

    def confirm_registration_option_is_by_default_selected(self):
        pass

    def which_exam_dropdown_is_active_by_default(self):
        pass

    def confirm_button_is_disabled_because_no_exam_has_been_selected_in_dropdown(self):
        pass

    def no_exam_is_selected_in_the_which_exam_dropdown(self):
        pass

    def confirm_register_is_selected(self):
        pass

    def then_no_is_selected(self):
        pass

    def confirm_register_is_checked_but_no_exam_is_selected_in_the_list(self):
        pass

    def confirm_button_gets_activated(self):
        pass

    def the_control_optin_treatment_is_assigned_to_a_student(self):
        pass

    def no_is_selected(self):
        pass

    def the_which_exam_dropdown_gets_disabled(self):
        pass

    def confirm_button_gets_disabled(self):
        pass

    def register_is_selected(self):
        pass

    def which_exam_gets_activated(self):
        pass

    def he_already_responded_to_exam_decision_questions_for_calculus_exams(self):
        pass

    def he_joins_another_class(self):
        pass

    def he_will_be_prompted_with_the_exam_decision_page(self):
        pass

    def the_previous_selection_in_which_exam_combo_should_be_preserved(self):
        pass

    def clicks_on_usage_tab(self):
        pass

    def the_usage_report_page_is_displayed(self):
        pass

    def an_educator_admin_on_usage_page(self):
        pass

    def selects_a_values_for_district_and_schools__classes_filters(self):
        pass

    def for_the_selected_classes_arent_quizzes_assigned(self):
        pass

    def selects_a_school_from_school__classes_filter(self):
        pass

    def sees_that_the_last_login_column_displays_the_date_the_teacher_of_the_selected_class_last_logged_in_to_the_apsupport_platform(self):
        pass

    def sees_that_days_visited_column_displays_the_number_of_days_in_which_the_teacher_of_the_selected_class_has_accessed_the_platform(self):
        pass

    def sees_the_number_of_classes_column_displays_the_number_of_classes_taught_by_the_teacher_at_the_selected_school(self):
        pass

    def sees_in_the_total_students_column_the_number_of_students_who_have_joined_classes_belonging_to_specific_teacher(self):
        pass

    def sees_unit_assessments_column_displays_the_number_of_unit_assessments_assigned_unit_tests_and_focus_quizzes_by_the_teacher_given_the_filter_criteria(self):
        pass

    def selects_a_schoolclass_from_school__classes_filter(self):
        pass

    def sees_that_question_bank_column_displays_the_number_of_question_bank_quizzes_assigned_by_the_teacher_given_the_filter_criteria(self):
        pass

    def selects_a_few_schools_from_schools__classes_filter(self):
        pass

    def sees_that_school_column_displays_the_associated_school_name_for_the_teacher(self):
        pass

    def the_list_of_teachers_teacher(self, datatable = ""):
        pass

    def the_message_is_message(self):
        pass

    def a_teacher_on_the_teaching_and_assessing_page_for_p1(self, p1 = ""):
        pass

    def clicks_assessments_tab(self):
        pass

    def assessments_page_content_for_p1_is_displayed(self, p1 = ""):
        pass

    def clicks_question_bank_tab(self):
        pass

    def a_teacher_on_a_subject_homepage(self):
        pass

    def sees_teaching_and_assessing_page_for_the_selected_subject(self):
        pass

    def a_teacher_on_assign_tab_from_assessment_page(self):
        pass

    def an_information_icon_appears_next_to_the_class_name(self):
        pass

    def does_not_select_a_class(self):
        pass

    def the_assign_button_is_not_displayed(self):
        pass

    def a_select_a_classbutton_is_displayed(self, select_a_class_button = "Select a class button"):
        pass

    def selected_classes_area_is_empty(self):
        pass

    def in_the_selected_classes_area_the_selected_class_name_is_displayed(self):
        pass

    def clicks_to_uncheck_one_of_the_selected_classes(self):
        pass

    def clicks_on_assign_button(self):
        pass

    def teacher_creates_a_class_in_my_classes(self):
        pass

    def teacher_goes_to_assessments_page(self):
        pass

    def the_class_appears_in_assessments_my_classes_list(self):
        pass

    def teacher_creates_a_class_in_my_classes_page(self):
        pass

    def teacher_goes_to_assessments_assign_tab(self):
        pass

    def clicks_on_assign_button_next_to_a_quiz(self):
        pass

    def the_teacher_module_page_is_displayed(self):
        pass

    def the_outline_is_collapsed(self):
        pass

    def a_teacher_on_units_page(self):
        pass

    def clicks_teacher_module_link_within_a_unit(self):
        pass

    def sees_that_the_unit_has_only_one_taa_module_associated_with_it(self):
        pass

    def a_teacher_on_teacher_module_page(self):
        pass

    def clicks_on_a_module_to_expand_it(self):
        pass

    def sees_that_a_teacher_module_can_be_associated_with_more_than_one_unit(self):
        pass

    def a_teacher_on_assessments_results_page(self):
        pass

    def clicks_on_a_question(self):
        pass

    def clicks_student_performance_tab(self):
        pass

    def clicks_on_a_student(self):
        pass

    def a_teacher_on_teaching__assessing_page(self):
        pass

    def sees_a_pop_up_containing_the_link_to_the_taa_resource(self):
        pass

    def clicks_on_practices_filter(self):
        pass

    def clicks_on_skills_filter(self):
        pass

    def a_list_of_mc_and_fr_published_questions(self):
        pass

    def some_of_them_have_skills_as_metadata_some_practices_some_units(self):
        pass

    def teacher_is_in_the_question_bank_create_tab(self):
        pass

    def he_filters_the_qb_items_by_the_parent_skill_orand_by_the_parent_practice_orand_by_the_parent_unit(self):
        pass

    def a_list_of_mc_and_fr_draft_questions(self):
        pass

    def a_list_of_mc_and_fr_publisheddraft_questions(self):
        pass

    def chooses_a_subject_from_subject_dropdown(self):
        pass

    def enters_a_class_name_in_name_field(self):
        pass

    def clicks_the_enroll_members_button(self):
        pass

    def searches_for_a_member(self):
        pass

    def clicks_on_the_add_button_next_to_a_member_name(self):
        pass

    def clicks_on_a_class_name_from_my_classes_list(self):
        pass

    def click_on_save_button(self):
        pass

    def entres_a_name_in_the_search_field(self):
        pass

    def selects_yes_option_in_the_active_dropdown(self):
        pass

    def clicks_search(self):
        pass

    def the_system_returns_all_active_users_containing_the_entered_name(self):
        pass

    def navigates_to_question_bank_progress_tab(self):
        pass

    def the_progress_for_that_specific_class_assignments_is_displayed_with_the_following_p1(self, p1 = ""):
        pass

    def to_filter_the_assignments_by_p1(self, p1 = ""):
        pass

    def there_are_unopened_assignments(self):
        pass

    def there_are_assignments_that_students_started_but_not_finished_yet(self):
        pass

    def sees_that_in_the_progress_column_for_the_started_assignments_is_displayed_a_grey_progress_bar(self):
        pass

    def there_are_assignments_completed_by_students(self):
        pass

    def sees_that_in_the_progress_column_the_finished_assignments_are_marked_as_complete(self):
        pass

    def teacher_navigates_to_question_bank_progress_tab(self):
        pass

    def the_progress_page_for_that_specific_assignment_is_displayed(self):
        pass

    def clicks_open_assessment_button_in_action_column_for_a_locked_assignment(self):
        pass

    def then_in_student_access_section_switches_on_the_assignment_toggle_button(self):
        pass

    def clicks_on_an_assignment_that_is_not_enabled_to_show_scores_to_students(self):
        pass

    def then_in_student_access_section_switches_on_the_results_toggle_button(self):
        pass

    def the_assignment_is_enabled_to_show_scores_to_students(self):
        pass

    def the_students_will_see_the_results_as_they_are_available(self):
        pass

    def teacher_navigates_to_question_bank_progress_tabspecific_assignmet_enter_scores_tab(self):
        pass

    def for_a_student_inserts_scores_for_every_question_or_part_of_the_quiz_in_their_specific_column(self):
        pass

    def try_to_insert_a_value_different_that_0_or_1_for_free_text_questions(self):
        pass

    def enter_scores_for_some_or_all_students(self):
        pass

    def clicks_save_scores_button(self):
        pass

    def the_entered_scores_are_saved(self):
        pass

    def navigates_to_question_bank_results_tab(self):
        pass

    def the_teacher_is_able_to_select_a_class_or_all_classes_to_view_the_results_for(self):
        pass

    def a_student_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def a_student_on_homepage(self):
        pass

    def the_student_lands_on_p1_homepage(self, p1 = ""):
        pass

    def student_fills_in_a_wrong_join_code_the_email_address_and_password(self):
        pass

    def an_error_message_regarding_the_invalid_join_code_is_thrown_and_the_enroll_button_is_inactive(self):
        pass

    def the_list_of_student_users(self, datatable = ""):
        pass

    def enroll_in_button_is_disabled_and_the_following_p1_should_be_thrown(self, p1 = ""):
        pass

    def student_fills_in_the_required_fields(self):
        pass

    def provides_a_wrong_join_code(self):
        pass

    def an_error_message_regarding_the_invalid_join_code_is_thrown(self):
        pass

    def student_fills_in_the_join_code(self):
        pass

    def student_checks_i_dont_have_an_email_address_option_and_fills_the_rest_of_the_required_fields(self):
        pass

    def a_world_history_teacher_on_the_login_page(self):
        pass


    def teacher_logs_in_and_lands_on_the_homepage(self):
        pass

    def a_calculus_teacher_on_the_login_page(self):
        pass

    def logs_in_and_lands_on_the_homepage_and_sees(self, p1 = ""):
        homepage_single_subject = self.homePage.is_homepage() and self.homePage.has_subject(p1)
        subjects_multiple = self.subjectsPage.is_multiple_subjects_page() and self.subjectsPage.has_subject_in_list(p1)

        assert (homepage_single_subject or subjects_multiple) is True




    def a_computer_science_principles_teacher_on_the_login_page(self):
        pass



    def a_us_history_teacher_on_the_login_page(self):
        pass

    def he_sees_only_teacher_modules_unit_assessments_and_qb_in_the_header_menu(self):
        pass

    def a_us_biology_teacher_on_the_apc_login_page(self):
        pass

    def he_sees_only_unit_assessments_and_qb_in_the_header_menu(self):
        pass

    def a_chemistry_teacher_on_the_login_page(self):
        pass



    def a_student_sees_their_assignments_in_the_todo_widget(self):
        pass

    def he_has_opened__not_started__no_lock_date_assigned_assessments(self):
        pass



    def he_clicks_on_the_units_unit_tests_link(self):
        pass



    def he_applies_p1(self, p1 = ""):
        pass

    def the_teacher_is_logged_in_apc(self):
        pass



    def a_teacher_opened_an_assignment_to_students(self):
        pass

    def sees_the_status_for_the_assigned_unopened_quiz_is_locked(self, locked = "Locked"):
        pass


    def student_begins_a_quiz(self):
        pass

    def selects_the_answers_and_clicks_the_save_progress_button_without_submitting_the_answers(self, save_progress = "Save Progress"):
        pass

    def the_selected_answers_are_saved(self):
        pass


    def the_questions_are_added_in_the_quiz(self):
        pass

    def the_questions_title_and_type_are_displayed_under_the_quiz_in_a_list(self):
        pass

    def next_to_each_question_buttons_to_change_the_order_in_the_list_and_delete_buttons_are_present(self):
        pass

    def the_user_is_a_qb_teacher(self):
        pass

    def the_user_is_creating_a_quiz(self):
        pass

    def adding_two_questions_that_share_a_stimulus(self):
        pass

    def the_quiz_will_show_that_there_is_a_passage_associated_with_the_two_questions(self):
        pass



    def he_clicks_on_assign_button(self):
        pass



    def he_sees_all_the_saved_quizzes(self):
        pass

    def gives_answers_for_all_the_questions_and_clicks_submit_button(self):
        pass

    def the_quiz_is_submitted(self):
        pass



    def the_progress_page_is_displayed_and_the_following__info_is_available(self, _info = "=info"):
        pass

    def the_results_page_is_displayed_and_the_following_p1_is_available(self, p1 = ""):
        pass

    def clicks_on_a_quizz(self):
        pass

    def a_student_on_the_results_tab_from_assessments(self):
        pass

    def a_next_button_is_available_to_navigate_to_the_next_question(self):
        pass



    def then_clicks_on_get_report(self):
        pass

    def class_performance_tab_is_opened(self):
        pass

    def he_clicks_on_get_all_reports_button(self):
        pass


    def a_student_is_on_the_login_page(self):
        pass


    def he_clicks_on_p1_button(self, p1 = ""):
        pass

    def teacher_is_redirected_to_question_bank_page__results_tab(self):
        pass

    def he_clicks_on_p1_button_in_the_topright_corner_of_the_class_progress_widget(self, p1 = ""):
        pass

    def he_is_redirected_to_my_classes_where_the_subject_is_preselected_in_the_subject_dropdown__httpsmyapcollegeboardorgcoursescreate_test_cd_where_test_cd_is_the_cb_subject_id_for_the_displayed_subject(self):
        pass

    def he_is_able_to_create_and_save_a_class_successfully(self):
        pass

    def he_clicks_in_the_widget_header_on_class_name(self):
        pass

    def there_is_no_class_created(self):
        pass

    def he_clicks_on_create_a_section_class_button_from_the_middle_of_the_widget(self):
        pass

    def teacher_is_redirected_to_apro_httpsmyapcollegeboardorgcoursescreate_test_cd(self):
        pass

    def he_sees_you_don_t_have_any_assignment_activities_yet_(self, you_don_t_have_any_assignment_activities_yet_ = "You don't have any assignment activities yet."):
        pass

    def teacher_sees_the_widget(self):
        pass

    def he_sees_p1_button_in_the_middle_of_the_widget(self, p1 = ""):
        pass

    def a_message_p1(self, p1 = ""):
        pass

    def it_is_the_exam_period(self):
        pass

    def he_sees_the_exam_tile_title_on_top_of_the_widget(self):
        pass

    def title_is_p1(self, p1 = ""):
        pass

    def he_can_see_exam_responses_tile(self):
        pass

    def its_not_the_exam_period(self):
        pass

    def he_clicks_on_exam_responses_tile(self):
        pass

    def a_popover_appears_having_2_columns_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def each_column_is_populated_with_student_that_responded_or_not_to_the_exam_decision_questions(self):
        pass

    def the_lists_could_have_545_names_showing_first_name_and_then_last_name_under_the_2_headings(self):
        pass

    def there_are_some_students_that_responded_to_exam_questions_and_some_that_not(self):
        pass

    def teacher_clicks_on_exam_response_tile(self):
        pass

    def the_he_sees_both_lists_alphabetically_ordered_by_first_name(self):
        pass

    def teacher_refreshes_class_widget(self):
        pass

    def the_p1_number_is_increased_by_1(self, p1 = ""):
        pass

    def students_name_is_displayed_in_the_popover_under_the_correct_column(self):
        pass

    def he_responded_to_the_exam_questions_by_logging_in_the_app(self):
        pass

    def he_can_see_in_the_monitor_ap_exam_responses_tile_the_final_deadline(self):
        pass

    def there_is_no_student_assigned_in_its_class(self):
        pass

    def he_sees_in_the_exam_responses_tile_p1(self, p1 = ""):
        pass

    def a_teacher_on_unit_assessments_tab__results(self):
        pass

    def teacher_assigned_an_assessment_to_a_class(self):
        pass

    def the_students_submitted_their_responses(self):
        pass

    def sees_on_unit_assessments_page_next_steps_cards(self):
        pass

    def a_least_two_questions_assesses_the_same_block(self):
        pass

    def there_are_still_slots_remaining(self):
        pass

    def overall_unit_test_performance_s_in_red_range(self):
        pass

    def a_link_to_teacher_module_is_available_on_the_card(self):
        pass

    def there_are_blocks_with_low_performance_on_many_questions(self):
        pass

    def the_average_performance_percent_is_tie_for_two_or_more_blocks(self):
        pass

    def show_first_the_next_step_card_for_lower_block_number(self):
        pass

    def test_includes_fr_qs_and_they_have_not_yet_been_scoredapproved(self):
        pass

    def the_criteria_has_been_met(self):
        pass

    def calculate_performance_based_on_mc_qs_and_show_cards(self):
        pass

    def he_sees_the_p1_tile(self, p1 = ""):
        pass

    def only_some_students_have_submitted_results(self):
        pass

    def show_cards_based_on_students_scored_to_date(self):
        pass

    def there_are_no_next_steps_cards_to_show_based_on_criteria(self):
        pass

    def the_next_steps_section_is_not_displayed(self):
        pass

    def sees_the_next_step_card_header_focus_topic_topic(self):
        pass

    def a_popup_with_the_questions_that_measure_the_performance_marker_is_displayed(self):
        pass

    def next_to_each_question_in_the_popup_is_displayed_a_performance_marker(self):
        pass

    def at_least_one_assessment_that_meets_the_criteria_of_having_80_of_the_class_having_the_assignment_fully_scored(self):
        pass

    def he_can_see_all_the_units_collapsed(self):
        pass

    def a_unit_is_expanded(self):
        pass

    def expand_all_is_clicked(self):
        pass

    def an_educator_admin_user_on_login_page(self):
        pass

    def the_educator_admin_logs_in(self):
        pass

    def he_lands_on_the_multisubject_page(self):
        pass

    def an_educator_admin_user_logs_in_the_application(self):
        pass

    def an_educator_admin_user_on_the_subject_homepage(self):
        pass

    def no_value_is_selected_for_school_and_teacher_filters(self):
        pass

    def the_class_preview_widget_will_display_the_following_message_p1(self, p1 = ""):
        pass

    def p1_is_displayed(self, p1 = ""):
        pass

    def the_student_logs_in(self):
        pass

    def clicks_on_usage_tab(self):
        pass

    def an_educator_admin_on_usage_page(self):
        pass

    def the_user_is_associated_with_only_one_district(self):
        pass

    def the_district_is_selected_by_default(self):
        pass

    def the_usage_table_displays_all_data_associated_with_the_selected_district(self):
        pass

    def the_educator_admin_selects_a_subject(self):
        pass

    def applies_a_filter_for_district_and_schools__classes(self):
        pass

    def the_calculations_for_the_displayed_results_are_at_the_subject_level_and_subject_to_the_selected_filter_values(self):
        pass

    def the_filter_values_should_be_retained_within_the_session_when_moving_between_usage_ua_or_qb_results_page(self):
        pass

    def for_the_selected_classes_arent_quizzes_assigned(self):
        pass

    def the_question_bank_column_is_not_displayed_in_the_usage_table(self):
        pass

    def sees_that_the_name_column_displays_the_teacher_names_for_the_selected_classes(self):
        pass

    def selects_a_few_classes_from_the_schools__classes_filter(self):
        pass

    def the_unit_assessments_column_is_not_displayed_in_the_usage_table(self):
        pass

    def the_list_of_teachers_teacher(self, datatable = ""):
        pass

    def the_message_is_message(self):
        pass

    def the_assign_button_is_not_displayed(self):
        pass

    def the_teacher_is_able_to_click_the_assign_button(self):
        pass

    def a_teacher_on_teacher_module_page(self):
        pass

    def a_biology_teacher_on_the_homepage(self):
        pass

    def he_filters_the_qb_items_by_the_parent_skill_orand_by_the_parent_practice_orand_by_the_parent_unit(self):
        pass

    def teacher_navigates_to_question_bank_progress_tab(self):
        pass

    def a_student_on_the_class_enrollment_page(self):
        pass

    def student_fills_in_the_join_code_and_the_rest_of_the_required_fields(self):
        pass

    def provides_an_email_addres_that_is_already_in_use(self):
        pass

    def an_error_message_regarding_the_fact_that_the_email_is_already_used_is_thrown(self):
        pass

    def doesnt_fill_in_all_the_required_fields(self):
        pass

    def logs_in_and_lands_on_the_homepage_and_sees_p1(self, p1 = ""):
        pass

    def he_is_redirected_to_the_site_terms_and_conditions_page(self):
        pass

    def he_enters_data_in_all_mandatory_fields(self):
        pass

    def he_is_in_fr_create_form_specify_metadata_tab(self):
        pass

    def student_have_assignments_in_different_states(self):
        pass

    def a_teacher_on_question_bank_results_page(self):
        pass

    def he_is_redirected_to_the_assessments_page_with_assign_tab_opened(self):
        pass

    def he_clicks_on_the_units_unit_tests_link(self):
        pass

    def he_sees_unit_guide_hiperlink_under_unit_title(self):
        pass

    def he_sees_the_list_of_building_blocks_under_unit_blocks_section_without_their_resources(self):
        pass

    def p1_button_is_available_at_the_bottom_of_the_widget(self, p1 = ""):
        pass

    def the_teacher_is_redirected_to_teacher_modules_section_as_defined_in_the_fym_taa_sheet_of_the_metadata_google_doc(self):
        pass

    def specific_teaching_module_is_expanded_to_show_its_content(self):
        pass

    def the_widget_shows_the_content_for_the_next_unit(self):
        pass

    def he_clicks_on_the_p1(self, p1 = ""):
        pass

    def he_clicks_to_expand_a_unit(self):
        pass

    def he_go_back_to_the_homepage(self):
        pass

    def a_whc_teacher_is_on_the_homepage(self):
        pass

    def he_sees_the_first_unit_from_the_list_displayed_in_the_widget(self):
        pass

    def he_clicks_on_the_units_tab(self):
        pass

    def he_clicks_on_collapse_all(self):
        pass

    def filters_set_to_unitp1(self, p1 = ""):
        pass

    def he_is_a_teacher_of_multiple_subjects(self):
        pass

    def he_clicks_on_the_current_subject_to_open_the_dropdown(self):
        pass

    def he_sees_all_the_subjects_the_teacher_teaches_based_on_epl_authorization(self):
        pass

    def the_content_of_the_page_is_updated_according_to_the_selected_subject(self):
        pass

    def a_section_has_been_expanded_for_a_taa(self):
        pass

    def he_navigate_to_a_different_page(self):
        pass

    def then_he_goes_back_to_teacher_module_page(self):
        pass

    def he_sees_the_last_section_accessed_expanded_in_the_subjects_taa(self):
        pass

    def he_navigates_through_different_subjects(self):
        pass

    def in_each_subject_he_expanded_a_section_for_a_taa(self):
        pass

    def he_navigates_back_to_each_subject_to_teacher_module_page(self):
        pass

    def he_uses_the_same_device(self):
        pass

    def he_sees_the_last_section_accessed_expanded_for_each_subject(self):
        pass

    def he_navigates_to_teacher_module_page_for_the_first_time(self):
        pass

    def all_sections_are_collapsed(self):
        pass

    def he_logs_in_the_application_from_a_different_device_or_browser(self):
        pass

    def he_navigates_to_teacher_module_page(self):
        pass

    def he_wont_see_the_last_accessed_section_from_a_different_device_or_browser(self):
        pass

    def any_date_and_time_earlier_than_the_current_moment_are_disabled_and_cannot_be_selected(self):
        pass

    def p1_button_is_displayed(self, p1 = ""):
        pass

    def the_list_is_filtered_and_displays_only_the_correct_questions(self):
        pass

    def the_teacher_is_logged_in_the_application(self):
        pass

    def teacher_navigates_to_question_bank_page(self):
        pass

    def the_user_is_editing_a_question(self):
        pass

    def he_wants_to_exit_the_editor(self):
        pass

    def he_clicks_the_button_p1(self, p1 = ""):
        pass

    def in_the_assignments_page_the_begin_button_becomes_continue_button(self):
        pass

    def he_clicks_p1_button_for_two_existing_questions_in_the_list(self, p1 = ""):
        pass

    def the_quiz_gets_assigned_to_a_class(self):
        pass

    def is_no_longer_displayed_in_assignments_tab(self):
        pass

    def he_applies_filters_form_p1_section(self, p1 = ""):
        pass

    def are_displayed_only_the_questions_that_match_the_applied_filter(self):
        pass

    def the_teacher_opens_an_assignment_to_students(self):
        pass

    def the_assessments_page_is_displayed(self):
        pass

    def assignments_tab_is_displayed_by_default_with_the_following_p1(self, datatable = "||", p1 = "p1"):
        pass

    def sees_the_status_for_the_open_assignment_is_opened(self, opened = "Opened"):
        pass

    def no_button_is_available_in_the_action_column_to_begin_the_quiz(self):
        pass


    def teacher_clicks_p1_button_for_two_existing_questions_in_the_list(self, p1 = ""):
        pass


    def he_adds_two_or_more_questions_that_share_the_same_stimulus_in_order_to_create_a_new_quiz(self):
        pass

    def the_questions_are_added_and_grouped_under_the_same_stimulus(self):
        pass


    def a_pdf_file_is_opened_in_another_tab_containing_the_quiz_questions_results_and_points_plus_all_the_questions_listed_with_the_correctincorrect_answer(self):
        pass


    def a_pdf_file_is_opened_in_another_tab_containing_the_quiz_questions_results_and_points_for_all_students_plus_all_the_questions_listed_for_each_student_with_the_correctincorrect_answers(self):
        pass


    def he_looks_at_the_homepage(self):
        pass

    def he_sees_the_class_widget_next_to_unit_widget(self):
        pass

    def the_widget_has_class_name_as_hyperlink(self):
        pass

    def there_are_arrows_in_the_topright_corner_of_the_widget_to_navigate_through_classes(self):
        pass


    def he_clicks_on_p1_button_in_the_topright_corner_of_the_widget(self, p1 = ""):
        pass

    def he_is_redirected_to_my_classes_where_the_subject_is_preselected_in_the_subject_dropdown(self):
        pass


    def he_tries_to_navigate_through_classes_using_arrows(self):
        pass

    def he_sees_the_arrows_are_not_available_since_there_is_only_1_class(self):
        pass


    def he_clicks_on_create_class_button_from_the_middle_of_the_widget(self):
        pass

    def teacher_is_redirected_to_my_classes(self):
       pass

    def he_sees(self):
        pass


    def he_did_not_respond_to_exam_questions(self):
        pass


    def is_enrolled_in_fym_subjects(self):
        pass

    def is_displayed_a_next_step_card_for_teaching_and_assessing(self):
        pass

    def this_card_is_displays_first(self):
        pass


    def the_correspondent_next_steps_cars_are_sorted_from_lowest_to_highest(self):
        pass



    def sees_the_next_step_card_header_focus_block_block(self):
        pass


    def under_the_title_sees_resource_links_in_this_order_if_they_exist_for_the_block_khan_academy_teacher_lesson_plan_student_handout_focus_quiz(self):
        pass



    def clicks_on_a_performance_marker_on_a_next_step_card(self):
        pass

    def clicks_on_assign_button_for_a_quiz_created_by_himself(self):
        pass

    def the_teacher_creates_a_new_quiz(self):
        pass

    def after_the_quiz_is_created_clicks_on_assign_button(self):
        pass

    def on_the_displayed_assign_popup_sees_that_the_scramble_question_option_is_available(self):
        pass

    def a_teacher_assigns_a_quiz_with_scramble_question_option_on_to_two_classes(self):
        pass

    def two_students_one_from_each_class_login_the_application(self):
        pass

    def go_to_assessments_tab(self):
        pass

    def click_on_begin_button_for_the_quiz_with_scramble_questions(self):
        pass

    def each_student_sees_the_questions_in_a_different_order(self):
        pass

    def the_teacher_goes_to_question_bank_progress_tab(self):
        pass

    def opens_each_quiz_to_see_its_enter_scores_tab(self):
        pass

    def observes_that_the_questions_order_is_different_for_the_two_quizzes(self):
        pass

    def a_teacher_taking_a_certification_test(self):
        pass

    def the_students_from_the_two_classes_submit_the_responses_for_the_quiz(self):
        pass

    def the_teacher_goes_to_question_bank_results_page(self):
        pass

    def clicks_on_each_quiz_to_see_the_class_performance_tab(self):
        pass

    def opens_each_quiz_and_looks_at_the_questions_order_in_students_performance_tab(self):
        pass

    def a_student_from_one_of_the_classes_logs_in(self):
        pass

    def takes_the_quiz_and_submits_the_responses(self):
        pass

    def goes_to_assessments_progress_tab_and_click_on_review_button(self):
        pass

    def observes_that_the_question_order_from_the_quiz_player_is_maintained_in_progress_preview_popup(self):
        pass

    def goes_to_assessments_results_page_and_clicks_on_the_quiz(self):
        pass

    def observes_that_the_questions_order_from_the_quiz_player_is_maintained_in_results_tab(self):
        pass

    def logs_in_and_sees_the_mslp_page(self):
        pass

    def a_teacher_on_the_apc_login_page(self):
        pass

    def a_teacher_on_the_ros_login_page(self):
        pass

    def user_is_redirected_to_apc(self):
        pass

    def a_user_logged_in_the_application_apc(self):
        pass

    def the_user_logs_out_of_the_application(self):
        pass

    def the_user_is_logged_out(self):
        pass

    def redirected_to_the_ros_login_page(self):
        pass

    def he_introduces_wrong_username_or_password(self):
        pass

    def he_is_redirected_to_ros_page_asking_to_introduce_credentials_again(self):
        pass

    def notification_is_displayed_message(self):
        pass

    def he_selects_forgot_username_hyperlink(self):
        pass

    def he_is_redirected_to_cb(self, free_text = ""):
        pass

    def he_selects_the_forgot_password_hyperlink(self):
        pass

    def he_is_redirected_to_cb_page(self, free_text = ""):
        pass

    def he_selects_sign_up_hyperlink(self):
        pass

    def he_opens_a_new_tab_in_the_browser(self):
        pass

    def he_navigates_to_my_ap(self):
        pass

    def the_teacher_is_automatically_logged_in_my_ap(self):
        pass

    def the_teacher_has_multiple_subjects(self):
        pass

    def a_computer_science_principles_teacher_on_the_apc_login_page(self):
        pass

    def logs_in_using_sso(self):
        pass

    def lands_on_the_homepage(self):
        pass

    def a_us_history_teacher_on_the_apc_login_page(self):
        pass

    def a_chemistry_teacher_on_the_apc_login_page(self):
        pass

    def a_whc_teacher_on_the_apc_login_page(self):
        pass

    def logs_is_using_sso(self):
        pass

    def the_teacher_has_one_subject(self):
        pass

    def logs_in_and_sees_the_homepage_for_that_subject(self):
        pass

    def the_teacher_completes_the_answers_for_all_the_questions(self):
        pass

    def the_teacher_does_not_complete_all_the_answers(self):
        pass

    def the_teacher_fills_in_all_the_answers(self):
        pass

    def the_teacher_presses_on_submit_button(self):
        pass

    def a_popup_with_two_yes_no_options_appears(self, free_text = ""):
        pass

    def has_the_same_layout_and_look_as_the_one_for_students_quiz(self):
        pass

    def the_answers_should_be_submitted(self):
        pass

    def leaves_the_test_presses_on_back_button_without_submitting_the_answers(self):
        pass

    def the_answers_should_be_saved(self):
        pass

    def the_status_of_the_test_should_be_not_finished(self):
        pass

    def the_teacher_completes_the_correct_answers_for_all_the_questions(self):
        pass

    def the_status_of_the_test_should_be_passed(self):
        pass

    def a_teacher_on_the_content_manager_page(self):
        pass

    def the_teacher_selects_a_library_from_the_dropdown(self):
        pass

    def the_import_package_button_appears_and_is_available(self):
        pass

    def the_import_package_button_is_available(self):
        pass

    def the_teacher_selected_one_library(self):
        pass

    def the_teacher_presses_on_the_import_package_button(self):
        pass

    def a_browse_popup_appears(self):
        pass

    def it_filters_automatically_only_zip_files(self):
        pass

    def the_teacher_selects_a_package_for_import(self):
        pass

    def the_package_is_imported_sent_for_validation__backend(self):
        pass

    def the_import_button_changes_to_display_progress_and_status(self):
        pass

    def he_adds_more_questions_to_the_saved_quiz(self):
        pass

    def clicks_on_cancel_changes_button(self):
        pass

    def the_changes_done_to_the_saved_quiz_are_canceled(self):
        pass

    def the_questions_are_not_added_to_the_quiz(self):
        pass

    def he_removes_a_few_questions_from_the_saved_quiz(self):
        pass

    def the_changes_are_canceled(self):
        pass

    def the_questions_are_not_removed_from_the_quiz(self):
        pass

    def he_clicks_on_delete_assessment_button(self):
        pass

    def the_quiz_is_deleted(self):
        pass

    def is_not_displayed_in_progress_tab(self):
        pass

    def clicks_on_my_classes_tab(self):
        pass

    def is_redirected_to_my_classes_page_from_my_ap_application(self, free_text = ""):
        pass

    def creates_a_class_in_apro_for_the_selected_subject(self):
        pass

    def goes_back_to_apc(self):
        pass

    def is_redirected_back_to_apc(self):
        pass

    def the_created_classes_are_available_also_in_the_class_progress_widget(self):
        pass

    def after_the_redirect_to_my_ap_edits_a_class(self):
        pass

    def he_sees_the_modification_made_to_the_class_in_class_widget(self):
        pass

    def a_teacher_on_my_classes_tab(self):
        pass

    def he_fills_in_the_mandatory_fields_school_and_name(self):
        pass

    def create_button_becomes_enabled(self):
        pass

    def he_is_able_to_search_and_add_students_to_the_class_roster(self):
        pass

    def he_fills_in_all_the_mandatory_fields_and_clicks_on_create_button(self):
        pass

    def the_class_is_created_and_added_in_my_classes_column(self):
        pass

    def he_clicks_on_a_class_from_my_classes_column(self):
        pass

    def the_class_displays_all_its_attributes_name_edit_button_active_toggle_join_code_roster_and_the_enroll_members_button(self):
        pass

    def a_teacher_viewing_a_class_from_my_classes_tab(self):
        pass

    def he_clicks_on_enroll_members_button(self):
        pass

    def he_switches_the_toggle_from_active_to_archived_and_clicks_on_save_button(self):
        pass

    def class_is_deleted_from_my_classes_tab(self):
        pass

    def he_creates_a_new_class_in_my_classes_tab(self):
        pass

    def navigate_to_homepage(self):
        pass

    def the_newly_created_class_is_displayed_in_class_widget(self):
        pass

    def a_teacher_on_the_homepage_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_inspect_the_top_banner_of_the_screen(self):
        pass

    def an_info_text_that_reads_your_guide_to_the_content_skills_crosswalks_instructional_strategies_and_recommended_resources_across_this_course_(self, your_guide_to_the_content_skills_crosswalks_instructional_strategies_and_recommended_resources_across_this_course_ = "Your guide to the content, skills, crosswalks, instructional strategies and recommended resources across this course."):
        pass

    def the_teacher_sees_course_resources_link_preceded_by_a_pencil_icon(self):
        pass

    def a_teacher_on_the_units_page_of_a_p1_subject(self, p1 = "p1"):
        pass

    def a_p2_teacher_on_the_p1_page_of_an_ap_subject(self, p1 = "p1", p2 = "p2"):
        pass

    def he_clicks_on_course_resources_link(self):
        pass

    def the_teachers_guide_pdf_specific_for_that_subject_opens_in_a_new_tab(self):
        pass

    def a_teacher_on_the_p1_page_of_each_pre_ap_subject(self, p1 = "p1"):
        pass

    def the_specific_course_resources_popup_is_displayed_in_a_modal_way(self):
        pass

    def a_teacher_on_the_assign_tab_of_ua(self):
        pass

    def the_teacher_assigns_an_assessment_to_one_or_multiple_class(self):
        pass

    def the_teacher_sees_the_time_limit_toggle(self):
        pass

    def the_teacher_can_activate_and_fill_in_the_time_limit(self):
        pass

    def a_teacher_on_create_tab_of_a_subject_qb_page(self):
        pass

    def the_teacher_clicks_on_p1_button_of_any_question(self, p1 = ""):
        pass

    def the_question_content_is_previewed_in_a_popup_each_question_on_one_page(self):
        pass

    def p1_and_previous_buttons_are_present_to_navigate_to_the_nextprevious_question(self, p1 = "", previous = "Previous"):
        pass

    def the_teacher_sees_the_accnum_and_platform_fields_in_the_items_table(self):
        pass

    def the_teacher_sets_the_value_in_the_db_for_accnum_and_platform(self):
        pass

    def the_accnum_and_id_fields_are_populated_with_the_inserted_values(self):
        pass

    def the_accnum_and_id_fields_are_populated_with_the_imported_values(self):
        pass

    def adds_a_question_to_a_quiz(self):
        pass

    def saves_the_quiz(self):
        pass

    def an_icon_indicates_that_the_question_has_been_added_to_a_quiz(self):
        pass

    def a_teacher_is_on_units_page(self):
        pass

    def he_opens_each_assessment_unit_testfocus_quiz(self):
        pass

    def he_is_redirected_to_correct_assessment_preview(self):
        pass

    def the_id_from_the_url_matched_the_id_from_the_metadata_importer_sheet(self):
        pass

    def whe(self):
        pass

    def a_teacher_verifies_the_number_of_submitted_tests_is_greater_than_zero(self):
        pass

    def a_teacher_is_on_the_question_bank_page(self):
        pass

    def a_teacher_clicks_on_the_progress_tab(self):
        pass

    def a_teacher_clicks_on_its_default_class(self):
        pass

    def the_last_expanded_teacher_modules_modules_are_remembered_and_the_outline_is_expanded(self):
        pass

    def he_clicks_on_scoring_guide_within_the_unit_widget(self):
        pass

    def scoring_guide_pdf_file_loads_in_a_new_browser_tab(self):
        pass

    def he_is_able_to_view_all_units_and_resources_for_each_unit(self):
        pass

    def filters_big_idea_enduring_understanding_learning_objective_historical_thinking_skills_should_appear_in_the_left_side_of_the_page(self):
        pass

    def the_unit_gets_expanded(self):
        pass

    def check_the_resources_for_a_key_concept(self):
        pass

    def he_is_able_to_see_combination_of_resources_source_sets_student_handouts_crosswalks_assessments(self):
        pass

    def he_clicks_on_performance_task_from_unit_resources_within_a_unit(self):
        pass

    def he_clicks_on_expand_all_button_at_the_top_of_the_screen(self):
        pass

    def both_pre_ap_and_ap_sections_should_be_expanded_and_display_the_available_subjects(self):
        pass

    def he_expanded_all_sections(self):
        pass

    def both_pre_ap_and_ap_sections_should_be_collapsed_with_only_the_section_names_exposed(self):
        pass

    def there_is_a_key_concept_that_has_a_source_set_assigned(self):
        pass

    def source_set_pdf_loads_in_a_new_browser_tab(self):
        pass

    def scoring_guide_pdf_loads_in_a_new_browser_tab(self):
        pass

    def there_is_a_key_concept_that_has_a_student_handout_as_resource(self):
        pass

    def the_student_handout_pdf_file_loads_in_a_new_browser_tab(self):
        pass

    def he_clicks_on_it(self):
        pass

    def specific_assessment_is_listed(self):
        pass

    def the_filters_are_set_to_unitp1_and_key_concept_p2(self, p1 = "", p2 = ""):
        pass

    def there_are_key_concepts_that_have_tba_enduring_understanding(self):
        pass

    def he_filters_by_enduring_understanding(self):
        pass

    def only_the_units_with_those_enduring_understanding_concepts_assigned_are_displayed_on_the_screen(self):
        pass

    def he_navigate_to_a_different_tab(self):
        pass

    def then_he_goes_back_to_teacher_modules_tab(self):
        pass

    def he_sees_the_module_previously_expanded(self):
        pass

    def he_navigates_through_different_p1_subjects(self, p1 = "p1"):
        pass

    def in_each_subject_he_expanded_a_certain_module(self):
        pass

    def he_navigates_to_another_teacher_modules_subject_page(self):
        pass

    def he_navigates_to_teacher_modules_page_for_the_first_time(self):
        pass

    def a_teacher_on_my_subjects_page(self):
        pass

    def he_navigates_to_teacher_modules_page(self):
        pass

    def he_has_added_a_question_to_a_new_quiz(self):
        pass

    def he_clicks_on_p1_button_in_the_topright_corner_of_the_class_widget(self, p1 = ""):
        pass

    def he_is_redirected_to_ros_class_management_page_where_he_can_see_the_subject_table_and_its_associated_classes(self):
        pass

    def he_clicks_on_create_class_button_from_the_middle_of_the_class_widget(self):
        pass

    def teacher_is_redirected_to_ros_class_management_page(self):
        pass

    def he_can_see_exam_decision_tile(self):
        pass

    def the_message_is_p3(self, p3 = "p3"):
        pass

    def a_pre_ap_only_teacher_on_the_login_page(self):
        pass

    def teacher_clicks_sign_in_button(self):
        pass

    def logs_in_and_lands_on_the_course_homepage_and_sees_p1(self, p1 = ""):
        pass

    def an_ap_only_teacher_on_the_login_page(self):
        pass

    def the_teacher_has_just_one_subject(self):
        pass

    def a_teacher_with_both_pre_ap_and_ap_subjects_on_the_login_page(self):
        pass

    def logs_in_and_lands_on_my_subjects_page_where_he_can_see_all_his_pre_ap_and_ap_subjects(self):
        pass

    def a_teacher_with_multiple_ap_subjects_on_the_login_page(self):
        pass

    def logs_in_and_lands_on_my_subjects_page_where_he_can_see_all_his_ap_subjects(self):
        pass

    def a_teacher_with_multiple_pre_ap_subjects_on_the_login_page(self):
        pass

    def logs_in_and_lands_on_my_subjects_page_where_he_can_see_the_all_his_pre_ap_subjects(self):
        pass

    def a_teacher_with_one_pre_ap_and_one_ap_subject_on_the_login_page(self):
        pass

    def logs_in_and_lands_on_my_subjects_page_where_he_can_see_both_his_pre_ap_and_ap_subjects(self):
        pass

    def he_lands_on_my_subjects_page_where_he_can_see_2_subject_sections_first_ap_and_then_pre_ap(self):
        pass

    def no_ap_subjects(self):
        pass

    def no_pre_ap_subjects(self):
        pass

    def he_lands_on_my_subjects_page_where_he_can_see_the_pre_ap_courses_he_has_access_to_onscreen(self):
        pass

    def he_lands_on_my_subjects_page_where_he_can_see_the_ap_courses_he_has_access_to_onscreen(self):
        pass

    def he_lands_on_my_subjects_page_where_he_can_see_the_pre_ap_subjects_grouped_under_the_pre_ap_section(self):
        pass

    def the_ap_subjects_grouped_under_the_ap_section(self):
        pass

    def the_pre_ap_section_is_not_displayed(self):
        pass

    def the_ap_section_is_not_displayed(self):
        pass

    def he_lands_on_my_subjects_page_where_he_can_see_the_ap_subjects_displayed_on_load_not_withing_an_accordion(self):
        pass

    def he_lands_on_my_subjects_page_where_he_can_see_the_pre_ap_subjects_displayed_on_load_not_withing_an_accordion(self):
        pass

    def he_lands_on_my_subjects_page_where_both_ap_and_pre_ap_sections_are_collapsed_by_default(self):
        pass

    def a_teacher_with_access_to_two_pre_ap_subject_on_the_login_page(self):
        pass

    def logs_in_and_lands_on_my_subjects_page_where_he_cannot_see_the_other_pre_ap_subjects_has_not_access_to(self):
        pass

    def a_teacher_with_multiple_pre_ap_subjects_on_the_homepage_of_a_subject(self):
        pass

    def navigates_to_user_profile_menu__my_subjects_option(self):
        pass

    def a_teacher_with_multiple_ap_subjects_on_the_homepage_of_a_subject(self):
        pass

    def lands_on_my_subjects_page_where_he_can_see_all_the_ap_subjects_for_which_he_was_granted_access(self):
        pass

    def a_teacher_with_multiple_pre_ap_and_ap_subjects_on_the_homepage_of_a_subject(self):
        pass

    def lands_on_my_subjects_page_where_he_can_see_the_pre_ap_and_ap_sections_expanded(self):
        pass

    def all_the_pre_ap_and_ap_subjects_for_which_he_was_granted_access(self):
        pass

    def lands_on_my_subjects_page_where_he_does_not_see_my_classes_button_near_the_pre_ap_header(self):
        pass

    def a_teacher_on_a_pre_ap_subject_homepage(self):
        pass

    def lands_on_my_subjects_page_where_he_does_not_see_at_all_my_classes_button(self):
        pass

    def lands_on_my_subjects_page_where_he_can_see_the_pre_ap_subjects_without_my_classes_button(self):
        pass

    def lands_on_my_subjects_page_where_he_does_not_see_my_classes_button_near_the_ap_header(self):
        pass

    def the_pre_ap_section_without_my_classes_button(self):
        pass

    def he_lands_on_my_subjects_page_where_he_does_not_see_my_classes_button_near_my_subjects_header(self):
        pass

    def a_teacher_on_a_ap_subject_homepage(self):
        pass

    def lands_on_my_subjects_page_where_he_can_see_the_ap_subjects_without_my_classes_button(self):
        pass

    def lands_on_my_subjects_page_where_my_classes_button_is_not_displayed(self):
        pass

    def ap_subjects_but_no_classes_yet(self):
        pass

    def the_teacher_has_pre_ap_subjects_and_classes(self):
        pass


    def ap_subjects_and_classes(self):
        pass

    def the_teacher_has_only_pre_ap_subjects_and_no_classes_assigned(self):
        pass

    def the_teacher_has_pre_ap_subjects_but_no_classes_yet(self):
        pass

    def the_teacher_has_only_ap_subjects_and_no_classes_assigned(self):
        pass

    def the_teacher_has_only_ap_subjects_with_classes_assigned(self):
        pass

    def teacher_fills_in_p1_and_p2(self, p1 = "", p2 = "", datatable = "||"):
        pass

    def teacher_lands_on_the_selected_course_homepage_and_sees_p1_as_page_title(self, p1 = ""):
        pass

    def teacher_lands_on_the_course_homepage_and_sees_p1_as_page_title(self, p1 = ""):
        pass

    def he_clicks_on_p1(self, p1 = "", free_text = "", datatable = "||"):
        pass

    def the_teacher_has_multiple_pre_ap_subjects_including_p1(self, p1 = ""):
        pass

    def a_pre_ap_teacher_on_the_login_page(self):
        pass

    def logs_in_and_is_redirected_to_the_appropriate_course_homepage_p1(self, p1 = ""):
        pass

    def a_teacher_on_the_course_homepage_of_a_pre_ap_subject(self):
        pass

    def the_teacher_has_multiple_pre_ap_subjects(self):
        pass

    def he_selects_other_subject_from_the_global_navigation_drop_down(self):
        pass

    def a_teacher_with_access_to_two_pre_ap_subject_on_a_course_homepage(self):
        pass

    def the_teacher_is_enrolled_in_a_school_that_has_all_the_pre_ap_subjects_in_its_curriculum(self):
        pass

    def he_clicks_on_the_global_navigation_drop_down(self):
        pass

    def the_teacher_cannot_see_all_the_pre_ap_subjects_of_the_school(self):
        pass

    def he_sees_only_the_subjects_he_has_been_provisioned_access_for_individually(self):
        pass

    def he_sees_the_following_modules_home_units_assessments_teacher_modules_and_my_classes_in_this_order(self):
        pass

    def he_inspects_the_navigation_bar(self):
        pass

    def teacher_on_the_course_homepage_of_a_pre_ap_subject(self):
        pass

    def a_teacher_that_has_both_pre_ap_and_ap_subjects_on_my_subjects_page(self):
        pass

    def a_teacher_on_the_course_homepage_of_an_ap_subject(self):
        pass

    def the_teacher_has_both_ap_and_pre_ap_subjects(self):
        pass

    def he_selects_a_pre_ap_subject_from_the_global_navigation_drop_down(self):
        pass

    def the_teacher_has_assigned_only_pre_ap_subjects(self):
        pass

    def teacher_on_the_course_homepage_of_an_ap_subject(self):
        pass

    def the_teacher_has_assigned_only_ap_subjects(self):
        pass

    def he_sees_the_following_modules_home_units_teacher_modules_unit_assessments_question_bank_and_my_classes_in_this_order(self):
        pass

    def a_pre_ap_and_ap_teacher_on_the_course_homepage_of_an_ap_subject(self):
        pass

    def the_teacher_has_the_following_modules_home_units_teacher_modules_unit_assessments_question_bank_and_my_classes(self):
        pass

    def he_switches_to_a_pre_ap_course_from_the_global_navigation_drop_down(self):
        pass

    def the_top_navigation_changes_to_home_units_assessments_teacher_modules_and_my_classes_in_this_order(self):
        pass

    def a_pre_ap_and_ap_teacher_on_the_course_homepage_of_a_pre_ap_subject(self):
        pass

    def the_teacher_has_the_following_modules_home_units_assessments_teacher_modules_and_my_classes(self):
        pass

    def he_switches_to_an_ap_course_from_the_global_navigation_drop_down(self):
        pass

    def the_top_navigation_changes_to_home_units_teacher_modules_unit_assessments_question_bank_and_my_classes_in_this_order(self):
        pass

    def a_pre_ap_and_ap_teacher_on_my_subjects_page(self):
        pass

    def he_chooses_a_pre_ap_subject(self):
        pass

    def he_chooses_an_ap_subject(self):
        pass

    def he_lands_on_the_course_homepage_of_the_selected_subject(self):
        pass

    def sees_the_following_top_navigation_elements_home_units_teacher_modules_unit_assessments_question_bank_and_my_classes_in_this_order(self):
        pass

    def sees_the_following_top_navigation_elements_home_units_assessments_teacher_modules_and_my_classes_in_this_order(self):
        pass

    def a_teacher_on_the_homepage_of_pre_ap_subject(self):
        pass



    def teacher_inspects_the_class_widget(self):
        pass

    def there_is_no_class_created_for_that_subject(self):
        pass

    def a_teacher_on_the_homepage_of_a_pre_ap_subject(self):
        pass

    def there_is_no_class_created_for_that_subject(self):
        pass

    def the_teacher_is_redirected_to_ros_class_management_page_where_he_is_able_to_create_and_save_a_classes_successfully(self):
        pass

    def a_pre_ap_teacher_on_ros_class_management_page(self):
        pass

    def he_creates_a_class_using_add_section_option(self, add_section = "Add Section"):
        pass

    def the_teacher_is_redirected_to_pre_ap_subject_homepage_where_he_is_able_to_see_the_created_class_in_class_widget(self):
        pass

    def he_clicks_on_p1_button_from_the_top_navigation_bar(self, p1 = ""):
        pass

    def the_teacher_is_redirected_to_ros_class_management_page_where_he_can_create_new_classes_for_that_subject(self):
        pass

    def a_pre_ap_teacher_on_the_p1_subtab_of_the_assessments_tab(self, p1 = "p1"):
        pass

    def he_clicks_on_create_class_p2(self, p2 = "p2"):
        pass

    def the_created_classes_are_visible_in_apc(self):
        pass

    def teacher_is_redirected_to_ros_class_management_page_where_he_is_able_to_create_and_save_classes_successfully(self):
        pass

    def there_is_no_class_created_for_the_selected_pre_ap_subject(self):
        pass

    def a_pre_ap_teacher_with_classes_on_ros_class_management_page(self):
        pass

    def he_edits_class_name(self):
        pass

    def goes_back_to_pre_ap_subject_homepage(self):
        pass

    def the_edited_class_name_is_displayed_in_the_widget(self):
        pass

    def a_teacher_on_the_p1_homepage(self, p1 = "p1"):
        pass

    def he_clicks_on_any_of_the_resources_links_displayed(self):
        pass

    def a_pdf_is_downloaded_to_the_default_downloads_location_of_the_machine(self):
        pass

    def a_teacher_with_multiple_pre_ap_courses_on_my_subjects_page(self):
        pass

    def he_is_redirected_to_the_appropriate_course_homepage_p1(self, p1 = ""):
        pass

    def he_clicks_on_p2_option(self, p2 = "p1", datatable = "||"):
        pass

    def he_lands_on_my_subjects_page_where_collapse_all_and_expand_all_buttons_are_not_displayed(self):
        pass

    def he_clicks_on_units_tab(self):
        pass

    def a_pre_ap_whg_teacher_is_on_the_units_page(self):
        pass

    def he_clicks_on_source_sets(self):
        pass

    def he_clicks_on_unit_guide_within_the_unit_widget(self):
        pass

    def the_teacher_clicks_on_it(self):
        pass

    def there_is_a_key_concept_that_has_an_assessment_as_resource(self):
        pass

    def he_clicks_on_the_arrow_to_expand_a_unit(self):
        pass

    def a_pre_ap_whg_teacher_is_on_the_homepage(self):
        pass

    def there_are_key_concepts_that_have_tba_big_idea(self):
        pass

    def he_filters_by_big_idea(self):
        pass

    def only_the_units_with_those_big_idea_concepts_assigned_are_displayed_on_the_screen(self):
        pass

    def there_are_key_concepts_that_have_tba_learning_objective(self):
        pass

    def he_filters_by_learning_objective(self):
        pass

    def only_the_units_with_those_learning_objective_concepts_assigned_are_displayed_on_the_screen(self):
        pass

    def there_are_key_concepts_that_have_tba_historical_thinking_skills(self):
        pass

    def he_filters_by_historical_thinking_skills(self):
        pass

    def only_the_units_with_those_historical_thinking_skills_concepts_assigned_are_displayed_on_the_screen(self):
        pass

    def the_user_is_redirected_to_assessments_page(self):
        pass

    def the_specific_performance_task_is_displayed_in_preview_mode(self):
        pass

    def he_clicks_on_performance_task_from_unit_resources_within_the_unit_widget(self):
        pass

    def he_clicks_on_scoring_guide_from_unit_resources_section(self):
        pass

    def he_clicks_download_button(self):
        pass

    def p1_is_successfully_downloaded_to_the_selected_location(self, p1 = "p1"):
        pass

    def he_clicks_print_button(self):
        pass

    def p1_is_successfully_printed(self, p1 = "p1"):
        pass

    def a_pre_ap_biology_teacher_is_on_the_units_page(self):
        pass

    def a_pre_ap_whg_teacher_on_the_units_page(self):
        pass

    def a_pre_ap_whg_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_whg_teacher_on_a_pdf_resource_page(self):
        pass

    def a_pre_ap_biology_teacher_is_on_the_homepage(self):
        pass

    def he_clicks_on_performance_task_scoring_guide_from_unit_resources_section(self):
        pass

    def performance_task_scoring_guide_pdf_loads_in_a_new_browser_tab(self):
        pass

    def he_clicks_on_performance_task_scoring_guide_within_unit_resources_of_unit_widget(self):
        pass

    def he_clicks_on_practice_performance_task_from_unit_resources_within_a_unit(self):
        pass

    def the_specific_practice_performance_task_is_displayed_in_preview_mode(self):
        pass

    def he_clicks_on_practice_performance_task_from_unit_resources_within_the_unit_widget(self):
        pass

    def the_specific_practice_performance_task_is_displayed_in_preview_mode(self):
        pass

    def there_is_a_key_concept_that_has_a_student_handout_launch_activity_as_resource(self, student_handout_launch_activity = "Student Handout: Launch Activity"):
        pass

    def the_student_handout_launch_activity_pdf_file_loads_in_a_new_browser_tab(self, student_handout_launch_activity = "Student Handout: Launch Activity"):
        pass

    def there_is_a_key_concept_that_has_a_student_handout_analytical_reading_writing_as_resource(self):
        pass

    def there_is_a_key_concept_that_has_a_student_handout_modeling_lesson(self):
        pass

    def the_student_handout_analytical_reading_writing_file_loads_in_a_new_browser_tab(self):
        pass

    def there_is_a_key_concept_having_student_handout_data_analysis_lesson_as_resource(self):
        pass

    def the_student_handout_data_analysis_file_loads_in_a_new_browser_tab(self):
        pass

    def the_student_handout_modeling_lesson_loads_in_a_new_browser_tab(self):
        pass

    def a_pre_ap_only_teacher_on_homepage(self):
        pass

    def the_teacher_inspects_class_widget(self):
        pass

    def no_class_was_created_yet(self):
        pass

    def a_class_was_created(self):
        pass

    def trying_to_login_with_p1_and_p2(self, p1 = "", p2 = ""):
        pass

    def a_teacher_with_both_ap_and_pre_ap_subjects_on_the_homepage_of_an_ap_subject(self):
        pass

    def a_teacher_with_both_pre_ap_and_ap_subjects_on_the_homepage_of_an_ap_subject(self):
        pass

    def the_teacher_switches_to_a_pre_ap_subject(self):
        pass

    def a_teacher_with_p1_subjects_on_the_homepage_of_an_ap_subject(self, p1 = "p1"):
        pass

    def a_teacher_with_p1_subjects_on_the_homepage_of_an_pre_ap_subject(self, p1 = "p1"):
        pass

    def he_does_not_see_the_exam_decision_tile(self):
        pass

    def a_student_that_has_only_one_pre_ap_subject_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def the_student_enters_the_correct_credentials_and_clicks_sign_in(self):
        pass

    def he_logs_in_and_lands_on_the_homepage_where_he_can_see_his_subject(self):
        pass

    def a_student_with_only_one_ap_subject_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def the_student_enters_the_correct_credentials_and_clicks_on_the_sign_in_button(self):
        pass

    def he_logs_in_and_lands_on_the_homepage_and_sees_his_subject(self):
        pass

    def a_student_with_multiple_pre_ap_subjects_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def he_enters_the_correct_credentials_and_clicks_on_sign_in_button(self):
        pass

    def logs_in_and_lands_on_the_multisubject_landing_page(self):
        pass

    def sees_all_his_pre_ap_subjects_grouped_under_the_pre_ap_section(self):
        pass

    def a_student_with_multiple_ap_subjects_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def sees_all_his_ap_subjects_grouped_under_the_ap_section(self):
        pass

    def it_is_the_exam_period_for_the_ap_subject(self):
        pass

    def its_not_the_exam_period_for_the_ap_subject(self):
        pass

    def a_teacher_with_both_ap_and_pre_ap_subjects_on_the_homepage_of_a_pre_ap_subject(self):
        pass

    def classes_with_assessments_were_created_for_both_subjects(self):
        pass

    def when_he_switches_to_ap_subject(self):
        pass

    def he_sees_the_exam_decision_title_displayed_in_the_class_widget(self):
        pass

    def in_the_course_resources_popup_he_can_see_the_course_guide_link_associated_to_the_specific_subject(self):
        pass

    def a_teacher_on_the_p1_units_page(self, p1 = "p1"):
        pass

    def he_clicks_on_course_resources_link_from_the_top_banner(self):
        pass

    def a_teacher_in_the_p1_course_resources_popup(self, p1 = "p1"):
        pass

    def a_p1_teacher_is_on_the_units_page(self, p1 = "p1"):
        pass

    def he_clicks_on_performance_task_within_the_unit_widget(self):
        pass

    def there_is_a_key_concept_with_lab_resource(self):
        pass

    def the_lab_resource_loads_in_a_new_browser_tab(self):
        pass

    def he_is_able_to_view_course_resources_section_expand_units_collapse_units_buttons(self):
        pass

    def filters_tba_should_appear_in_the_left_side_of_the_page(self):
        pass

    def he_is_able_to_see_combination_of_resources_teacher_guide_source_sets_different_type_of_student_handouts_crosswalks_labs(self):
        pass

    def there_are_key_concepts_that_have_tba(self):
        pass

    def he_filters_by_tba(self):
        pass

    def only_the_units_with_those_tba_concepts_assigned_are_displayed_on_the_screen(self):
        pass

    def a_pre_ap_algebra_teacher_on_the_units_page(self):
        pass

    def a_pre_ap_algebra_teacher_is_on_the_homepage(self):
        pass

    def he_clicks_on_unit_guide_within_unit_resources_section(self):
        pass

    def a_p1_teacher_is_on_the_homepage(self, p1 = "p1"):
        pass

    def displays_the_following_sections_course_resources_filter_section_unit_resources_the_specific_subunit_types_with_their_resources(self):
        pass

    def a_pre_ap_ela_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_ela_teacher_is_on_the_units_page(self):
        pass

    def a_pre_ap_ela_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_ela_teacher_on_a_pdf_resource_page(self):
        pass

    def a_p1_teacher_is_on_the_homepage(self, p1 = "p1"):
        pass

    def a_pre_ap_ela_teacher_on_the_units_page(self):
        pass

    def a_pre_ap_music_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_music_teacher_is_on_the_units_page(self):
        pass

    def a_pre_ap_music_teacher_on_a_pdf_resource_page(self):
        pass

    def a_pre_ap_music_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_music_teacher_on_the_units_page(self):
        pass

    def a_pre_ap_theatre_teacher_on_a_pdf_resource_page(self):
        pass

    def a_pre_ap_theatre_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_theatre_teacher_is_on_the_units_page(self):
        pass

    def a_pre_ap_theatre_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_theatre_teacher_on_the_units_page(self):
        pass

    def a_pre_ap_dance_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_dance_teacher_is_on_the_units_page(self):
        pass

    def a_pre_ap_dance_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_dance_teacher_on_a_pdf_resource_page(self):
        pass

    def a_pre_ap_dance_teacher_on_the_units_page(self):
        pass

    def a_pre_ap_vpa_teacher_on_a_pdf_resource_page(self):
        pass

    def a_pre_ap_vpa_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_vpa_teacher_is_on_the_units_page(self):
        pass

    def a_pre_ap_vpa_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_vpa_teacher_on_the_units_page(self):
        pass

    def a_pre_ap_algebra_teacher_is_on_the_homepage(self):
        pass

    def a_pre_ap_algebra_teacher_is_on_the_units_page(self):
        pass

    def a_pre_ap_algebra_teacher_on_a_pdf_resource_page(self):
        pass

    def he_clicks_on_a_standards_crosswalk_link(self):
        pass

    def the_link_is_downloaded_in_pdf_format_to_the_default_downloads_location_of_the_machine(self):
        pass

    def a_pre_ap_teacher_in_the_course_resource_popup(self):
        pass

    def the_popup_contains_at_least_one_standards_crosswalk(self):
        pass

    def in_the_course_resources_popup_he_can_see_a_standards_crosswalk_link_associated_to_the_specific_subject(self):
        pass

    def the_link_is_downloaded_and_contains_the_correct_information_for_the_specific_subject(self):
        pass

    def a_teacher_has_already_downloaded_a_course_guide_from_course_resources_popup(self):
        pass

    def he_inspects_the_size_of_the_downloaded_course_guide_pdf(self):
        pass

    def it_matches_the_size_displayed_in_the_course_resource_popup_for_that_specific_course_guide(self):
        pass

    def a_teacher_has_already_downloaded_a_standard_crosswalk_from_course_resources_popup(self):
        pass

    def he_inspects_the_size_of_the_downloaded_standard_crosswalk_pdf(self):
        pass

    def it_matches_the_size_displayed_in_the_course_resource_popup_for_that_specific_standard_crosswalk(self):
        pass

    def he_clicks_on_performance_task_scoring_guide_within_the_unit_widget(self):
        pass

    def performance_task_scoring_guide_pdf_file_loads_in_a_new_browser_tab(self):
        pass

    def a_pre_ap_whg_teacher_is_on_units_page(self):
        pass

    def he_sees_the_following_sections_course_resources_filter_section_unit_resources_key_concepts_assessments_performance_task(self):
        pass

    def he_sees_the_following_sections_course_resources_filter_section_unit_resources_key_concepts_assessments_performance_tasks_labs(self):
        pass

    def a_pre_ap_algebra_teacher_is_on_units_page(self):
        pass

    def he_sees_the_following_sections_course_resources_filter_section_unit_resources_key_concepts_assessments_performance_tasks(self):
        pass

    def a_pre_ap_ela_teacher_is_on_units_page(self):
        pass

    def he_sees_the_following_sections_course_resources_filter_section_unit_resources_weeks_assessments_performance_tasks(self):
        pass

    def a_teacher_on_the_homepage_of_a_preap_subject(self):
        pass

    def clicking_on_a_unit_tab(self, p1 = "p1"):
        pass

    def p1_icon_is_displayed_in_front_of_the_subunit(self, p1 = "p1"):
        pass

    def a_pre_ap_theatre_teacher_is_on_units_page(self):
        pass

    def a_pre_ap_music_teacher_is_on_units_page(self):
        pass

    def a_pre_ap_dance_teacher_is_on_units_page(self):
        pass

    def a_pre_ap_biology_teacher_is_on_units_page(self):
        pass

    def a_pre_ap_vpa_teacher_is_on_units_page(self):
        pass

    def pre_ap_teacher_on_units_page(self):
        pass

    def only_the_appropriate_subunits_have_the_required_tag(self, required = ""):
        pass

    def he_expands_a_unit(self):
        pass

    def both_all_unit_assessments_and_all_qb_assessments_buttons_are_displayed_in_class_widget(self):
        pass

    def only_one_button_is_displayed_in_the_widget_all_assessments(self):
        pass

    def no_button_is_displayed_at_the_bottom_of_the_widget(self):
        pass

    def only_one_button_is_displayed_at_the_bottom_of_the_widget_all_assessments_button(self):
        pass

    def the_teacher_clicks_on_all_assessments_button(self):
        pass

    def inspecting_class_widget_bottom(self):
        pass

    def he_sees_p1_buttons(self, p1 = "p1"):
        pass

    def a_pre_ap_and_ap_teacher_on_the_homepage_of_an_ap_subject(self):
        pass

    def the_teacher_clicks_on_all_unit_assessments_button(self):
        pass

    def teacher_is_redirected_to_unit_assessments_tab__results_subtab(self):
        pass

    def he_is_redirected_to_assessments_tab_results_subtab(self):
        pass

    def the_subunits_that_have_the_required_tag_are_displayed_as_bolded(self, required = ""):
        pass

    def the_accordion_drawers_are_collapsed(self):
        pass

    def he_clicks_on_student_reader_from_unit_resources_section(self):
        pass

    def student_reader_pdf_loads_in_a_new_browser_tab(self):
        pass

    def the_teacher_logs_in(self):
        pass

    def he_lands_on_my_subjects_page_where_the_only_header_reads_my_subjects(self, my_subjects = "AP"):
        pass

    def lands_on_my_subjects_page_where_he_can_see_all_the_pre_ap_subjects_for_which_he_was_granted_access(self):
        pass

    def the_teacher_has_only_pre_ap_subjects_with_classes(self):
        pass

    def a_teacher_with_multiple_pre_ap_courses_on_login_page(self):
        pass

    def a_teacher_with_multiple_ap_courses_on_login_page(self):
        pass

    def a_teacher_on_login_page(self):
        pass

    def the_required_tag_under_appropriate_subunits_is_read_only_and_highligted(self, required = ""):
        pass

    def the_subunits_that_dont_have_the_required_tag_are_not_displayed_as_bolded(self, required = ""):
        pass

    def p2_feature_flag_is_set_to_off(self):
        pass

    def the_teacher_navigates_to_user_profile_menu__my_subjects_option(self):
        pass

    def p2_feature_flag_is_set_to_on(self):
        pass

    def he_lands_on_my_subjects_page_where_he_sees_my_classes_button_near_my_subjects_header(self):
        pass

    def the_p2_feature_flag_is_set_to_off(self):
        pass

    def the_p2_feature_flag_is_set_to_on(self):
        pass

    def lands_on_my_subjects_page_where_my_classes_button_is_displayed(self):
        pass

    def lands_on_my_subjects_page_where_he_sees_my_classes_button_near_the_pre_ap_header(self):
        pass

    def lands_on_my_subjects_page_where_he_sees_my_classes_button_near_the_ap_header(self):
        pass

    def lands_on_my_subjects_page_where_he_sees_two_my_classes_buttons_one_near_the_ap_header_and_one_near_the_preap_header(self):
        pass

    def the_p2_flag_is_set_to_p1(self, p1 = "p1"):
        pass

    def lands_on_my_subjects_page_where_he_can_see_the_ap_subjects_and_the_pre_ap_subjects_without_my_classes_button(self):
        pass

    def a_p1_with_both_pre_ap_and_ap_subjects_on_the_login_page(self, p1 = "p1"):
        pass

    def he_logs_in(self):
        pass

    def he_lands_on_mslp_where_he_can_see_all_the_subjects_available_for_his_school(self):
        pass

    def an_admin_user_with_p1_subjects_on_login_page(self, p1 = "p1"):
        pass

    def the_admin_has_classes_assigned(self):
        pass

    def the_p2_feature_flag_on(self):
        pass

    def the_user_logs_in(self):
        pass

    def he_lands_on_mslp_where_he_can_see_all_his_subjects_without_my_classes_button_being_displayed(self):
        pass

    def the_p2_feature_flag_off(self):
        pass

    def a_coord_user_with_p1_subjects_on_login_page(self, p1 = "p1"):
        pass

    def the_coord_has_classes_assigned(self):
        pass

    def an_coord_user_with_p1_subjects_on_login_page(self, p1 = "p1"):
        pass

    def in_the_modal_popup_displayed_user_can_see_a_close_button_and_a_title_that_reads_course_resources(self):
        pass

    def under_these_a_subtitle_that_reads_pre_ap_p1(self, p1 = "p1"):
        pass

    def in_the_modal_popup_displayed_user_can_see_a_short_text_description_under_each_type_of_resource(self):
        pass

    def the_user_can_see_under_each_description_of_each_resource_the_file_type_for_that_resource(self):
        pass

    def the_user_can_see_near_the_description_of_each_resource_the_file_size_of_that_resource(self):
        pass

    def the_user_sees_all_the_resources_displayed_in_the_order_specified_in_the_importer_on_2_columns_column1123__and_column245(self):
        pass

    def an_icon_is_displayed_to_the_right_side_of_the_size_element_and_indicates_a_teaching_specific_resource__teacher_guide_teacher_modules(self):
        pass

    def a_module_has_been_expanded(self):
        pass

    def a_p1_teacher_on_the_homepage(self, p1 = "p1"):
        pass

    def he_clicks_on_teacher_modules_tab(self):
        pass

    def teacher_modules_is_opened_and_the_page_url_is_p2(self, p2 = "p2"):
        pass

    def a_teacher_on_teacher_modules_page(self):
        pass

    def clicks_teacher_modules_tab(self):
        pass

    def the_teacher_modules_page_is_displayed(self):
        pass

    def a_teacher_on_teacher_modules_page(self):
        pass

    def he_is_a_teacher_of_multiple_p1_subjects(self, p1 = "p1"):
        pass

    def a_coordinator_with_one_ap_subject_on_the_login_page(self):
        pass

    def the_coordinator_logs_in(self):
        pass

    def he_lands_on_mslp_page_where_he_sees_his_pre_ap_subject(self):
        pass

    def he_lands_on_mslp_page_and_he_sees_his_ap_subject(self):
        pass

    def a_coordinator_with_multiple_pre_ap_subjects_on_the_login_page(self):
        pass

    def he_lands_on_mslp_where_he_can_see_the_all_his_pre_ap_subjects(self):
        pass

    def a_coordinator_with_one_pre_ap_subject_on_the_login_page(self):
        pass

    def no_exam_security_pl_section_is_displayed(self):
        pass

    def no_pre_ap_subject(self):
        pass

    def he_lands_on_mslp_where_he_can_see_2_columns_the_left_column_displays_the_exam_security_section(self):
        pass

    def the_right_column_displays_all_his_subjects(self):
        pass

    def a_coordinator_without_active_teacherclasses_on_the_login_page(self):
        pass

    def he_lands_on_an_empty_page_without_any_active_subjects(self):
        pass

    def multiple_p1_subjects_were_provisioned_to_teachers_at_coordinators_associated_school(self, p1 = "p1"):
        pass

    def a_coordinator_on_login_page(self):
        pass

    def access_to_these_subjects_was_provisioned_also_for_the_coordinator(self):
        pass

    def he_lands_on_mslp_where_he_can_only_one_column_that_displays_the_subjects_he_was_provisioned_access_too(self):
        pass

    def the_exam_security_section_is_not_displayed(self):
        pass

    def access_to_a_ap_subject_was_not_yet_provisioned_for_the_coordinator_the_ap_teachers_havent_login_yet(self):
        pass

    def multiple_p1_subjects_were_provisioned_to_teachers_at_the_coordinators_associated_school(self, p1 = "p1"):
        pass

    def a_coordinator_enrolled_in_a_professional_learning_module_on_login_page(self):
        pass

    def a_coordinator_not_enrolled_in_a_professional_learning_module_on_login_page(self):
        pass

    def inspecting_units_widget(self):
        pass

    def a_class_was_created_and_assessments_were_assigned_to_that_class(self):
        pass

    def p2_teacher_on_the_homepage_of_an_ap_subject(self, p2 = "p2"):
        pass

    def a_class_is_already_created_for_that_subject(self):
        pass

    def teacher_inspects_the_page(self):
        pass

    def he_sees_a_create_a_class_button_in_the_right_upper_part_of_the_screen(self, create_a_class = ""):
        pass

    def there_is_no_class_created_for_the_selected_subject(self):
        pass

    def he_clicks_on_create_a_class_p2(self, p2 = "p2"):
        pass

    def teacher_on_units_page(self):
        pass

    def the_assign_button_of_those_assessment_resources_is_in_disabled_state_ie_label_reads_unassigned_in_grey_color_and_assign_icon_is_grey(self):
        pass

    def that_unit_contains_unassigned_assessment_resources(self):
        pass

    def expanding_an_unshared_unit(self):
        pass

    def the_assign_button_of_those_assessment_resources_is_in_unassigned_state_ie_label_reads_unassigned_in_grey_color_and_assign_icon_is_blue(self):
        pass

    def expanding_a_shared_unit(self):
        pass

    def that_unit_contains_assessment_resources_that_were_assigned_to_existing_classes(self):
        pass

    def the_assign_button_of_those_assessment_resources_is_in_assigned_state_ie_label_reads_assigned_in_green_color_and_assign_icon_is_blue(self):
        pass

    def unsharing_a_unit_that_was_previously_shared(self):
        pass

    def the_assign_button_of_those_assessment_resources_moves_to_assigned_while_unit_is_hidden_state_ie_label_reads_assigned_in_green_color_and_assign_icon_is_grey(self):
        pass

    def that_unit_contains_unshared_resources(self):
        pass

    def the_share_button_of_those_resources_is_in_disabled_state_ie_label_reads_unshared_in_grey_color_and_share_icon_is_grey(self):
        pass

    def that_unit_contains_unshared_resources(self):
        pass

    def the_share_button_of_those_resources_is_in_unshared_state_ie_label_reads_unshared_in_grey_color_and_share_icon_is_blue(self):
        pass

    def that_unit_contains_resources_that_were_shared_with_existing_classes(self):
        pass

    def the_share_button_of_those_resources_is_in_shared_state_ie_label_reads_shared_in_green_color_and_share_icon_is_blue(self):
        pass

    def the_share_button_of_those_resources_is_in_shared_while_unit_is_in_hidden_state_ie_label_reads_shared_in_green_color_and_share_icon_is_grey(self):
        pass

    def a_teacher_on_units_page_of_a_subject(self):
        pass

    def he_clicks_on_the_assign_icon_of_a_configured_focus_quiz_its_id_was_added_and_imported_in_gdoc(self):
        pass

    def the_teacher_can_see_the_assessment_preview_page_without_the_assign_popover_open(self):
        pass

    def he_is_redirected_to_the_unit_assessments_page_with_assign_tab_opened(self):
        pass

    def an_assessment_has_already_been_assigned_to_a_class(self):
        pass

    def clicking_on_the_assigned_label_of_that_assessment_from_a_unit_tab(self, assigned = "Assigned"):
        pass

    def nothing_happens(self):
        pass

    def a_student_with_no_enrollments_on_the_login_page(self):
        pass

    def an_error_message_is_displayed_on_the_screen_ap_classroom_error_ap_classroom_does_not_have_you_enrolled_in_any_classes(self, ap_classroom_error_ap_classroom_does_not_have_you_enrolled_in_any_classes = "AP Classroom Error AP Classroom does not have you enrolled in any classes."):
        pass

    def an_error_message_is_displayed_ap_classroom_error_ap_classroom_does_not_have_you_enrolled_in_any_ap_classes_please_try_again_later_or_contact_customer_support_from_the_help_menu(self, ap_classroom_error_ap_classroom_does_not_have_you_enrolled_in_any_classes = "AP Classroom Error AP Classroom does not have you enrolled in any classes."):
        pass

    def a_student_that_has_a_pre_ap_subject_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def he_lands_on_the_homepage_where_he_can_the_top_navigation_bar_having_3_tabs_homepage_resources_and_assessments(self):
        pass

    def a_class_has_already_been_created_for_the_teacher(self):
        pass

    def the_teacher_deletes_the_class_from_ros(self):
        pass

    def the_class_is_no_longer_displayed_in_class_widget_assessments_tab(self):
        pass

    def a_student_enrolled_in_one_class(self):
        pass

    def the_teacher_that_owns_that_class_drops_the_student_from_his_class(self):
        pass

    def the_student_tries_to_login(self):
        pass

    def an_error_message_is_displayed_on_the_screen_ap_classroom_error_ap_classroom_does_not_have_you_enrolled_in_any_ap_classes_please_try_again_later_or_contact_customer_support_from_the_help_menu(self, ap_classroom_error_ap_classroom_does_not_have_you_enrolled_in_any_classes = "AP Classroom Error AP Classroom does not have you enrolled in any classes."):
        pass

    def there_is_one_class_created_for_that_subject(self):
        pass

    def teacher_deletes_that_class_from_ros(self):
        pass

    def a_p1_with_pre_ap_andor_ap_subjects_on_mslp(self, p1 = "p1"):
        pass

    def he_navigates_to_ap_registration_and_ordering__settings__access_management(self):
        pass

    def removes_a_subject_access_for_all_teachers_that_had_access_to_it(self):
        pass

    def the_deleted_subject_is_no_longer_displayed_for_p1_when_navigating_to_mslp(self, p1 = "p1"):
        pass

    def a_teacher_on_the_homepage(self):
        pass

    def he_navigates_to_teacher_modules(self):
        pass

    def navigation_menu_is_displayed_in_upper_right_side_of_the_screen(self):
        pass

    def a_teacher_on_a_p1_subject_homepage(self, p1 = "p1"):
        pass

    def a_configurable_text_button_is_displayed_at_the_bottom_of_the_units_widget_view_all_subunit_label(self):
        pass

    def that_subject_has_available_units(self):
        pass

    def a_configurable_subunit_header_is_displayed_unit_subunit_label_having_the_same_value_as_the_button_at_the_bottom_of_the_screen(self):
        pass

    def a_coordinator_on_a_p1_subject_homepage(self, p1 = "p1"):
        pass

    def an_admin_on_a_p1_subject_homepage(self, p1 = "p1"):
        pass

    def a_student_on_a_p1_subject_homepage(self, p1 = "p1"):
        pass

    def navigating_to_units_page(self):
        pass

    def a_configurable_subunit_header_is_displayed_unit_subunit_label_having_the_same_value_as_in_the_unit_widget(self):
        pass

    def an_admincoord_on_a_p1_subject_homepage(self, p1 = "p1"):
        pass

    def navigating_to_resources_page(self):
        pass

    def that_subject_has_available_resources(self):
        pass

    def all_the_teachers_affected_by_this_change_login_into_the_app(self):
        pass

    def the_preview_mode_is_displayed_and_contains_2_tabs_summary_and_view_questions_in_this_order(self):
        pass

    def he_clicks_on_a_focus_quiz(self):
        pass

    def a_p3_on_the_unit_assessments_assessments_page_assign_tab(self, p3 = "p3"):
        pass

    def he_clicks_on_a_p2_p1(self, p1 = "p1", p2 = "p2"):
        pass

    def a_teacher_on_the_unit_assessments_assessments_page_progress_tab(self):
        pass

    def a_teacher_on_the_unit_assessments_assessments_page_results_tab(self):
        pass

    def he_clicks_on_a_p1_from_the_table(self, p1 = "p1"):
        pass

    def then_clicks_on_the_p1_title_in_the_assessmentspecific_results_page(self, p1 = "p1"):
        pass

    def he_clicks_on_a_p1_from_the_table_that_contains_all_in_progress_assessments(self, p1 = "p1"):
        pass

    def then_clicks_on_the_p1_title_in_the_assessmentspecific_progress_page(self, p1 = "p1"):
        pass

    def summary_tab_is_opened_by_default(self):
        pass

    def an_ap_p2_on_question_bank_page_assign_tab(self, p2 = "p2"):
        pass

    def the_teacher_clicks_on_a_quiz_p1(self, p1 = "p1"):
        pass

    def an_ap_teacher_on_question_bank_page_results_tab(self):
        pass

    def he_clicks_on_a_quiz_from_the_table(self):
        pass

    def then_clicks_on_the_quiz_title_in_the_assessmentspecific_results_page(self):
        pass

    def an_ap_teacher_on_question_bank_page_progress_tab(self):
        pass

    def he_clicks_on_a_quiz_from_the_table_that_contains_all_in_progress_assessments(self):
        pass

    def then_clicks_on_the_quiz_title_in_the_assessmentspecific_progress_page(self):
        pass

    def an_ap_teacher_on_question_bank_page_create_tab(self):
        pass

    def the_teacher_clicks_on_p1(self, p1 = "p1"):
        pass

    def he_has_created_an_empty_quiz_without_questions(self):
        pass

    def the_teacher_tries_to_click_on_p1_button_under_quiz_name(self, p1 = ""):
        pass

    def the_teacher_clicks_on_a_question_p1(self, p1 = "p1"):
        pass

    def the_preview_mode_is_displayed_and_contains_only_the_overview_tab_with_the_content_of_the_question__question_details(self):
        pass

    def he_clicks_on_view_questions_tab(self):
        pass

    def summary_tab_is_in_display(self):
        pass

    def questions_overview_is_displayed_with_all_its_elements_overview_button_question_contentanswerstext_box_previous_next_buttons_question_details_tab(self):
        pass

    def the_general_buttons_close_preview_teacher_guide_and_assign_buttons(self):
        pass

    def view_questions_tab_is_in_display(self):
        pass

    def he_clicks_on_summary_tab(self):
        pass

    def the_assessment_summary_is_displayed_with_all_its_content(self):
        pass

    def that_unit_contains_unassigned_assessment_resources_focus_quiz_unit_testtbd(self):
        pass

    def the_assign_popover_opens_in_units_tab_and_the_teacher_can_assign_the_assessment_to_an_available_class(self):
        pass

    def he_clicks_on_the_title_of_an_assessment_found_on_a_unit_tab(self):
        pass

    def the_preview_button_is_disabled(self):
        pass

    def an_ap_p2_on_question_bank_page_create_tab(self, p2 = "p2"):
        pass

    def a_p2_on_units_page_and_a_unit_is_expanded_having_p1_focus_quizzes(self, p1 = "p1", p2 = "p2"):
        pass

    def a_unit_is_shared_for_students(self):
        pass

    def the_preview_mode_opens_in_unit_assessments_assessments_page_assign_tab(self):
        pass

    def contains_2_tabs_summarydisplayed_by_default_and_view_questions(self):
        pass

    def he_clicks_on_an_assessment(self):
        pass

    def contains_also_the_general_buttons_close_preview_scoring_guide_and_assign_buttons(self):
        pass

    def he_opens_the_preview_of_the_assessment_by_clicking_on_the_p4(self, p4 = "p4"):
        pass

    def the_teacher_is_returned_to_where_heshe_was_when_heshe_clicked_on_the_exam_ie_the_outline_page(self):
        pass

    def a_teacher_on_units_page_and_a_unit_is_expanded(self):
        pass

    def a_teacher_on_units_page_and_a_unit_is_expanded_having_p1_p2(self, p1 = "", p2 = ""):
        pass

    def he_clicks_on_an_assignable_resource_focusquizunit_test_that_has_not_been_configured_its_id_was_not_added_and_imported_in_gdoc(self):
        pass

    def he_clicks_on_the_title_of_a_p1_that_has_been_configured_its_id_was_added_and_imported_in_gdoc(self, p1 = "p1"):
        pass

    def a_wh_teacher_on_units_page(self):
        pass

    def he_clicks_on_filters_button(self):
        pass

    def he_is_able_to_see_among_filters_period_thematic_learning_objectives_practices_and_skills_sub_practice_sub_skill_resource_type(self):
        pass

    def clicks_on_choose_button_of_period_filter(self):
        pass

    def he_filters_the_units_by_the_parent_period_orand_by_the_parent_practice_orand_by_the_parent_thematic_learning_objectives(self):
        pass

    def units_are_filtered_properly_and_only_the_units_that_are_linked_to_the_filters_are_listed(self):
        pass

    def the_teacher_inspects_the_unit_outline_filters(self):
        pass

    def the_filter_icon_is_not_displayed(self):
        pass

    def he_inspects_the_page(self):
        pass

    def the_filters_column_is_no_longer_displayed_only_a_filter_button_that_hides_all_filtersicon(self):
        pass

    def the_teacher_filters_by_a_specific_criteria_eg_period(self):
        pass

    def all_the_units_that_meet_that_criteria_are_displayed_along_with_the_subunits(self):
        pass

    def some_of_the_units_are_linked_to_period_12(self):
        pass

    def he_filters_the_units_by_period_12(self):
        pass

    def units_are_filtered_properly_and_only_the_units_that_are_linked_to_period_12_are_listed(self):
        pass

    def filters_have_already_been_added(self):
        pass

    def the_teacher_clicks_on_clear_all_button_displayed_on_the_outline(self):
        pass

    def filters_are_removed_and_all_the_units_are_displayed(self):
        pass

    def the_teacher_clicks_on_filters_button(self):
        pass

    def the_filter_values_are_displayed_as_a_checkbox_list(self):
        pass

    def all_the_valuescheckboxes_of_that_filter_are_selected(self):
        pass

    def some_filters_have_been_applied(self):
        pass

    def all_the_valuescheckboxes_of_that_filter_are_cleared(self):
        pass

    def the_teacher_clicks_on_filters_button_choose_button__clear_button(self):
        pass

    def the_teacher_clicks_on_filters_button_x_button(self):
        pass

    def then_clicks_on_show_full_text_button(self):
        pass

    def some_of_the_units_are_linked_to_period_123__some_are_linked_to_env_thematic_learning_objectives_and_some_to_practices_12(self):
        pass

    def the_content_of_the_labels_for_that_specific_filter_is_displayed(self):
        pass

    def then_clicks_on_choose_from_one_of_the_filters(self):
        pass

    def the_teacher_clicks_on_filters_button__choose_button_show_full_text_button__show_labels_only_button(self):
        pass

    def the_content_of_the_labels_is_hidden_and_only_the_label_titles_are_displayed_for_that_specific_filter(self):
        pass

    def the_teacher_clicks_on_filters_button_choose_button_select_all_button(self):
        pass

    def all_the_units_that_meet_this_filter_are_displayed(self):
        pass

    def all_the_units_with_all_their_content_are_displayed(self):
        pass

    def the_unit_contains_only_one_assessment_of_this_type(self):
        pass

    def the_unit_contains_multiple_assessments_of_this_type(self):
        pass

    def unit_assessments_assessments_page_assign_tab_is_opened(self):
        pass

    def displays_all_the_assessments_of_that_unit_with_the_specific_filters(self):
        pass

    def he_clicks_on_the_assign_icon_of_a_not_configured_focus_quiz_its_id_was_not_added_and_imported_in_gdoc(self):
        pass

    def no_filter_categories_tags_are_specified_in_the_configuration_google_sheet_for_the_course(self):
        pass

    def a_teacher_with_classes_and_enrolled_students_logs_in_and_goes_to_units_page(self):
        pass

    def that_unit_has_no_hideshow_label_or_icon(self):
        pass

    def the_unit_along_with_the_assignableshareable_resources_is_visible_for_students(self):
        pass

    def there_are_no_classes_yet_for_that_subject(self):
        pass

    def a_unit_is_marked_as_p1_in_the_unit_outline_configuration_doc(self, p1 = ""):
        pass

    def a_teacher_without_classes_for_that_subject_logs_in_and_opens_units_page(self):
        pass

    def status_label_for_that_unit_is_gray_and_the_icon_is_disabledgray(self):
        pass

    def a_teacher_with_classes_for_that_subject_logs_in_and_opens_units_page(self):
        pass

    def near_the_unit_title_there_is_a_label_that_reads_by_default_not_visible_and_an_active_blue_icon(self, not_visible = "Not Visible"):
        pass

    def an_ap_wh_unit_is_marked_as_p1_in_the_unit_outline_configuration_doc(self, p1 = ""):
        pass

    def the_unit_has_not_been_shared_before(self):
        pass

    def an_ap_wh_student_logs_in_and_opens_resources_page(self):
        pass

    def by_default_the_student_does_not_see_that_unit_nor_its_content(self):
        pass

    def there_is_a_unit_marked_as_not_visible(self):
        pass

    def the_teacher_clicks_on_showhide_icon_and_shares_the_unit_with_a_class(self):
        pass

    def the_label_near_unit_title_changes_to_visible_and_the_showhide_icon_remains_blue(self):
        pass

    def a_teacher_with_classes_on_units_page(self):
        pass

    def he_can_see_only_the_shared_units_in_resources_tab(self):
        pass

    def the_teacher_clicks_on_showhide_icon(self):
        pass

    def he_can_share_the_unit_with_both_classes(self):
        pass

    def a_teacher_with_class_a_and_class_b_on_units_page(self):
        pass

    def shares_the_unit_to_both_classes(self):
        pass

    def students_from_both_classes_can_see_that_unit(self):
        pass

    def he_can_share_the_unit_only_to_class_a(self):
        pass

    def students_from_class_a_can_see_the_unit(self):
        pass

    def students_from_class_b_cannot_see_the_unit(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_with_units(self):
        pass

    def he_clicks_on_a_unit_test_from_unit_widget(self):
        pass

    def then_clicks_on_close_preview(self):
        pass

    def the_teacher_is_returned_to_homepage(self):
        pass

    def an_ap_wh_unit_is_marked_as_p1_in_the_unit_outline_configuration(self, p1 = ""):
        pass

    def an_ap_wh_student_logs_in_and_opens_resources_tab(self):
        pass

    def the_unit_is_displayed(self):
        pass

    def there_is_a_unit_marked_as_p1(self, p1 = "p1"):
        pass

    def show_units_by_class_popup_is_displayed(self):
        pass

    def displays_the_focus_quiz_in_preview_mode(self):
        pass

    def the_show_units_popup_is_displayed_and_contains_a_title_show_units_a_info_text_choose_one_or_many_classes_to_see_this_unit_you_can_add_or_remove_classes_at_any_time(self):
        pass

    def he_clicks_on_cancel_button_from_the_share_units_popup(self):
        pass

    def the_teacher_clicks_on_showhide_units_icon_and_selectsunselects_some_classes(self):
        pass

    def all_the_changes_made_are_rolled_back_and_the_initial_state_of_the_unit_is_kept(self):
        pass

    def he_clicks_on_save_button_from_the_share_units_popup(self):
        pass

    def all_the_changes_made_are_saved_and_remembered(self):
        pass

    def a_teacher_with_classes_on_share_units_popup(self):
        pass

    def the_unit_has_been_shared_with_some_classes(self):
        pass

    def the_teacher_clicks_on_x_button_in_front_of_a_class_from_the_right_table(self):
        pass

    def that_class_is_removed_from_the_right_table_and_becomes_unchecked_in_the_left_table(self):
        pass

    def the_teacher_p1_the_checkbox_of_a_class_from_the_left_table(self, p1 = "p1"):
        pass

    def that_class_is_p2_infrom_the_right_table(self, p2 = "p2"):
        pass

    def a_teacher_that_has_a_unit_which_has_been_shared_with_classes_a_and_b(self):
        pass

    def the_share_unit_popover_shows_the_current_share_details(self):
        pass

    def the_teacher_navigates_through_tabs_and_then_returns_to_units_page(self):
        pass

    def he_clicks_on_showhide_units_icon(self):
        pass

    def the_teacher_logs_out_and_then_logs_back_in(self):
        pass

    def he_opens_units_page_and_clicks_on_showhide_units_icon(self):
        pass

    def a_metadata_import_has_been_done_meanwhile(self):
        pass

    def he_refreshes_units_page_and_clicks_on_showhide_units_icon(self):
        pass

    def a_multisubject_teacher_that_has_an_ap_wh_unit_which_has_been_shared_with_classes_a_and_b(self):
        pass

    def the_teacher_navigates_to_another_subject(self):
        pass

    def he_returns_to_ap_wh__units_page_clicks_on_sharehide_unit_icon_for_the_above_unit(self):
        pass

    def the_teacher_navigates_to_ros_using_my_classes_buttontab(self):
        pass

    def he_returns_to_apc__units_page_clicks_on_sharehide_unit_icon_for_the_above_unit(self):
        pass

    def a_teacher_with_classes_on_share_unit_popup(self):
        pass

    def save_button_is_disabled_user_hasnt_done_any_changes_yet(self):
        pass

    def he_selectsremoves_a_class(self):
        pass

    def save_button_becomes_enabled(self):
        pass

    def a_unit_has_been_shared_with_one_or_more_classes(self):
        pass

    def some_the_units_nonassignable_resources_have_been_shared(self):
        pass

    def the_teacher_hides_the_unit_for_all_classes(self):
        pass

    def the_icons_disabledgray(self):
        pass

    def the_shared_nonassignable_resources_of_the_unit_become_hidden_automatically_the_resource_share_label_is_gray_and_reads_hidden(self):
        pass

    def the_unit_has_p1(self, p1 = "p1"):
        pass

    def a_popup_is_displayed_that_reads_you_are_about_to_hide_a_unit_that_has_resources_shared_with_classes_and_assessments_assigned_to_classes_if_you_proceed_the_resources_in_the_unit_will_no_longer_be_visible_to_classes_assessments_will_continue_to_show_for_classes_until_the_assignments_are_marked_completed_or_deleted_do_you_want_to_proceed_(self, you_are_about_to_hide_a_unit_that_has_resources_shared_with_classes_and_assessments_assigned_to_classes_if_you_proceed_the_resources_in_the_unit_will_no_longer_be_visible_to_classes_assessments_will_continue_to_show_for_classes_until_the_assignments_are_marked_completed_or_deleted_do_you_want_to_proceed_ = "You are about to hide a unit that has resources shared with classes and assessments assigned to classes. If you proceed, the resources in the unit will no longer be visible to classes. Assessments will continue to show for classes until the assignments are marked completed or deleted.  Do you want to proceed?"):
        pass

    def non_of_the_units_shareableassignable_resources_have_been_assigned(self):
        pass

    def the_resources_of_the_unit_remain_unsharedunassigned_the_resource_assign_label_is_grey(self):
        pass

    def a_unit_has_been_shared_with_more_classes(self):
        pass

    def some_of_the_units_shareableassignable_resources_have_been_assigned(self):
        pass

    def the_teacher_hides_the_unit_only_for_a_class(self):
        pass

    def the_resources_of_the_unit_keep_their_state(self):
        pass

    def some_the_units_shareable_resources_have_been_shared(self):
        pass

    def then_shares_back_the_unit_with_the_same_classes(self):
        pass

    def all_the_shareable_resources_of_the_unit_are_in_hidden_but_active_state_the_resource_share_label_is_gray_and_reads_unshared__icon_activeblue(self):
        pass

    def the_unit_has_some_assigned_resources_and_some_unassigned_resources(self):
        pass

    def all_the_unassigned_resources_of_the_unit_remain_unassigned_but_active_the_resource_label_is_gray_and_reads_unassigned_icon_activeblue(self):
        pass

    def the_assigned_resources_of_the_unit_remain_assigned_and_active_the_resource_label_is_green_and_reads_assigned_icon_activeblue(self):
        pass

    def the_teacher_opens_share_unit_popup_and_removes_all_classes(self):
        pass

    def the_teacher_opens_share_unit_popup_and_removes_only_one_class(self):
        pass

    def the_hide_unit_warning_message_is_not_displayed(self):
        pass

    def a_unit_is_marked_as_p1_in_the_unit_outline_configuration_units_tab_can_show_hide_false(self, p1 = ""):
        pass

    def an_ap_wh_unit_is_marked_as_showable_in_the_unit_outline_configuration_doc(self):
        pass

    def the_unit_has_been_shared_with_a_class(self):
        pass

    def an_ap_wh_student_belonging_to_that_class_logs_in_and_opens_resources_page(self):
        pass

    def a_resource_is_marked_as_always_show_in_the_unit_outline_configuration_visibility_to_students_always_show(self):
        pass

    def the_unit_that_contains_it_is_visible_for_a_specific_class(self):
        pass

    def a_student_belonging_to_that_class_opens_resource_tab_and_expands_the_unit(self):
        pass

    def that_resource_is_visible_and_can_be_accessed(self):
        pass

    def a_resource_is_marked_as_shareable_in_the_unit_outline_configuration_visibility_to_students_shareable(self):
        pass

    def it_was_shared_with_a_class(self):
        pass

    def the_unit_that_contains_it_is_also_visible(self):
        pass

    def that_assessment_is_visible_and_has_near_its_title_a_label_that_reads_begin(self):
        pass

    def a_locked__without_unlock_datewithout_lock_date_assessment_was_assigned_to_a_class(self):
        pass

    def a_teacher_on_the_preview_display_of_a_unit_testfocus_quiz_from_assign_tab(self):
        pass

    def the_preview_contains_only_close_preview_overview_and_question_details_buttons_so_no_teacher_guide_no_assign_buttons(self):
        pass

    def the_teacher_sees_the_accnum_and_platform_fields_in_the_item_top_of_the_page(self):
        pass

    def the_teacher_sees_the_accnum_and_id_fields_in_the_items_table(self):
        pass

    def a_popup_presenting_the_content_validation_results_will_be_dispalyed(self):
        pass

    def there_is_a_unit_marked_as_visible(self):
        pass

    def the_teacher_clicks_on_showhide_icon_for_a_shareable_resource_under_that_unit(self):
        pass

    def he_can_share_the_resource_only_to_class_a(self):
        pass

    def students_from_class_a_can_see_the_resource(self):
        pass

    def students_from_class_b_cannot_see_the_resource(self):
        pass

    def shares_the_resource_to_both_classes(self):
        pass

    def students_from_both_classes_can_see_that_resource(self):
        pass

    def there_is_a_resource_marked_as_p1(self, p1 = "p1"):
        pass

    def a_teacher_with_classes_on_units_page_with_a_visible_unit(self):
        pass

    def show_resources_by_class_popup_is_displayed(self):
        pass

    def a_teacher_that_has_a_resource_which_has_been_shared_with_classes_a_and_b(self):
        pass

    def he_clicks_on_shared_unshared_resources_icon(self):
        pass

    def the_share_resources_popover_shows_the_current_share_details(self):
        pass

    def a_teacher_with_classes_on_share_resources_popup(self):
        pass

    def the_resource_has_been_shared_with_some_classes(self):
        pass

    def he_refreshes_units_page_and_clicks_on_shared_unshared_resources_icon_for_that_resource(self):
        pass

    def the_teacher_clicks_on_shared_unshared_icon_for_a_resource_that_belongs_to_a_visible_unit(self):
        pass

    def the_show_resources_popup_is_displayed_and_contains_a_title_show_resources_by_class_a_info_text_choose_one_or_many_classes_to_see_this_resource_you_can_add_or_remove_classes_at_any_time(self):
        pass

    def a_resource_has_been_shared_with_some_classes(self):
        pass

    def the_teacher_opens_share_resources_popup_and_removes_all_the_classes(self):
        pass

    def no_warning_message_is_displayed(self):
        pass

    def a_resource_is_marked_as_p1_in_the_unit_outline_configuration_resources_tab_visibility_to_students_always_show(self, p1 = ""):
        pass

    def the_unit_that_contains_it_is_visible(self):
        pass

    def that_resource_has_no_shared_unshared_label_or_icon(self):
        pass

    def the_teacher_click_import_button_in_the_content_validation_results(self):
        pass

    def the_resource_along_with_its_unit_is_visible_for_students(self):
        pass

    def the_unit_that_contains_it_is_not_visible(self):
        pass

    def the_resource_along_with_its_unit_is_not_visible_for_students(self):
        pass

    def a_popup_presenting_the_schema_validation_will_be_dispalyed_import_was_a_success(self, import_was_a_success = "Import was a success"):
        pass

    def an_ap_insight_only_teacher_on_a_ap_insight_page(self):
        pass

    def there_is_a_resource_marked_as_unshared_within_a_visible_unit(self):
        pass

    def the_teacher_clicks_on_shared_unshared_icon_and_shares_the_resource_with_a_class(self):
        pass

    def the_label_near_resource_title_changes_to_shared_and_the_shared_unshared_icon_remains_blue(self):
        pass

    def the_teacher_sees_the_button_to_import_items(self):
        pass

    def the_status_label_for_that_resource_is_gray_and_reads_unshared_and_the_icon_is_disabledgray(self):
        pass

    def a_resource_is_marked_as_shared_in_the_unit_outline_configuration_doc_visibility_to_students_shareable(self):
        pass

    def the_teacher_can_copy_the_results_for_further_use(self):
        pass

    def the_teacher_can_save_the_results_as_pdf(self):
        pass

    def a_resource_is_marked_as_never_show_in_the_unit_outline_configuration_doc_visibility_to_students_never_show(self):
        pass

    def the_resource_is_not_visible_for_students(self):
        pass

    def there_is_no_shared_unshared_label_or_icon_near_resource_title(self):
        pass

    def there_is_a_resource_within_a_visible_unit_marked_as_unshared(self):
        pass

    def he_can_share_the_resource_with_both_classes(self):
        pass

    def the_teacher_selectsunselects_some_classes(self):
        pass

    def he_clicks_on_cancel_button(self):
        pass

    def a_teacher_on_shared_unshared_resources_popup(self):
        pass

    def all_the_changes_made_are_rolled_back_and_the_initial_state_of_the_resource_is_kept(self):
        pass

    def the_teacher_clicks_on_showhide_resources_icon_and_selectsunselects_some_classes(self):
        pass

    def he_clicks_on_save_button_from_the_share_resources_popup(self):
        pass

    def a_resource_is_marked_as_shareable_in_gdoc_imported_visibility_to_students_shareable(self):
        pass

    def the_resource_was_not_shared_before(self):
        pass

    def the_metadata_import_is_done(self):
        pass

    def by_default_the_resource_has_unshared_status_label_reads_unshared(self):
        pass

    def it_is_not_visible_to_students(self):
        pass

    def a_new_revision_exists_of_an_existing__question_type_item_in_the_p2_database(self, _question_type = "=question_type"):
        pass

    def the_new_revision_is_not_in_the_operational_database(self):
        pass

    def the_copy_item_updates_script_is_invoked(self):
        pass

    def the_new_revision_is_copied_over_to_the_operational_database(self):
        pass

    def the_new_revision_has_blank_metadata(self):
        pass

    def a_new__question_type_item_is_created_in_the_p2_database(self, _question_type = "=question_type"):
        pass

    def a_new_item_is_created_with_the_same_id_as_the_item_in_the_p2_database(self):
        pass

    def no_pl_section(self):
        pass

    def also_the_left_column_containing_exam_security(self):
        pass

    def a_coordinator_with_initial_access_to_exam_security_having_at_least_one_ap_subject(self):
        pass

    def the_exam_security_access_is_removed_for_the_coordinator_the_ap_subjects_are_removed(self):
        pass

    def he_lands_on_mslp_page_where_he_still_sees_pl_section_with_the_exam_security_along_with_the_subjects_that_he_has_access_too(self):
        pass

    def the_teacher_accesses_the_import_log_page(self):
        pass

    def the_import_log_page_has_a_table_with_stored_data_for_each_import(self):
        pass

    def the_import_log_table_holds_relevant_info_like_date_user_library_filename_and_success(self):
        pass

    def a_teacher_on_the_import_log_page(self):
        pass

    def the_teacher_is_sorting_the_table_by_date(self):
        pass

    def the_import_log_table_is_sorted_asc_or_desc_by_date(self):
        pass

    def the_teacher_is_sorting_the_table_by_user(self):
        pass

    def the_import_log_table_is_sorted_asc_or_desc_by_user(self):
        pass

    def the_teacher_is_sorting_the_table_by_library(self):
        pass

    def the_import_log_table_is_sorted_asc_or_desc_by_library(self):
        pass

    def the_teacher_is_sorting_the_table_by_filename(self):
        pass

    def the_import_log_table_is_sorted_asc_or_desc_by_filename(self):
        pass

    def the_teacher_is_sorting_the_table_by_successful(self):
        pass

    def the_import_log_table_is_sorted_asc_or_desc_by_successful(self):
        pass

    def the_teacher_presses_on_the_import_button(self):
        pass

    def the_import_log_button_is_available_and_selected(self):
        pass

    def the_import_log_page_is_opened_successfully(self):
        pass

    def the_import_log_page_shows_the_correct_status_of_the_import(self):
        pass

    def a_teacher_on_p1_page__results_tab(self, p1 = "p1"):
        pass

    def he_clicks_on_an_assessment_title_that_has_been_scored_for_all_students__student_performance_subtab_class_overview(self):
        pass

    def he_sees_on_student_performance_subtab_the_average_point_display_rounded_down_avg_points_points_possible_of_the_quiz(self):
        pass

    def he_clicks_on_an_assessment_title__class_performance_subtab(self):
        pass

    def he_sees_a_performance_bar_near_the_class_name(self):
        pass

    def he_inspects_class_average_column_for_scored_assessments(self):
        pass

    def he_sees_the_average_point_display_per_class_rounded_down_avg_points_points_possible_of_the_quiz(self):
        pass

    def he_opens_student_performance_subtab_for_an_assignment_that_contains_fr_qs(self):
        pass

    def he_inspects_student_performance_column(self):
        pass

    def he_sees_a_performance_bar(self):
        pass

    def he_clicks_on_an_assessment_title_student_performance_subtab_class_overview(self):
        pass

    def he_clicks_on_an_assessment_title__class_performance_subtab__click_on_a_question(self):
        pass

    def he_sees_a_performance_bar_near_the_class_title(self):
        pass

    def he_clicks_on_an_assessment_title_that_has_been_scored_for_a_student__student_performance_subtab_click_on_the_scored_student(self):
        pass

    def he_sees_a_performance_bar_near_students_name(self):
        pass

    def he_clicks_on_an_assessment_title_that_has_not_been_scored_for_a_student__student_performance_subtab_click_on_that_specific_student(self):
        pass

    def he_sees_awaiting_scoring_label_near_students_name(self):
        pass

    def he_clicks_on_an_assessment_title_that_has_been_scored_for_a_student__student_performance_subtab_click_on_the_scored_student__click_on_a_question_link(self):
        pass

    def he_sees_a_performance_bar_near_question_title(self):
        pass

    def he_sees_on_student_performance_subtab_the_awaiting_scoring_label(self):
        pass

    def he_opens_a_question_that_has_not_been_scored_yet(self):
        pass

    def he_clicks_on_an_submitted_mrq_assessment_title__student_performance_subtab_click_on_a_student(self):
        pass

    def he_sees_correct_answers_with_a_green_check_next_to_them_and_incorrect_answers_have_a_red_x_next_to_them(self):
        pass

    def he_clicks_on_a_scored_frq_assessment_title__student_performance_subtab_click_on_a_student(self):
        pass

    def he_sees_red_x_for_no_credit_yellow_circle_for_partial_credit_green_check_for_full_credit_awaiting_scoring_for_not_scored_for_subscores_of_an_frq_the_same_but_faded_slightly(self):
        pass

    def a_student_on_assessments_page__results_tab(self):
        pass

    def he_inspects_performance_column(self):
        pass

    def a_student_on_assessments_page_results_tab(self):
        pass

    def he_clicks_on_a_scored_assessment_title__your_performance_subtab(self):
        pass

    def he_clicks_on_and_clicks_on_view_results_link(self):
        pass

    def he_sees_a_awaiting_scoring_label_on_the_right_corner_of_your_performance_subtab(self):
        pass

    def he_clicks_on_an_assessment_title__your_performance_subtab__click_on_a_p1_answer(self, p1 = "p1"):
        pass

    def he_sees_p2_near_the_question_title(self, p2 = "p2"):
        pass

    def there_is_a_key_concept_that_has_an_performance_task_as_resource(self):
        pass

    def the_teacher_sees_a_p1_message(self, p1 = ""):
        pass

    def the_popup_has_yes_no_options(self):
        pass

    def the_teacher_presses_yes_on_the_popup(self):
        pass

    def the_teacher_sees_results_that_the_save_was_successfull(self):
        pass

    def the_teacher_is_returned_to_default_library_view_of_questions(self):
        pass

    def the_teacher_presses_cancel_on_the_popup(self):
        pass

    def the_teacher_sees_results_that_the_cancel_was_successful(self):
        pass

    def it_was_not_shared_with_a_class(self):
        pass

    def the_unit_that_contains_is_shared_for_that_class(self):
        pass

    def that_resource_is_not_visible_and_cannot_be_accessed(self):
        pass

    def a_teacher_clicks_on_the_choose_button_under_the_use_status_filter(self):
        pass

    def a_teacher_selects_one_filter_in_the_pop_up(self):
        pass

    def a_teacher_should_see_the_chosen_filter_under_the_use_status_choose_button(self):
        pass

    def no_performance_icon_is_displayed_for_it(self):
        pass

    def he_logs_in__opens_resources_page__clicks_on_the_assessment_p2(self, p2 = "p2"):
        pass

    def the_assign_popover_is_displayed(self):
        pass

    def the_assign_popover_contains_the_administer_section_set_time_limit(self):
        pass

    def the_toggle_can_be_switched_onoff(self):
        pass

    def there_is_a_student_from_that_class_that_hasnt_started_the_assessment_yet(self):
        pass

    def he_logs_in_and_opens_resources_page(self):
        pass

    def a_teacher_selects_2_filters_in_the_pop_up(self):
        pass

    def a_teacher_should_see_the_text_multiple_selected_under_the_use_status_choose_button(self):
        pass

    def the_student_is_redirected_to_the_quiz_playerassignmentsassignment_id_from_progress_tab_of_the_uaqb_pages_where_he_can_continue_filling_in_his_answers(self):
        pass

    def he_turns_on_the_set_time_limit_toggle(self):
        pass

    def the_minutes_box_will_appear_along_with_an_information_message(self):
        pass

    def the_teacher_can_add_the_desired_time(self):
        pass

    def a_student_on_the_homepage_of_a_subject(self):
        pass

    def that_an_opened_p1_assessment_was_assigned_to_a_class(self, p1 = "p1"):
        pass

    def he_p2(self, p2 = "p2"):
        pass

    def he_turns_on_the_set_time_limit_toggle_and_sets_a_value(self):
        pass

    def he_assigns_the_quiz_o_a_class(self):
        pass

    def the_page_si_redirected_to_the_progress_page_of_that_quiz(self):
        pass

    def the_item_is_not_in_the_operational_database(self):
        pass

    def the_teacher_can_see_the_previously_added_time(self):
        pass

    def a_database_in_environment_with_newly_loaded_data_from_prod_db_dump(self, datatable = "||", environment = ""):
        pass

    def the_script_is_run_to_purge_sso_user_type_users(self, user_type = ""):
        pass

    def the_sections_and_assignments_of_that_user_type_users_are_no_longer_available_in_the_database(self, user_type = ""):
        pass

    def when_you_login_with_the_user_type_you_wont_see_any_assignments(self, user_type = ""):
        pass

    def an_ap_wh_calculus_student_on_the_resource_page_of_ap_wh(self):
        pass

    def the_student_switches_to_ap_calculus(self):
        pass

    def the_calculus_resources_are_displayed_in_resources_page(self):
        pass

    def in_the_unit_widget_of_the_homepage(self):
        pass

    def an_ap_wh_calculus_student_on_the_homepage_of_ap_wh(self):
        pass

    def the_calculus_units_are_displayed_in_units_widget(self):
        pass

    def in_the_resources_page(self):
        pass

    def the_teacher_on_the_progress_page_of_a_timed_assessment(self):
        pass

    def he_filters_the_units_and_there_are_no_related_results(self):
        pass

    def a_message_is_displayed_there_are_no_unit_resources_that_match_your_selection(self):
        pass

    def a_student_on_the_resource_page_of_a_subject(self):
        pass

    def the_student_switches_to_a_subject_without_resourcesall_units_are_not_shared(self):
        pass

    def he_is_taken_to_the_homepage_of_that_subject(self):
        pass

    def a_teacher_on_the_units_page_of_a_subject(self):
        pass

    def the_teacher_switches_to_a_subject_without_units(self):
        pass

    def the_teacher_presses_on_the_timed_assessment_section(self):
        pass

    def he_disables_the_time_toggle(self):
        pass

    def the_time_will_be_removed_from_the_assessment(self):
        pass

    def an_import_has_been_done_for_calculus_google_sheet(self):
        pass

    def a_calculus_teacher_logs_in_and_navigates_to_units_page(self):
        pass

    def the_unit_block_number_focus_block_and_order_block_title_practices_and_skills_teacher_module_resources_khan_lesson_plan_unit_guides_display_the_same_info_as_in_the_google_sheet(self):
        pass

    def an_import_has_been_done_for_ap_wh_google_sheet(self):
        pass

    def an_ap_wh_teacher_logs_in_and_navigates_to_units_page(self):
        pass

    def an_import_has_been_done_for_a_preap_subject_google_sheet(self):
        pass

    def a_teacher_that_has_this_subject_logs_in_and_navigates_to_units_page(self):
        pass

    def the_unit_subunit_number_key_concpets_and_order_key_concepts_title_resources_display_the_same_content_as_in_the_google_sheet(self):
        pass

    def a_student_on_the_assessments_page(self):
        pass

    def the_student_clicks_on_begin_button_of_an_assessment(self):
        pass

    def the_assessment_is_a_timed_one(self):
        pass

    def an_import_has_been_done_for_a_subject_google_sheet(self):
        pass

    def a_confirmation_message_should_appear_informing_the_student_that_it_is_a_timed_assessmnet(self):
        pass

    def units_and_subunits_are_displayed_in_the_sequence_of_the_units_subunits_tabs_of_the_imported_google_sheet(self):
        pass

    def regular_sequential_subunits_have_a_specific_icon_and_are_displayed_with_a_sequence_number_as_described_in_the_imported_gdoc_sheet_subunits_tab(self):
        pass

    def an_import_containing_milestone_subunit_types_has_been_done_for_a_subject_google_sheet(self):
        pass

    def milestone_subunits_have_a_specific_icon_as_described_in_the_imported_gdoc_sheet_subunits_tab(self):
        pass

    def they_do_not_show_a_sequence_number_and_do_not_increment_the_sequence_number_for_the_next_subunit(self):
        pass

    def a_student_on_the_home_page(self):
        pass

    def there_is_a_to_do_card_to_begin_a_timed_assessment(self):
        pass

    def the_student_clicks_on_begin_to_do_card_of_the_timed_assessment(self):
        pass

    def the_student_begins_a_timed_assessment_from_to_do_cards(self):
        pass

    def the_student_selects_begin_in_the_confirmation_popup(self):
        pass

    def the_assessment_is_started_and_the_student_can_answer_the_questions(self):
        pass

    def the_student_begins_a_timed_assessment(self):
        pass

    def the_student_selects_cancel_in_the_confirmation_popup(self):
        pass

    def the_assessment_is_not_started_and_user_is_kept_on_the_assessments_page(self):
        pass

    def that_an_unit_outline_import_has_been_done_for_a_subject_google_sheet(self):
        pass

    def inspects_units_section_from_the_homepage_of_that_subject(self):
        pass

    def the_display_order_of_the_units_and_subunits_level_resources_matches_the_order_found_in_the_resources_tab_of_the_imported_google_sheet(self):
        pass

    def the_assessment_is_not_started_and_the_student_remains_on_the_home_page(self):
        pass

    def a_reminder_banner_is_displayed(self):
        pass

    def he_inspects_the_off_state_of_set_date_and_time_toggle(self):
        pass

    def he_does_not_see_the_calendar_fields_only_set_date_and_time_title_followed_by_the_toggle_button(self):
        pass

    def an_info_text_that_reads_automatically_unlock_and_lock_this_assessment_across_the_date_and_time_range_entered_below(self):
        pass

    def he_switches_it_to_off(self):
        pass

    def the_2_calendar_fields_disappear_and_only_the_title_toggle_and_the_info_text_remain(self):
        pass

    def he_inspects_the_set_date_and_time_toggle(self):
        pass

    def by_default_this_toggle_is_in_disabled_state_off(self):
        pass

    def the_set_date_and_time_toggle_on(self):
        pass

    def the_a_timed_assessment_assigned_and_open(self):
        pass

    def the_student_sees_a_begin_to_do_card_for_that_assessment(self):
        pass

    def the_begin_card_displays_a_timer_icon_and_the_duration_of_the_assessment(self):
        pass

    def the_student_just_completed_a_timed_assessment(self):
        pass

    def he_sets_a_specific_due_date__a_specific_day_in_the_calendar(self):
        pass

    def start_date_calendar_has_all_the_days_after_the_due_date_grayed_out(self):
        pass

    def the_teacher_cannot_select_any_start_date_later_than_the_due_date(self):
        pass

    def he_sets_a_specific_start_date__a_specific_day_in_the_calendar(self):
        pass

    def due_date_calendar_has_all_the_days_previous_to_the_start_date_grayed_out(self):
        pass

    def the_teacher_cannot_select_any_due_date_earlier_than_the_start_date(self):
        pass

    def he_sets_a_specific_start_date_due_date__a_specific_day_in_the_calendar(self):
        pass

    def the_start_date_hour_is_later_than_the_due_date_hour(self):
        pass

    def the_teacher_tries_to_assign_the_assessment_to_a_class(self):
        pass

    def a_specific_error_message_is_displayed_letting_the_user_know_start_date_hour_cannot_be_set_later_than_the_due_date_hour(self):
        pass

    def he_sets_a_specific_start_date_due_date__same_day_and_same_hour(self):
        pass

    def a_specific_error_message_is_displayed_letting_the_user_know_start_date_hour_should_be_sooner_than_the_due_date_hour(self):
        pass

    def he_switches_the_set_date_and_time_toggle_to_on_and_chooses_valid_dates_and_times_for_the_start_and_due_date(self):
        pass

    def assigns_the_assessment_to_a_class(self):
        pass

    def the_assessment_is_assigned_successfully_to_that_class_having_assessment_beginsspecified_start_date_and_assessment_duespecified_due_date(self):
        pass

    def assigns_the_assessment_to_multiple_classes(self):
        pass

    def the_assessment_is_assigned_successfully_to_those_classes_having_assessment_beginsspecified_start_date_and_assessment_duespecified_due_date_for_all_those_classes(self):
        pass

    def he_switches_set_date_and_time_toggle_to_on(self):
        pass

    def the_set_date_and_time_on(self):
        pass

    def the_teacher_tries_to_type_characters_from_the_keyboard_in_the_calendar_fields(self):
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

    def that_an_unit_outline_import_has_been_done_for_an_ap_subject(self):
        pass

    def he_sees_the_following_types_of_resources_unit_resources_unit_guide_teacher_module__question_bank_(self):
        pass

    def teacher_guide_student_handouts_displayed_as_subunit_resources(self):
        pass

    def that_an_unit_outline_import_has_been_done_for_a_pre_ap_subject(self):
        pass

    def he_sees_sample_quiz_questions_displayed_as_unit_resource(self):
        pass

    def that_an_unit_outline_import_has_been_done_for_a_subject(self):
        pass

    def a_teacher_goes_to_the_homepage_of_that_subject__clicks_on_a_unit_tab__clicks_on_the_hyperlinked_p1_name(self, p1 = "p1"):
        pass

    def the_resource_opens_and_displays_its_content(self):
        pass

    def an_openedwithout_lock_date_with_unlock_date_assessment_was_assigned_to_a_class(self):
        pass

    def that_an_openednot_startedwithwithout_lock_date_mcq_assessment_exists_for_a_student_in_resource_tab(self):
        pass

    def the_student_navigates_to_assessment_page__p1_tab(self, p1 = "p1"):
        pass

    def that_resource_has_no_unsharedshared_label_or_icon(self):
        pass

    def the_teacher_clicks_on_shared_unshared_icon_for_that_resource(self):
        pass

    def the_teacher_clicks_on_shared_unshared_icon_for_a_shareable_resource_under_that_unit(self):
        pass

    def a_student_belonging_to_that_class_logs_in_and_opens_resources_tab(self):
        pass

    def the_assessment_title_is_not_clickable_and_nothing_happens(self):
        pass

    def a_student_belonging_to_that_class_tries_to_click_on_the_assessment_title_from_resources_page(self):
        pass

    def the_assessment_has_p1(self, p1 = "p1"):
        pass

    def a_locked_p1__p2__assessment_was_assigned_to_a_class(self, p1 = "p1", p2 = "p2"):
        pass

    def that_a_lockednot_startedwith_unlock_date_assessment_exists_for_a_student_in_resource_tab(self):
        pass

    def the_assessment_has_a_specified_unlock_date_a_specified_lock_date(self):
        pass

    def that_assessment_is_visible_and_has_a_label_that_reads_locked_until_mmddyy_that_matches_the_date_of_the_unlocking_date__lock_icon(self):
        pass

    def a_locked_p1_assessment_was_assigned_to_a_class(self, p1 = "p1"):
        pass

    def that_assessment_is_visible_and_has_near_its_title_a_label_that_reads_begin_until_mmddyy_where_datelock_date(self):
        pass

    def an_opened_with_lock_date_p1_assessment_was_assigned_to_a_class(self, p1 = "p1"):
        pass

    def multiple_students_have_completed_the_assignment(self):
        pass

    def the_teacher_is_on_the_results_page_for_the_assignment(self):
        pass

    def then_the_teacher_will_be_able_to_generate_a_pdf_that_includes_the_report_for_every_student_in_the_assignedto_class(self):
        pass

    def the_teacher_generates_a_pdf_which_includes_the_report_for_every_student(self):
        pass

    def each_students_report_starts_on_a_new_page(self):
        pass

    def no_page_has_the_end_of_one_students_report_and_the_beginning_of_another_students_report(self):
        pass

    def each_students_individual_summary_contains_a_cover_sheet(self):
        pass

    def the_cover_sheet_contains_a_summary_of_question_titles_question_numbers_color_coding_for_correctness(self):
        pass

    def a_page_break_occurs_for_a_question(self):
        pass

    def the_page_break_does_not_separate_a_question_from_any_of_its_answer_choices(self):
        pass

    def the_page_break_does_not_separate_a_question_from_its_feedback(self):
        pass

    def the_footer_contains_p1(self, p1 = ""):
        pass

    def copyright_with_p1(self, p1 = ""):
        pass

    def page_numbers_should_reset_to_1_for_the_first_page_of_each_students_report(self):
        pass

    def the_question_contains_audio(self):
        pass

    def instead_of_where_an_audio_player_would_go_in_the_online_version_a_box_around_the_text_p1_appears(self, p1 = ""):
        pass

    def all_question_titles_will_be_displayed(self):
        pass

    def assessment_title_and_p1_will_display_in_header(self, p1 = ""):
        pass

    def that_a_lockedstartedwithout_unlock_date_assessment_exists_for_a_student_in_resource_tab(self):
        pass

    def no_to_do_card_appears_for_this_assessment(self):
        pass

    def the_student_sees_a_review_to_do_card_for_that_assessment(self):
        pass

    def the_review_card_displays_a_timer_icon_and_the_duration_of_the_assessment(self):
        pass

    def to_do_card_begin_in_the_subject_homepage(self):
        pass

    def has_assigned_an_assessment_that_can_be_scored(self):
        pass

    def an_opened_with_lock_date__p1_assessment_was_assigned_to_a_class(self, p1 = "p1"):
        pass

    def the_student_sees_a_to_score_to_do_card_for_that_assessment(self):
        pass

    def the_score_card_displays_a_timer_icon_and_the_duration_of_the_assessment(self):
        pass

    def there_is_a_student_from_that_class_that_started_the_assessment_but_hasnt_submitted_it_yet(self):
        pass

    def that_assessment_is_visible_and_has_near_its_title_a_label_that_reads_finish_until_mmddyy_where_datelock_date(self):
        pass

    def that_assessment_is_visible_and_has_near_its_title_a_label_that_reads_finish(self):
        pass

    def the_student_is_redirected_to_the_quiz_player_assignmentsassignment_id_from_assign_tab_of_uaqb_pages_where_he_can_start_fill_in_his_answers(self):
        pass

    def that_an_openedin_progresswithwithout_lock_date_mcq_assessment_exists_for_a_student_in_resource_tab(self):
        pass

    def to_do_card_finish_in_the_subject_homepage(self):
        pass

    def that_an_openedin_progresswithwithout_lock_date_frq_assessment_exists_for_a_student_in_resource_tab(self):
        pass

    def that_an_openednot_startedwithwithout_lock_date_frq_assessment_exists_for_a_student_in_resource_tab(self):
        pass

    def a_student_submitted_a_mcq_assessment_that_was_set_by_the_teacher_with_show_result_on(self):
        pass

    def the_assessment_is_in_p1_state_at_the_current_moment(self, p1 = "p1"):
        pass

    def the_student_opens_resources_tab_and_expand_the_unit_containing_that_resource(self):
        pass

    def the_assessment_is_visible_and_has_p2_status(self, p2 = "p1"):
        pass

    def a_performance_icon_is_available(self):
        pass

    def a_student_is_taking_a_timed_assessment(self):
        pass

    def the_student_is_on_the_quiz_player(self):
        pass

    def the_student_is_seeing_an_orange_button_that_contains_a_time_indicator_with_show_caption(self):
        pass

    def he_navigates_to_resources_page__clicks_on_the_performance_icon_for_that_specific_assessment(self):
        pass

    def the_student_is_taken_to_p4(self, p4 = "p4"):
        pass

    def a_student_on_resources_page(self):
        pass

    def the_student_clicks_on_the_assessment_p2(self, p2 = "p2"):
        pass

    def he_presses_on_the_show_button(self):
        pass

    def the_student_is_seeing_the_countdown_timer_with_the_time_left(self):
        pass

    def the_assessment_has_the_status_get_feedbackthe_feedback_has_been_viewed(self):
        pass

    def to_do_card_get_feedback_in_the_subject_homepage(self):
        pass

    def a_student_submitted_a_mcq_assessment_that_is_p2_at_the_current_moment(self, p2 = "p2"):
        pass

    def he_presses_on_the_countdown_timer_button(self):
        pass

    def the_countdown_timer_is_hidden(self):
        pass

    def the_countdown_timer_has_1_minute_left_and_less(self):
        pass

    def the_the_countdown_timer_is_displayed_automatically(self):
        pass

    def the_countdown_timer_cannot_be_hidden(self):
        pass

    def the_buttontime_box_turns_red(self):
        pass

    def the_time_runs_out(self):
        pass

    def there_is_a_submitted__p1__show_results_on_p3_assessment(self, p1 = "", p3 = "p3"):
        pass

    def a_popup_appears_notifying_the_user_that_the_time_ran_out(self):
        pass

    def the_popup_contains_submit_now_and_continue_options(self):
        pass

    def a_student_submitted_an_assessment_with_show_results_toggle_set_to_p1(self, p1 = "p1"):
        pass

    def a_student_submitted_a_mcq_assessment_that_was_set_by_the_teacher_with_show_result_off(self):
        pass

    def the_assessment_is_visible_has_no_status_but_a_performance_icon_is_available(self):
        pass

    def the_start_due_dates_feature_flag_is_set_to_p1(self, p1 = "p1"):
        pass

    def a_teacher_opens_the_assign_assessment_by_class_popup_from_p2(self, p2 = "p2"):
        pass

    def he_p3_set_date_and_time_toggle(self, p3 = "p3"):
        pass

    def a_teacher_on_the_assign_assessment_by_class_popup(self):
        pass

    def he_inspects_set_date_and_time_toggle(self):
        pass

    def sees_it_is_positioned_between_lock_unlock_assessment_and_set_time_limit_toggles(self):
        pass

    def he_switches_the_set_date_and_time_toggle_to_on_and_tries_to_set_start_date_earlier_than_the_current_moment(self):
        pass

    def he_sets_due_date_hour_to_be_p1_than_time_limit_expiration(self, p1 = "p1"):
        pass

    def the_p2_is_reached(self, p2 = "p2"):
        pass

    def an_assessment_was_auto_locked_due_date_was_reached(self):
        pass

    def the_teacher_goes_to_uaqb_page__progress_tab__opens_the_above_assessment__tries_to_manually_unlock_the_quiz(self):
        pass

    def a_popup_error_message_is_displayed_whups_title__you_cant_unlock_an_assessment_after_its_assessment_due_date_to_unlock_configure_the_assessment_due_date_text_ok_button(self):
        pass

    def the_assessment_becomes_locked(self):
        pass

    def a_teacher_on_the_assign_assessment_by_class_popup_of_the_ua_page__results_tab__resources_subtab(self):
        pass

    def a_teacher_on_the_assign_assessment_by_class_popup_of_the_units_page(self):
        pass

    def a_teacher_on_the_assign_assessment_by_class_popup_of_the_qb_page__create_tab(self):
        pass

    def a_teacher_on_the_assign_assessment_by_class_popup_of_qb_page__assign_tab(self):
        pass

    def he_sets_immediately_open_assignments_to_p1(self, p1 = "p1"):
        pass

    def the_assessment_has_the_following_values_in_the_specific_columns_from_progress_table_p4(self, p4 = "p4"):
        pass

    def sets_set_date_and_time_to_p2(self, p2 = ""):
        pass

    def sets_set_time_to_p3(self, p3 = "p3"):
        pass

    def a_teacher_on_the_assign_popup_of_an_assessment(self):
        pass

    def the_assessment_has_the_status_opened_this_can_be_checked_in_progress_tab_of_uaqb_pages_with_assessment_begins_date_and_time_of_the_assigning(self):
        pass

    def he_assigns_a_quiz_with_immediately_open_assignments_toggle_on(self):
        pass

    def a_teacher_on_uaqb_page__results_tab(self):
        pass

    def there_is_an_assessment_where_all_submissions_have_been_scored(self):
        pass

    def he_clicks_on_an_assessment_title__student_performance_subtab_class_overview(self):
        pass

    def there_is_an_assessment_where_all_students_have_submitted_their_answers(self):
        pass

    def not_all_submissions_have_been_scored(self):
        pass

    def not_all_the_students_have_submitted_their_answers(self):
        pass

    def the_assessment_is_in_open_state(self):
        pass

    def the_assessment_is_in_lockedcompleted_state(self):
        pass

    def the_feedback_has_already_been_viewed(self):
        pass

    def the_assessment_is_visible_and_has_no_status(self):
        pass

    def the_student_clicks_on_the_assessment_title(self):
        pass

    def a_teacher_opens_the_subtabs_of_a_quiz_from_p2_page(self, p2 = "p2"):
        pass

    def he_p3_alongside_group_type_and_time_limit(self, p3 = "p3"):
        pass

    def he_opens_a_locked_quiz_that_has_p1(self, p1 = "p1"):
        pass

    def inspects_its_subtabs_class_performance_student_performance_resources(self):
        pass

    def the_teacher_sees_start_date_p2_and_due_date_p3(self, p2 = "p2", p3 = "p3"):
        pass

    def he_accesses_an_opened_quiz_that_has_p1(self, p1 = "p1"):
        pass

    def he_accesses_a_locked_quiz_with_specified_start_and_due_dates(self):
        pass

    def the_teacher_sees_alongside_other_general_data_like_group_type_and_time_limit_the_specified_start_and_due_dates_values(self):
        pass

    def he_accesses_an_opened_quiz_with_specified_start_and_due_dates(self):
        pass

    def a_student_submitted_a_frq_assessment_that_was_set_by_the_teacher_with_show_result_on(self):
        pass

    def a_student_submitted_a_frq_assessment_that_was_set_by_the_teacher_with_show_result_off(self):
        pass

    def a_student_submitted_a_frqmcq_assessment_with_show_results_toggle_set_to_p1(self, p1 = "p1"):
        pass

    def a_student_submitted_a_mcqfrq_assessment_with_show_results_toggle_set_to_p1(self, p1 = "p1"):
        pass

    def the_feedback_has_already_been_viewed_for_a_submitted__p1__show_results_on_mcq_assessment(self, p1 = "p1"):
        pass

    def the_student_is_redirected_to_resultsassignment_idperformance_from_results_tab_of_ua_page_where_he_can_review_his_answers(self):
        pass

    def the_feedback_has_already_been_viewed_for_a_submitted__p1__show_results_on_frq_assessment(self, p1 = "p1"):
        pass

    def a_student_submitted_a_frq_assessment_that_is_p2_at_the_current_moment(self, p2 = "p2"):
        pass

    def a_student_submitted_a_frq_assessment_that_was_set_by_the_teacher_with_score_entryp3(self, p3 = "p3"):
        pass

    def no_performance_icon_is_available(self):
        pass

    def a_student_on_the_your_performance_tab_of_the_results_screen(self):
        pass

    def the_assessment_is_mcq(self):
        pass

    def scoring_has_not_started_for_this_assessment(self):
        pass

    def there_is_a_submitted__p1__score_entry_p3_frq_assessment(self, p1 = "", p3 = "p3"):
        pass

    def scoring_has_not_been_yet_started(self):
        pass

    def the_student_is_redirected_to_p4_page(self, p4 = "p4"):
        pass

    def the_student_answered_correctly(self):
        pass

    def it_has_a_green_color_3_a913_f(self):
        pass

    def a_check_mark_appears_next_to_the_question(self):
        pass

    def click_on_a_specific_question(self):
        pass

    def the_student_answered_wrong(self):
        pass

    def an_x_icon_appears_next_to_the_question(self):
        pass

    def it_has_a_red_color_cf2_b4_e(self):
        pass

    def a_user_assigns_a_quiz_to_a_class_with_start_and_due_date_values(self):
        pass

    def he_inspects_developer_tools__network_tab__assignments_request(self):
        pass

    def start_due_dates_and_times_sent_to_the_server_match_the_values_selected_by_the_user(self):
        pass

    def the_assessment_was_scored_by_the_p3(self, p3 = "p3"):
        pass

    def the_feedback_has_not_been_viewed(self):
        pass

    def the_assessment_has_get_feedback_status(self):
        pass

    def he_navigating_back_to_apc(self):
        pass

    def scoring_is_in_progress(self):
        pass

    def the_assessment_is_in_open_state_and_it_was_scored(self):
        pass

    def the_assessment_was_scored_by_p3(self, p3 = "p3"):
        pass

    def a_teacher_on_the_student_performance_tab_of_the_results_screen(self):
        pass

    def the_teacher_clicks_on_a_students_name_to_view_the_results(self):
        pass

    def a_check_mark_appears_next_to_the_questions_answered_correctly(self):
        pass

    def x_sign_appears_next_to_the_questions_answered_incorrectly(self):
        pass

    def the_teacher_clicks_on_a_specific_question(self):
        pass

    def the_question_is_answered_incorrectly(self):
        pass

    def the_question_is_answered_correctly(self):
        pass

    def a_teacher_on_the_class_performance_tab_of_the_results_screen(self):
        pass

    def the_assessment_is_visible_and_has_locked_status__lock_icon(self):
        pass

    def a_student_submitted_a_frq_assessment_that_was_set_by_the_teacher_with_show_result_on__allow_score_entry__p4(self, p4 = "p4"):
        pass

    def a_student_submitted_a_frq_assessment_that_was_set_by_the_teacher_with_show_result_off__allow_score_entry__p4(self, p4 = ""):
        pass

    def he_p3_start_and_due_date_info_in_the_info_bar_of_the_your_performance_resources_subtabs(self, p3 = "p3"):
        pass

    def there_is_a_student_with_submitted_and_scored_assignments(self):
        pass

    def he_navigates_to_assessments_page__results_tab__opens_an_assessment(self):
        pass

    def a_teacher_on_the_progress_results_tab_of_p1_page(self, p1 = "p1"):
        pass

    def inspects_progress_results_tables(self):
        pass

    def no_date_column_is_displayed(self):
        pass

    def a_teacher_opens_the_progress_results_tabs_from_p2(self, p2 = "p2"):
        pass

    def he_p3_start_date_and_due_columns_in_the_progress_results_tables(self, p3 = "p3"):
        pass

    def there_is_an_assessment_with_time_limit_value(self):
        pass

    def he_sees_p3_column_without_p4_column_in_the_progress_results_tables(self, p3 = "p3", p4 = "p4"):
        pass

    def a_internal_test_teacher_with_email(self, email = "email", datatable = "||"):
        pass

    def you_login_with_p1_and_password(self, p1 = ""):
        pass

    def you_land_on_multi_subject_landing_page_if_you_have_multiple_subjects_or_subject_homepage_when_you_have_one_subject(self):
        pass

    def a_internal_test_student_with_email(self, email = "email", datatable = "||"):
        pass

    def you_land_on_multi_subject_landing_page_if_you_have_multiple_subjects_or_student_homepage_when_you_have_one_subject(self):
        pass

    def subunit_resources_teacher_lesson_plan_student_handout_focus_quiz_unit_test(self):
        pass

    def filters_button_is_inactive(self):
        pass

    def he_no_longer_sees_unit_tests_link_under_unit_resources(self):
        pass

    def he_inspects_unit_widget(self):
        pass

    def they_are_on_the_progress_tab(self):
        pass

    def an_assessment_exists_with_student_progress(self):
        pass

    def the_teacher_clicks_on_the_progress_bar(self):
        pass

    def the_teacher_sees_a_blank_circle_indicating_not_started_with_the_number_of_students_who_have_not_started_the_assessment(self):
        pass

    def one_or_more_students_have_not_started_the_assessment(self):
        pass

    def an_assessment_exists(self):
        pass

    def one_or_more_students_have_started_but_not_completed_the_assessment(self):
        pass

    def the_teacher_sees_in_the_popup_the_halffilled_light_blue_circle_indicating_in_progress_with_the_number_of_students_who_have_started_the_assessment(self):
        pass

    def one_or_more_students_have_completed_the_assessment(self):
        pass

    def the_teacher_sees_a_dark_blue_checkmark_indicating_complete_with_the_number_of_students_who_have_completed_the_assessment(self):
        pass

    def the_teacher_clicks_on_the_assessment(self):
        pass

    def the_teacher_sees_a_blank_circle_indicating_not_started_in_the_overview_table_next_to_the_students_name(self):
        pass

    def the_teacher_sees_a_light_blue_partially_filled_in_circle_indicating_in_progress_on_the_overview_table_next_to_the_students_name(self):
        pass

    def the_teacher_sees_a_dark_blue_checkmark_indicating_complete_in_the_overview_table_next_to_the_students_name(self):
        pass

    def one_or_more_students_have_a_scored_assessment(self):
        pass

    def the_teacher_sees_a_dark_blue_checkmark_indicating_scored_in_the_overview_table_next_to_the_students_name(self):
        pass

    def one_or_more_students_have_a_student_scored_assessment(self):
        pass

    def the_teacher_sees_a_dark_blue_checkmark_indicating_student_scored_in_the_overview_table_next_to_the_students_name(self):
        pass

    def those_assignments_still_have_questions_that_need_to_be_scored(self):
        pass

    def the_teacher_sees_a_dark_blue_check_mark_indicating_submitted_with_the_number_of_students_who_have_submitted_the_assessment(self):
        pass

    def one_or_more_students_have_a_submitted_assessment(self):
        pass

    def the_teacher_has_started_scoring_the_assessments(self):
        pass

    def the_teacher_sees_a_partially_filled_blue_circle_indicating_score_started_in_the_overview_table_next_to_the_students_name(self):
        pass

    def the_assessment_still_needs_to_be_scored(self):
        pass

    def the_teacher_sees_a_dark_blue_empty_circle_indicating_submitted_in_the_overview_table_next_to_the_students_name(self):
        pass

    def the_assignment_questions_have_been_all_scored(self):
        pass

    def the_teacher_sees_in_the_popup_a_dark_blue_check_mark_indicating_scored_with_the_number_of_students_who_have_their_assignment_scored(self):
        pass

    def an_assessment_exists_with_a_progress_bar(self):
        pass

    def one_or_more_students_has_started_but_not_completed_the_assessment(self):
        pass

    def the_teacher_sees_a_blue_partially_filled_circle_indicating_in_progress_with_the_number_of_students_who_have_not_started_the_assessment(self):
        pass

    def the_teacher_sees_a_blue_checkmark_indicating_completed_with_the_number_of_students_who_have_completed_the_assessment(self):
        pass

    def one_or_more_students_have_submitted_the_assessment(self):
        pass

    def the_assessment_has_been_scored(self):
        pass

    def the_assessment_has_not_been_scored(self):
        pass

    def the_teacher_has_started_scoring_the_assessment(self):
        pass

    def the_student_has_scored_the_assessment(self):
        pass

    def the_teacher_has_scored_the_assessment(self):
        pass

    def the_teacher_sees_a_blue_checkmark_indicating_scored_with_the_number_of_assessments_that_have_been_scored_by_the_teacher(self):
        pass

    def the_teacher_sees_a_blank_circle_indicating_not_started_next_to_the_students_name_in_the_overview(self):
        pass

    def the_teacher_sees_a_blue_partially_filled_circle_indicating_in_progress_next_to_the_students_name_in_the_overview(self):
        pass

    def the_teacher_sees_a_blue_checkmark_indicating_completed_next_to_the_students_name_in_the_overview(self):
        pass

    def the_teacher_sees_a_blue_empty_circle_indicating_submitted_next_to_the_students_name_in_the_overview(self):
        pass

    def the_teacher_sees_a_blue_partially_filled_circle_indicating_scoring_started_next_to_the_students_name_in_the_overview(self):
        pass

    def the_teacher_sees_a_blue_checkmark_indicating_student_scored_next_to_the_students_name_in_the_overview(self):
        pass

    def the_teacher_sees_a_blue_checkmark_indicating_scored_next_to_the_students_name_in_the_overview(self):
        pass

    def a_teacher_is_on_the_unit_assessments_page(self):
        pass

    def a_teacher_on_the_p4_page(self, p4 = "p4"):
        pass

    def a_teacher_on_the_progress_results_tab_of_uaqb_page(self):
        pass

    def a_teacher_manually_opens_a_quiz_that_was_locked_with_p1(self, p1 = "p1"):
        pass

    def a_teacher_manually_locks_a_quiz_that_was_opened_with_p1(self, p1 = "p1"):
        pass

    def inspects_its_the_start__due_date_info_at_quiz_level(self):
        pass

    def he_navigates_to_the_p4_page(self, p4 = "p4"):
        pass

    def he_sets_date_and_time_on__start_date_p1_and_due_date_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def a_teacher_on_the_assign_popup_of_a_quiz(self):
        pass

    def the_assessment_p3(self, p3 = "p3"):
        pass

    def leaves_all_the_other_toggles_on_off(self):
        pass

    def assigns_the_assessment_to_a_class_as_opened(self):
        pass

    def a_teacher_assigns_a_locked_assessment_with_start_date_p1_and_due_date_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def the_teacher_goes_to_uaqb_page__progress_tab__opens_the_above_assessment__tries_to_manually_lock_the_quiz(self):
        pass

    def the_quiz_becomes_locked(self):
        pass

    def assessment_due_updates_to_the_date_and_time_of_the_locking_action(self):
        pass

    def the_start_date_and_hour_is_reached(self):
        pass

    def the_quiz_becomes_opened(self):
        pass

    def can_be_started_by_students(self):
        pass

    def a_teacher_assigns_a_locked_quiz_with_specified_start_date_and_p1(self, p1 = "p1"):
        pass

    def the_due_date_and_hour_is_reached(self):
        pass

    def students_can_no_longer_work_on_the_it(self):
        pass

    def a_teacher_assigns_an_immediately_open_quiz_with_specified_due_date(self):
        pass

    def a_teacher_assigns_a_locked_quiz_with_future_start_and_due_dates(self):
        pass

    def the_quiz_has_become_autoopened_at_its_specified_start_date(self):
        pass

    def an_open_assessment_with_start_date_p1_and_due_date_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def assessment_begins_date_and_time_of_the_unlock_action(self):
        pass

    def he_tries_to_manually_unlock_the_quiz(self):
        pass

    def a_teacher_manually_opens_a_quiz_that_was_assigned_as_locked_with_future_start_date_and_not_specified_due_date(self):
        pass

    def he_clicks_on_configure_button_from_the_quiz_progress_view(self):
        pass

    def he_is_able_to_set_a_future_due_date(self):
        pass

    def he_sets_a_future_due_date(self):
        pass

    def that_future_due_date_is_reached(self):
        pass

    def the_quiz_is_autolocked(self):
        pass

    def students_can_no_longer_work_on_it(self):
        pass

    def the_assessment_is_visible_and_has_a_status_of_awaiting_results(self):
        pass

    def the_student_sees_a_performance_icon_and_get_feedback(self):
        pass

    def the_teacher_has_scored_the_frq_assessment(self):
        pass

    def the_assessment_is_visible_and_has_the_progress_icon(self):
        pass

    def the_student_has_submitted_an_assignment_with_mcq_questions(self):
        pass

    def a_message_is_displayed_p1(self, p1 = ""):
        pass

    def he_lands_on_mslp_where_he_can_only_see_one_column_that_displays_the_subjects_he_was_provisioned_access_too(self):
        pass

    def teacher_sees_blue_and_gray_instead_of_green_and_gray_shading_in_progress_bar(self):
        pass

    def teacher_clicks_on_any_unit(self):
        pass

    def teacher_clicks_on_any_progress_icon_next_to_assigned(self):
        pass

    def a_teacher_on_the_qb_page_progress_tab(self):
        pass

    def teacher_clicks_on_any_class(self):
        pass

    def teacher_clicks_on_any_progress_bar(self):
        pass

    def teacher_does_not_see_any_pop_over(self):
        pass

    def assessment_summary_feature_flag_on(self):
        pass

    def assessment_summary_feature_flag_off(self):
        pass

    def the_preview_mode_is_displayed_and_contains_a_single_overview_tab(self):
        pass

    def the_students_can_no_longer_work_on_that_quiz(self):
        pass

    def he_selects_p1_on(self, p1 = "p1"):
        pass

    def p1_toggle_is_switched_automatically_to_off(self, p1 = "p1"):
        pass

    def he_sets_p2__on(self, p2 = "p1"):
        pass

    def a_teacher_manually_opens_a_quiz_that_was_assigned_as_locked_with_future_start_date_and_not_specified_due_date_and_duration(self):
        pass

    def a_student_is_on_the_assessments_page(self):
        pass

    def the_click_on_results(self):
        pass

    def they_open_a_unit_test(self):
        pass

    def they_click_on_unit_topics(self):
        pass

    def the_icons_for_the_units_shown_will_match_those_in_the_unit_outline(self):
        pass

    def the_specific_subunits_covered_by_the_questions_on_the_unit_tests(self):
        pass

    def milestone_subunits_will_never_be_displayed(self):
        pass

    def a_subunit_label_exists_for_a_subunit(self):
        pass

    def the_subunit_label_will_be_display_ie_focus_topic_in_orange(self, focus_topic = "Focus Topic"):
        pass

    def student_handouts_and_focus_quiz_links_will_never_be_displayed(self):
        pass

    def the_headline_of_the_page_will_be_subunit_on_this_unit_test(self, subunit = "subunit"):
        pass

    def click_on_the_unit_p1(self, p1 = ""):
        pass

    def they_click_on_a_subunit(self):
        pass

    def the_link_should_go_to_the_unit_outline_page_with_the_associated_unit_expanded_and_the_page_scrolled_to_that_subunit(self):
        pass

    def they_click_on_unit_tab(self):
        pass

    def they_click_on_results(self):
        pass

    def the_name_of_the_tab_will_be_unit_p1(self, p1 = ""):
        pass

    def a_teacher_is_on_the_unit_page(self):
        pass

    def a_focus_quiz_has_been_completed_by_all_students(self):
        pass

    def that_focus_quiz_has_been_scored(self):
        pass

    def the_teacher_expands_the_subunit_that_focus_quiz_is_in(self):
        pass

    def the_teacher_sees_a_results_bar_showing_shades_of_green_from_light_to_dark(self):
        pass

    def the_teacher_clicks_on_the_results_bar(self):
        pass

    def the_assignments_popover_appears(self):
        pass

    def the_focus_quiz_for_that_class_is_under_view_latest_results(self):
        pass

    def the_results_bar_for_that_focus_quiz_is_in_different_shades_of_green_for_performance_andor_grey_for_not_submitted(self):
        pass

    def the_teacher_clicks_on_the_results_bar_in_the_assignments_popover(self):
        pass

    def the_results_popover_appears_showing_all_students_in_the_class(self):
        pass

    def the_students_are_ordered_alphabetically_by_their_score_on_the_focus_quiz(self):
        pass

    def the_scores_are_colored_different_shades_of_green_from_light_to_dark_or_grey_for_no_results(self):
        pass

    def a_teacher_is_on_the_assignments_popover(self):
        pass

    def the_teacher_has_clicked_on_the_results_bar(self):
        pass

    def the_teacher_clicks_on_a_students_name(self):
        pass

    def the_teacher_is_taken_to_the_results_of_that_assessment_to_that_student_performance(self):
        pass

    def the_subunit_label_is_set_to_p1(self, p1 = ""):
        pass

    def click_on_performance_bar(self):
        pass

    def performance_bars_should_show_corresponding_shade_of_green(self):
        pass

    def teacher_clicks_on_any_result_icon_next_to_assigned(self):
        pass

    def teacher_sees_performance_bars_showing_corresponding_shade_of_green(self):
        pass

    def a_teacher_on_the_unit_assessments_assessments_page_result_tab(self):
        pass

    def a_teacher_on_the_qb_page_result_tab(self):
        pass

    def students_within_each_category_are_sorted_by_score_and_then_by_last_name_as_tiebreaker(self):
        pass

    def student_names_are_hyperlinked(self):
        pass

    def teacher_clicks_on_assign(self):
        pass

    def teacher_clicks_on_preview_of_any_unit(self):
        pass

    def teacher_clicks_on_question_details(self):
        pass

    def teacher_sees_topic_which_is_renamed_from_subunit(self):
        pass

    def teacher_clicks_on_results(self):
        pass

    def teacher_clicks_on_view_of_any_unit(self):
        pass

    def teacher_clicks_on_visible_icon_next_to_unit_1(self):
        pass

    def teacher_sees_share_unit_with_class_with_text_select_who_should_see_this_unit_on_their_ap_classroom_outline_you_can_adjust_which_classes_can_see_this_unit_at_any_time(self, select_who_should_see_this_unit_on_their_ap_classroom_outline_you_can_adjust_which_classes_can_see_this_unit_at_any_time_ = "Select who should see this Unit on their AP Classroom outline. You can adjust which classes can see this unit at any time."):
        pass

    def teacher_clicks_on_unit_1(self):
        pass

    def teacher_clicks_on_icon_next_to_topic_5(self):
        pass

    def teacher_sees_assign_assessment_resource_with_text_select_who_should_see_this_assessment_on_their_ap_classroom_outline_and_assessments_page_assignments_can_be_updated_from_the_progress_tab_of_unit_assessments(self):
        pass

    def a_teacher_on_the_qb_page_assign_tab(self):
        pass

    def teacher_clicks_on_assign_button_of_any_class(self):
        pass

    def teacher_sees_assign_assessment_to_class_text_select_who_should_see_this_assessment_on_their_ap_classroom_assessments_page_assignments_can_be_updated_from_the_progress_tab_of_question_bank(self):
        pass

    def he_clicks_on_unit_outline_tab(self):
        pass

    def he_sees_the_teacher_view_of_units_all_outline_sections_and_resources(self):
        pass

    def sees_that_for_resources_no_status_message_shareunshare_assignunassign_is_displayed(self):
        pass

    def you_are_logged_in_as_coordinator(self):
        pass

    def you_are_on_units_tab(self):
        pass

    def you_expand_the_units(self):
        pass

    def you_click_on_a_share_sub_unit_resource_icon_that_is_active(self):
        pass

    def a_window_is_opening(self):
        pass

    def you_cannot_see_or_select_any_class(self):
        pass

    def the_message_p1_is_displayed_in_the_orange_box(self, p1 = ""):
        pass

    def you_click_on_a_share_sub_unit_assignement_resource_icon_that_is_active(self):
        pass

    def you_choose_a_shared_unit(self):
        pass

    def you_press_on_the_shared_unit_icon(self):
        pass

    def you_click_on_the_performance_bar(self):
        pass

    def you_are_on_units_outline(self):
        pass

    def you_can_see_the_performance_summary_for_assigned_assessments(self):
        pass

    def you_can_click_on_the_view_results_tile(self):
        pass

    def a_popup_opens(self):
        pass

    def you_cannot_click_on_score_tile(self):
        pass

    def you_cannot_click_on_monitor_tile(self):
        pass

    def the_admin_logs_in(self):
        pass

    def you_are_logged_in_as_admin(self):
        pass

    def a_preap_p3_on_the_p4(self, p3 = "p3", p4 = "p4"):
        pass

    def an_ap_p3_on_the_p4(self, p3 = "p3", p4 = "p4"):
        pass

    def assessment_summary_feature_flag_p5(self, p5 = "p5"):
        pass

    def the_preview_mode_of_the_quiz_is_displayed(self):
        pass

    def the_student_registers_for_the_first_time_and_joins_a_p1_class(self, p1 = ""):
        pass

    def the_student_joins_a_p1_class(self, p1 = ""):
        pass

    def he_has_already_joined_a_p3_class(self, p3 = ""):
        pass

    def goes_to_this_subject_in_apc(self):
        pass

    def a_teacher_on_assessments_results_page_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_p2_the_related_resources_section_on_the_right_side_of_the_question(self, p2 = "p2", related_resources = "Related Resources"):
        pass

    def a_teacher_on_assessments_results_page_of_an_ap_subject(self):
        pass

    def then_he_sees_the_resources_corresponding_to_the_test(self):
        pass

    def he_p2_the_unit_resources_tab(self, p2 = "p2"):
        pass

    def a_student_on_assessments_results_page_of_a_p1_subject(self, p1 = "p1"):
        pass

    def a_coordadmin_on_assessments_results_page_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_opens_an_assignment_and_clicks_on_a_question_of_the_assignment(self):
        pass

    def a_teacher_on_assessments__results_tab_of_a_preap_subject(self):
        pass

    def he_opens_a_quiz_that_has_classroom_connections_cards(self):
        pass

    def he_sees_as_title_above_the_cards_banner_classroom_connections(self):
        pass

    def he_sees_on_each_card_a_title_key_concept_or_p2(self, p2 = "p2"):
        pass

    def a_p1_teacher_on_assessments__results_tab(self, p1 = "p1"):
        pass

    def the_expand_all_button_is_inactivedisable(self):
        pass

    def he_can_see_all_the_units_expanded(self):
        pass

    def collapse_all_is_clicked(self):
        pass

    def the_collapse_all_button_is_inactivedisable(self):
        pass

    def all_the_units_are_collapsed(self):
        pass

    def the_button_expand_all_button_is_activeenable(self):
        pass

    def the_button_collapse_all_is_inactivedisable(self):
        pass

    def the_student_is_logged_in_apc(self):
        pass

    def he_clicks_on_units_resources_tab(self):
        pass

    def he_clicks_on_units_resouces_tab(self):
        pass

    def after_teacher_click_confirmation_button_yes(self):
        pass

    def an_assessment_assigned_to_archived_class_exists(self):
        pass

    def after_teacher_clicks_delete_button(self):
        pass

    def a_teacher_is_on_the_qb_progress_tab(self):
        pass

    def they_have_opened_an_assessment(self):
        pass

    def they_click_on_the_enter_scores_tab(self):
        pass

    def they_are_able_to_enter_in_scores_between_0_and_the_maximum_number_of_points_for_that_question(self, maximum = "maximum"):
        pass

    def they_are_able_to_enter_letter_for_the_choices_choices_available(self, letter = "letter", choices = "choices"):
        pass

    def the_assessment_has_a_question_with_maximum_number_of_points_for_a_question(self, maximum = "maximum"):
        pass

    def they_cannot_enter_any_scores_that_start_with_a_negative(self):
        pass

    def they_cannot_enter_any_scores_that_are_greater_than_the_maximum(self, maximum = "maximum"):
        pass

    def if_any_other_letter_is_entered_the_user_sees_a_message_that_says_please_use_letter_or__if_no_response(self, letter = "letter"):
        pass

    def he_goes_to_manage_classes_tab(self):
        pass

    def he_is_able_to_create_an_ap_insight_class_for_that_specific_subject(self):
        pass

    def a_p2_pilot_only_teacher_on_apc(self):
        pass

    def he_is_able_to_create_an_apc_class_for_a_specific_p2_pilot_subject(self):
        pass

    def an_ap_insight__p2_pilot_teacher_on_a_ap_insight_page(self):
        pass

    def he_is_able_to_create_an_ap_insight_class_for_a_specific_ap_insight_subject(self):
        pass

    def an_ap_insight__p2_pilot_admincoord_on_my_groups_page(self):
        pass

    def he_checks_a_school_with_ap_insight_classes(self):
        pass

    def he_is_able_to_see_the_details_of_the_ap_insight_class_for_a_specific_ap_insight_subject(self):
        pass

    def that_class_does_not_display_a_join_code_in_the_class_roster_page(self):
        pass

    def that_class_has_a_valid_join_code_in_ap_insight_classes_page(self):
        pass

    def he_goes_to_apro(self):
        pass

    def that_class_has_a_valid_join_code_in_apro(self):
        pass

    def he_is_taken_to_npl_apclassroomcoordinatortraining(self):
        pass

    def he_sees_a_text_box_containing_the_feedback_entered_by_the_teacher(self):
        pass

    def all_the_text_should_be_visible_in_the_box_with_no_scrolling_option(self):
        pass

    def the_box_will_be_sized_based_on_the_text_size_so_it_can_all_be_visible(self):
        pass

    def he_tries_to_edit_the_feedback_box(self):
        pass

    def he_is_not_able_to_edit_the_feedback_box(self):
        pass

    def a_teacher_with_ap_insight_and_apc_subjects(self):
        pass

    def they_login_to_ap_insight(self):
        pass

    def he_has_access_only_to_the_ap_insight_subjects_he_is_eligible_to_see(self):
        pass

    def a_teacher_with_both_ap_insight_and_p1_subjects(self, p1 = "p1"):
        pass

    def he_logs_into_apc(self):
        pass

    def he_logs_into_pl(self):
        pass

    def he_has_access_only_to_the_pl_subjects_he_is_eligible_to_see(self):
        pass

    def they_only_see_ap_insight_subjects_in_the_subject_selector(self):
        pass

    def a_teacher_with_ap_insight_pl_and_apc_subjects_logged_into_ap_classroom(self):
        pass

    def they_navigate_to_the_ap_insight_site(self):
        pass

    def teacher_clicks_edit_assessment_button(self):
        pass

    def the_assessment_is_deleted(self):
        pass

    def a_p1_teacher_on_p2__p3_assessment_level(self, p1 = "", p2 = "", p3 = "p3"):
        pass

    def he_inspects_students_table(self):
        pass

    def there_are_students_that_have_not_received_a_feedback_yet(self):
        pass

    def he_sees_in_action_column_the_feedback_button_changes_from_light_blue__sign_to_dark_blue_with_a_check_mark_on_it_for_that_specific_student(self, _sign = "+sign"):
        pass

    def the_teacher_opens_a_quiz_from_the_progress_tab(self):
        pass

    def an_admin_on_the_results_page_for_a_specific_quiz(self):
        pass

    def he_should_not_see_a__button_next_to_the_score_button(self):
        pass

    def the_teacher_opens_student_performance_for_a_specific_student(self):
        pass

    def he_should_not_see_the_feedback_field_with_the_text(self):
        pass

    def a_coordinator_user_on_the_results_page_for_a_specific_quiz(self):
        pass

    def he_sees_in_action_column_a_feedback_button_in_light_blue_with_a__sign_on_it_for_the_students_without_feedback(self):
        pass

    def there_are_students_that_received_feedback(self):
        pass

    def there_is_no_given_feedback_for_that_student(self):
        pass

    def a_teacher_on_assessment_page__progress_tab(self):
        pass

    def he_clicks_on_an_assessment_that_contains_p1_questions(self, p1 = "p1"):
        pass

    def a_teacher_on_the_progress_page_for_a_specific_quiz(self):
        pass

    def he_sees_in_action_column_p2(self, p2 = "p2"):
        pass

    def there_is_feedback_already_given_for_that_student(self):
        pass

    def he_changes_the_feedback(self):
        pass

    def the_student_should_see_the_updated_feedback(self):
        pass

    def the_teacher_clicks_on_print_report_button(self):
        pass

    def opens_the_student_report(self):
        pass

    def a_teacher_on_assessment_page__progress_tab__assessment_level(self):
        pass

    def he_clicks_on_p1_feedback_for_a_specific_student(self, p1 = ""):
        pass

    def a_dialog_popup_up_opens_containing_a_title_provide_feedback_on_this_assignment_for_student_name___text_box_cancel__save_buttons(self, provide_feedback_on_this_assignment_for_student_name_ = "Provide feedback on this assignment for <STUDENT_NAME>"):
        pass

    def the_teacher_sees_on_the_first_page_of_the_report_the_assessment_level_feedback_that_he_wrote_for_that_student(self):
        pass

    def the_teacher_types_in_alphanumeric_characters_special_characters_and_spaces(self):
        pass

    def he_is_able_to_save_the_changes_without_errors(self):
        pass

    def the_change_is_displayed_at_student_level(self):
        pass

    def the_teacher_tries_to_type_more_than_1000_characters_including_spaces(self):
        pass

    def he_sees_his_typing_is_limited_to_1000_characters(self):
        pass

    def the_teacher_gives_a_longer_feedback_and_saves_it(self):
        pass

    def he_can_see_the_feedback_displayed_without_any_ui_issues_in_results_tab__quiz_level__student_performance_tab__open_student_view(self):
        pass

    def a_teacher_on_the_progress_page_for_a_specific_assessment(self):
        pass

    def the_teacher_clicks_on_the__feedback_button_for_a_specific_student(self):
        pass

    def types_a_feedback_and_saves_it(self):
        pass

    def the_feedback_is_saved_without_errors(self):
        pass

    def he_clicks_on_the_check_feedback_button_and_clears_all_the_content_of_the_feedback_for_a_specific_student(self):
        pass

    def saves_this_change(self):
        pass

    def he_sees_in_action_column_for_that_student_that_the_feedback_button_changes_from_check_mark_to_sign(self):
        pass

    def all_the_other_feedback_buttons_remember_their_state(self):
        pass

    def he_gives_feedback_to_a_student_and_saves_it(self):
        pass

    def the_teacher_tries_to_save_the_feedback_popup_empty_or_with_spaces(self):
        pass

    def tba(self):
        pass

    def the_teacher_clicks_on_the_check_mark_feedback_button_for_a_specific_student(self):
        pass

    def adds_some_new_content_to_the_existing_feedback__edits_existing_feedback_and_saves_it(self):
        pass

    def the_teacher_opens_the_quiz(self):
        pass

    def he_should_see_the_feedback_box_with_the_actual_feedback(self):
        pass

    def the_teacher_cannot_edit_the_feedback(self):
        pass

    def an_admin_on_the_progress_page_for_a_specific_quiz(self):
        pass

    def an_coordinator_on_the_progress_page_for_a_specific_quiz(self):
        pass

    def a_teacher_on_the_assessment_feedback_popup_opened_from_progress_tab(self):
        pass

    def opens_the_student_reportfirst_page(self):
        pass

    def assessment_level_feedback_is_displayed_bellow_the_student_name(self):
        pass

    def assessment_level_feedback_is_displayed_before_the_questions_starts(self):
        pass

    def he_clicks_on_cancel_button_from_the_feedback_popup(self):
        pass

    def the_assessment_level_feedback_is_written_under_the_label_feedback_from_your_teacher(self, feedback_from_your_teacher = "Feedback from your teacher"):
        pass

    def goes_to_results_page__assessment_level_student_tab_clicks_on_the_above_specificied_student(self):
        pass

    def the_teacher_sees_the_feedback_is_not_changed_and_keeps_its_initial_content(self):
        pass

    def types_a_feedback_and_clicks_on_cancel_button(self):
        pass

    def the_text_entered_into_the_text_box_is_discarded_and_not_saved_for_that_specific_student(self):
        pass

    def the_feedback_button_keeps_its_initial_state__sign(self):
        pass

    def adds_some_new_content_to_the_existing_feedback__edits_existing_feedback_and_clicks_on_cancel_button(self):
        pass

    def the_feedback_popup_is_closed_without_errors(self):
        pass

    def a_teacher_goes_to_qb_results_select_a_quiz_student_performance_select_one_student(self):
        pass

    def a_teacher_goes_to_ua_results_select_a_quiz_student_performance_select_one_student(self):
        pass

    def a_teacher_updates_an_existing_feedback_for_a_specific_student_from_progress_page(self):
        pass

    def student_feedback_feature_flag_is_set_to_p1(self, p1 = "p1"):
        pass

    def a_teacher_opens_p2__progress_tab_and_clicks_on_a_specific_assignment(self, p2 = "p2"):
        pass

    def a_teacher_goes_to_assessments_results_select_a_quiz_student_performance_select_one_student(self):
        pass

    def gives_his_feedback_on_the_that_assignment_and_saves_it(self):
        pass

    def he_goes_to_progress_tab_opens_the_above_assignment_and_inspects_the_student_above(self):
        pass

    def he_sees_in_action_column_the_feedback_button_changed_from_light_blue__sign_to_dark_blue_with_a_check_mark_on_it(self, _sign = "+sign"):
        pass

    def he_is_finishing_the_scoring(self):
        pass

    def he_sees_in_the_button_in_light_blue_with_a__sign_on_it_for_the_students_without_feedback(self):
        pass

    def the_button_is_placed_next_to_the_submit_button(self):
        pass

    def he_sees_the_feedback_button_changes_from_light_blue__sign_to_dark_blue_with_a_check_mark_on_it_for_that_specific_student(self, _sign = "+sign"):
        pass

    def a_teacher_on_the_last_page_of_scoring_form_for_a_frq_assignment_for_a_specific_student(self):
        pass

    def he_already_has_given_feedback_for_that_specific_student(self):
        pass

    def he_removes_the_feedback_and_saves_the_changes(self):
        pass

    def a_teacher_on_assessment_page__progress_tab__score_page(self):
        pass

    def is_scoring_a_frq(self, p1 = "p1"):
        pass

    def is_on_the_last_page_to_submit_the_scores(self):
        pass

    def goes_to_progress_tab_opens_the_above_assignment_and_inspects_the_student_above(self):
        pass

    def he_sees_a_feedback_button_in_light_blue_with_a__sign_on_it_for_the_students_without_feedback(self, p2 = "p2"):
        pass

    def he_clicks_on_p1_feedback_on_the_submit_score_page(self, p1 = ""):
        pass

    def a_teacher_updates_an_existing_feedback_for_a_specific_student_from_scoring_form(self):
        pass

    def a_teacher_on_the_assessment_feedback_popup_opened_from_progress_tab__score_page(self):
        pass

    def a_teacher_on_the_assessment_feedback_popup_opened_from_progress_tab_score_page(self):
        pass

    def a_teacher_on_the_progress_page_for_a_specific_assessment__score_page(self):
        pass

    def there_is_feedback_already_given(self):
        pass

    def he_sees_that_the_feedback_button_changes_from_check_mark_to_sign(self):
        pass

    def the_teacher_clicks_on_the_check_mark_feedback_button(self):
        pass

    def he_p3_the_feedback_button(self, p3 = "p3"):
        pass

    def a_teacher_opens_p2__progress_tab_and_clicks_score_on_a_specific_assignment(self, p2 = "p2"):
        pass

    def he_p3_the_feedback_button_next_to_the_submit_one(self, p3 = "p3"):
        pass

    def there_is_feedback_already_given_for_that_student_from_progress_tab(self):
        pass

    def there_is_feedback_already_given_for_that_student_from_scoring_form(self):
        pass

    def a_p2_teacher_on_the_assign_popup_from_p1_page(self, p1 = "", p2 = "p2"):
        pass

    def he_inspects_the_text_displayed_under_the_student_results_slider(self):
        pass

    def he_sees_the_info_text_students_will_see_scores_and_feedback_as_they_are_available_(self, students_will_see_scores_and_feedback_as_they_are_available_ = "Students will see scores and feedback as they are available."):
        pass

    def a_p2_teacher_on_the_progress_tab_of_the_p1_page(self, p1 = "", p2 = "p2"):
        pass

    def a_p1_on_results_tab_of_p2_page(self, p1 = "", p2 = ""):
        pass

    def he_selects_onemore_classes_under_onemore_schools_from_schools__classes_filter(self):
        pass

    def he_navigates_to_usage_page(self):
        pass

    def he_sees_the_same_filter_applied_automatically_on_this_page(self):
        pass

    def a_coord_on_usage_page(self):
        pass

    def he_navigates_to_results_tab_of_uaqb_page(self):
        pass

    def deselects_the_schools(self):
        pass

    def clicks_on_choose_button_to_reselect_new_filters(self):
        pass

    def the_dropdown_displays_all_available_schools_and_classes(self):
        pass

    def the_teacher_tries_to_save_the_feedback_popup_having_introduced_spaces_from_the_keyboard(self):
        pass

    def feedback_is_saved_successfully_and_feedback_button_changes_to_checkmark(self):
        pass

    def a_p1_on_p2_page_results_tab__students_performance_subtab_of_a_timed_assignment(self, p1 = "", p2 = ""):
        pass

    def clicking_on_the_time_taken_question_mark_icon(self):
        pass

    def a_popup_is_displayed_and_reads_the_number_of_minutes_between_when_the_student_started_and_submitted_the_assignment(self):
        pass

    def inspecting_the_student_performance_table(self):
        pass

    def a_p1_on_p2_page_results_tab__students_performance_subtab_of_a_p3_assignment(self, p1 = "", p2 = "", p3 = "p3"):
        pass

    def he_p4_timed_taken_column_with_a_question_mark_icon(self, p4 = "p2"):
        pass

    def he_clicks_on_scoring_guide(self):
        pass

    def the_pdf_displays_scoring_guide_on_the_upper_right_part_of_the_first_page(self):
        pass

    def a_teacher_is_on_the_units_page(self):
        pass

    def a_teacher_is_on_homepage(self):
        pass

    def he_navigates_to_assessments_page__assignments_tab(self):
        pass

    def the_students_views_the_following_columns_title_start_date_due_duration_status_action(self):
        pass

    def a_student_goes_to_assignments_tab_form_assessment_page(self):
        pass

    def the_overview_player_of_the_quiz_is_displayed(self):
        pass

    def a_teacher_on_the_question_bank_page(self):
        pass

    def a_teacher_with_ap_insight_apc_and_pl_subjects(self):
        pass

    def he_logs_into_ap_insight(self):
        pass

    def he_sees_in_my_classes_filter_only_the_p1_classes_for_the_apc_subject_on_display(self, p1 = "p1"):
        pass

    def he_logs_into_apc_and_navigates_to_p2(self, p2 = "p2"):
        pass

    def he_logs_into_ap_insight_and_navigates_to_assessments_page(self):
        pass

    def he_sees_in_my_classes_filter_from_progress_results_manage_classes_tab_only_the_classes_for_the_ap_insight_subject_on_display(self):
        pass

    def he_sees_in_the_assign_widget_only_the_p1_classes_for_the_apc_subject_on_display(self, p1 = "p1"):
        pass

    def he_logs_into_apc_and_navigates_to_the_homepage_of_a_p1_subject(self, p1 = "p2"):
        pass

    def he_sees_in_the_class_widget_only_the_p1_classes_for_the_apc_subject_on_display(self, p1 = "p1"):
        pass

    def he_logs_into_ap_insight_and_navigates_to_assessments_page__assign_tab(self):
        pass

    def he_sees_in_the_assign_widget_only_the_classes_for_the_ap_insight_subject_on_display(self):
        pass

    def he_sees_only_the_p1_assignments_for_the_apc_subject_on_display(self, p1 = "p1"):
        pass

    def he_logs_into_ap_insight_and_navigates_to_assessments_page__progress_results_tab(self):
        pass

    def he_sees_only_the_assignments_for_the_ap_insight_subject_on_display(self):
        pass

    def he_logs_into_ap_insight_and_navigates_to_assessments_page__manage_classes_tab(self):
        pass

    def he_is_able_to_select_only_ap_insight_subjects_in_the_subject_selector_from_the_add_class_section(self):
        pass

    def a_teacher_with_ap_insight_pl_and_apc_subjects(self):
        pass

    def a_teacher_with_p1_subjects(self, p1 = "p1"):
        pass

    def the_teacher_has_access_only_to_the_apc_subjects_he_is_eligible_to_see_in_msl_psubject_selector(self):
        pass

    def he_logs_into_p2(self, p2 = "p2"):
        pass

    def switches_to_apc(self):
        pass

    def the_teacher_sees_only_to_the_apc_subjects_he_is_eligible_in_msl_psubject_selector(self):
        pass

    def switches_to_pl(self):
        pass

    def he_sees_only_his_pl_subjects(self):
        pass

    def the_xml_field_shows_a_checkmark_for_imported_items(self):
        pass

    def the_reviewed_field_shows_an_x_for_the_imported_items(self):
        pass

    def a_world_history_teacher_on_the_homepage(self):
        pass

    def a_teacher_is_on_the_homepage(self):
        pass

    def there_is_an_assessment_that_has_fr_qs_which_are_awaiting_scoring_by_teacher_display_status_submitted_or_score_startedaction_button_score(self):
        pass

    def the_teacher_checks_the_class_widget(self):
        pass

    def a_student_on_submits_a_quiz_with_frq_questions(self):
        pass

    def a_teacher_on_p1_page__results_tab__student_performance_subtab__student_view(self, p1 = "p1"):
        pass

    def he_sees_the_awaiting_scoring_label_near_print_all_reports_button(self):
        pass

    def sees_the_question_having_the_correct_answer_letter_marked_with_a_green_checkmark(self):
        pass

    def a_teacher_on_the_results_page_class_performance_tab_for_a_specific_quiz(self):
        pass

    def a_student_submitted_a_quiz_and_gave_answer_to_someall_the_questions_of_the_quiz(self):
        pass

    def the_teacher_that_owns_that_assignment_goes_to_uaqb_page__results_tab__class_performance_subtab_of_that_specific_quiz(self):
        pass

    def clicks_on_each_question(self):
        pass

    def he_sees_that_for_each_question_the_number_of_people_who_have_selected_a_specific_response_is_updated(self):
        pass

    def they_can_only_see_the_following_filters_use_status_source_question_type_period_unit_thematic_learning_objectives_practice_and_skills_exam_alignments_publicly_available_stimulus_type_year_of_exam(self):
        pass

    def he_sees_only_the_following_filters_use_status_question_type_big_ideas_science_practices_topic_exam_alignment_publicly_available_form_year_of_exam_stimulus_type_ap_insight_challenge_area(self):
        pass

    def he_sees_only_the_following_filters_use_status_question_type_big_ideas_mpa_cs_exam_ab_or_bc_publicly_available_form_year_of_exam_stimulus_type(self):
        pass

    def he_is_able_to_see_only_the_following_filters_use_status_source_question_type_period__thematic_learning_objectives_practices_and_skills_exam_alignment_publicly_available_stimulus_type_year_of_exam(self):
        pass

    def a_teacher_on_qb_page__create_tab(self):
        pass

    def he_applies_one_or_more_filters_to_the_questions(self):
        pass

    def then_he_removes_itthem(self):
        pass

    def the_list_of_questions_is_unfiltered(self):
        pass

    def he_inspects_the_questions(self):
        pass

    def he_sees_only_the_items_of_the_subject_on_display(self):
        pass

    def a_teacher_is_on_qb__create_tab(self):
        pass

    def the_shared_stimulus_that_is_displayed_has_a_title(self):
        pass

    def removing_the_second_question_under_a_shared_stimulus_group(self):
        pass

    def the_group_is_no_longer_displayed_just_the_title(self):
        pass

    def he_adds_p1(self, p1 = "p1"):
        pass

    def quiz_can_be_created_and_saved_successfully(self):
        pass

    def clicks_on_save(self):
        pass

    def an_ap_p2_opening_from_p1__the_preview_of_an_assessment_with_frq_items_that_has_not_been_assigned_yet(self, p1 = "p1", p2 = "p2"):
        pass

    def the_user_downloads_and_opens_the_scoring_guide_pdf(self):
        pass

    def he_can_see_scoring_guidelines_section(self):
        pass

    def an_ap_teacher_opening_from_progress_tab_of_uaqb_page_the_p1_of_an_assignment_that_contains_frq_items(self, p1 = "p1"):
        pass

    def a_preap_p2_opening_from_p1__the_preview_of_an_assessment_with_frq_items(self, p1 = "p1", p2 = "p2"):
        pass

    def the_user_inspects_the_preview_form(self):
        pass

    def he_does_not_see_scoring_guide_button(self):
        pass

    def an_ap_teacher_in_the_scoring_guide_pdf_of_an_assessment_that_contains_frq_items(self):
        pass

    def he_inspects_the_content_of_the_pdf(self):
        pass

    def he_sees_under_each_frq_item_a_dotted_line_dividing_the_question_content_from_its_scoring_guidelines(self):
        pass

    def he_sees_under_each_frq_dotted_line_the_scoring_section_having_a_bolded_text_title_that_reads_scoring_guidelines(self):
        pass

    def he_sees_the_first_element_of_the_scoring_guideline_section_as_the_section_title_of_the_scoring_form_from_the_question_content_editor(self):
        pass

    def an_ap_p1_in_the_scoring_guide_pdf_of_an_assessment_that_contains_frq_items(self, p1 = "p1"):
        pass

    def the_pdf_was_downloaded_from_p2(self, p2 = ""):
        pass

    def he_inspects_each_frq_item(self):
        pass

    def he_sees_the_scoring_instructions_as_the_second_element_of_the_scoring_guideline_section(self):
        pass

    def it_matches_the_scoring_content_from_content_manager_except_the_score_feedback_fields_associated_with_individual_scoresthat_are_excluded(self):
        pass

    def an_ap_teacher_in_the_scoring_guide_pdf_of_an_assessment_that_contains_mcq__frq_items(self):
        pass

    def he_sees_under_each_frq_item_the_scoring_guidelines_section_that_contains_scoring_instructions_info(self):
        pass

    def he_sees_for_each_mcq_item_the_correct_answer_being_highlighted(self):
        pass

    def a_teacher_is_on_assign_tab_of_a_subject_qb_page(self):
        pass

    def a_teacher_is_on_create_tab_of_a_subject_qb_page(self):
        pass

    def a_teacher_is_on_qb_page__create_tab_of_an_ap_subject(self):
        pass

    def he_adds_a_title_to_the_quiz(self):
        pass

    def clicks_save(self):
        pass

    def he_has_added_at_least_one_question_to_p1_form(self, p1 = ""):
        pass

    def the_new_quiz_is_created_and_saved(self):
        pass

    def he_adds_a_title_to_my_quiz_form_and_at_least_one_question(self, my_quiz = "My Quiz"):
        pass

    def the_new_quiz_is_created_and_saved_having_the_given_title(self):
        pass

    def a_teacher_on_ua_page__results_tab(self):
        pass

    def he_opens_an_assignment_and_clicks_on_a_mrq_question(self):
        pass

    def he_sees_the_question_content_and_the_available_answer_options(self):
        pass

    def he_sees_the_correct_answer_displayed_as_framed(self):
        pass

    def he_sees_the_question_title_displayed_at_question_level(self):
        pass

    def a_pre_ap_whg_teacher_logged_in(self):
        pass

    def a_teacher_is_on_the_homepage(self):
        pass

    def has_the_following_text_reminder_please_complete_the_online_scoring_modules_for_your_units_1_and_2_performance_tasks_modules_are_available_for_geography_era_1_and_era_4_learn_how_to_accurately_score_and_give_your_students_feedback_in_these_ondemand_and_selfpaced_modules_while_also_earning_ceu_continuing_education_units(self):
        pass

    def a_pre_ap_algebra_teacher_logged_in(self):
        pass

    def has_the_following_text_reminder_please_complete_the_online_scoring_modules_for_the_units_1_and_2_performance_tasks_learn_how_to_accurately_score_and_give_your_students_feedback_in_these_ondemand_and_selfpaced_modules_while_also_earning_ceu_continuing_education_units(self):
        pass

    def a_pre_ap_biology_teacher_logged_in(self):
        pass

    def a_pre_ap_english_teacher_logged_in(self):
        pass

    def he_sees_the_awaiting_scoring_label_in_the_class_average_column_for_that_specific_assignment(self):
        pass

    def he_opens_student_performance_subtab_for_a_mcq_only_assignment(self):
        pass

    def the_assignment_was_submitted_by_at_least_one_student(self):
        pass

    def he_sees_the_class_average_calculation_near_print_all_reports_button(self):
        pass

    def he_inspects_class_average_column_for_a_mcq_only_assignment(self):
        pass

    def he_sees_class_average_calculation_in_the_class_average_column_for_that_specific_assignment(self):
        pass

    def he_inspects_class_average_column_for_an_assignment_that_contains_fr_qs(self):
        pass

    def a_teacher_on_uaqb_page__results_table(self):
        pass

    def an_ap_teacher_on_p1__progress_tab__frq_assignment_on_display(self, p1 = "p1"):
        pass

    def the_user_enables_paper_testing_and_downloads_test_books_pdf(self):
        pass

    def he_does_not_see_scoring_guidelines_section_in_the_test_books_pdf(self):
        pass

    def a_p1_user_p5_subjects_on_the_login_page(self, p1 = "", p5 = "p5"):
        pass

    def he_logs_in_and_clicks_on_the_help_menu(self):
        pass

    def the_assignment_has_at_least_one_scored_submission__at_least_one_p1_submission(self, p1 = ""):
        pass

    def all_the_submissions_of_the_assignment_have_been_scored(self):
        pass

    def he_sees_the_correct_calculation_of_the_class_average_near_print_all_reports_button(self):
        pass

    def he_sees_the_correct_calculation_of_the_class_average_in_the_class_average_column_for_that_specific_assignment(self):
        pass

    def he_sees_the_following_available_sections_by_default_p2(self, p2 = "p2"):
        pass

    def he_clicks_on_faq_link_under_frequently_asked_questions_section(self):
        pass

    def he_sees_the_specific_faq_pdf_opening_in_a_new_tab_faqs_ap_classroom_fa_qspdf(self):
        pass

    def an_ap_p1_user_p3_subjects_in_the_help_menu(self, p1 = "", p3 = "p3"):
        pass

    def a_p1_coordinator_on_mslp_page(self, p1 = ""):
        pass

    def he_opens_help_menu(self):
        pass

    def he_p2_the_tutorials_link(self, p2 = "p2"):
        pass

    def an_ap_coord_on_the_help_menu(self):
        pass

    def he_clicks_on_tutorials_link(self):
        pass

    def the_teacher_is_logged_into_the_application(self):
        pass

    def teacher_navigates_to_assign_tab(self):
        pass

    def teacher_is_able_to_see_the_assign_button_for_a_question_bank(self):
        pass

    def a_student_enrolled_in_p1_subjects_on_the_homepage_of_a_subject(self, p1 = ""):
        pass

    def he_clicks_on_user_settings_menu_from_the_upper_right_side_of_the_screen(self):
        pass

    def he_p2_ap_stories_link_under_user_settings_menu(self, p2 = ""):
        pass

    def he_clicks_on_the_student_icon_for_a_given_answer(self):
        pass

    def he_sees_a_list_with_the_students_which_have_selected_that_answer(self):
        pass

    def the_teacher_opens_the_assignment_for_that_specific_student(self):
        pass

    def clicks_on_a_mcq_question(self):
        pass

    def he_clicks_on_the_student_icon_for_the_given_answer_of_the_student(self):
        pass

    def he_sees_in_the_list_the_student_which_selected_that_answer(self):
        pass

    def the_list_contains_on_each_line_the_student_overall_score_student_first_name_student_last_name(self):
        pass

    def a_p1_teacher_on_the_homepage_of_a_subject(self, p1 = ""):
        pass

    def a_teacher_on_p1_page__results_tab_question_level_view_mcq_question(self, p1 = "p1"):
        pass

    def he_sees_the_overall_score_for_each_student_as_the_report_from_total_gained_points_by_the_student_from_the_entire_assignmenttotal_possible_points_that_the_student_could_gain_from_the_answered_questions_of_the_assignment(self):
        pass

    def a_user_teacher_on_the_login_page(self, p1 = ""):
        pass

    def the_teacher_is_able_to_see_the_assign_button_for_an_already_created_question_bank(self):
        pass

    def teacher_clicks_on_the_assign_button(self):
        pass

    def teacher_is_able_to_see_the_assign_modal(self):
        pass

    def the_teacher_is_on_assign_tab_from_question_bank_page(self):
        pass

    def teacher_clicks_assign_button_for_an_already_created_question_bank(self):
        pass

    def in_assign_modal_switches_the_toggle_on_for_take_the_assessment_offline_option(self):
        pass

    def in_assign_modal_switches_the_toggle_off_for_take_the_assessment_offline_option(self):
        pass

    def teacher_is_able_to_click_the_assign_button_on_the_assign_modal(self):
        pass

    def the_flag_new_assignment_modal__on(self):
        pass

    def has_created_a_question_bank(self):
        pass

    def he_clicks_on_save_quiz(self):
        pass

    def the_assign_button_will_be_displayed(self):
        pass

    def flag_new_assignment_modal__on(self):
        pass

    def the_teacher_clicks_on_assign_button(self):
        pass

    def the_new_assign_modal_is_displayed(self):
        pass

    def teacher_selects_the_class_from_choose_classes_list(self):
        pass

    def he_switches_on_take_the_assessment_offline_toggle_button(self):
        pass

    def teacher_can_assign_the_question_bank_to_the_class(self):
        pass

    def he_clicks_on_the_assign_button(self):
        pass

    def he_is_presented_with_the_old_assign_modal(self):
        pass

    def the_take_the_assessment_offline_toggle_switch_is_not_displayed(self):
        pass

    def a_user_on_the_login_page_without_login_in(self):
        pass

    def he_clicks_to_expand_help_menu(self):
        pass

    def he_sees_only_the_contact_us_form(self):
        pass

    def the_student_expands_help_menu(self):
        pass

    def he_sees_p2_sections(self, p2 = "p2"):
        pass

    def a_student_enrolled_in_p1(self, p1 = ""):
        pass

    def he_has_already_logged_into_the_apc(self):
        pass

    def a_student_on_the_help_menu(self):
        pass

    def a_teacher_on_the_help_menu(self):
        pass

    def he_clicks_on_p1_link(self, p1 = "", free_text = "", datatable = "||"):
        pass

    def he_sees_the_specific_p2_pdf_opening_in_a_new_tab(self, p2 = "p2"):
        pass

    def the_user_clicks_on_p1_link(self, p1 = ""):
        pass

    def he_leaves_a_p1_question_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def he_should_see_the_unlock_the_assignment_now_toggle_switch_greyed_out(self):
        pass

    def the_teacher_is_presented_with_the_new_assign_modal_and_he_switches_on_take_the_assessment_offline_toggle_switch_and_clicks_on_more_options(self):
        pass

    def he_sees_the_p1_option_greyed_out(self, p1 = ""):
        pass

    def the_flag_p1_and_the_teacher_is_presented_with_the_new_assign_modal_and_he_switches_on_p2_toggle_switch(self, p1 = "", p2 = ""):
        pass

    def the_flag_p1_and_the_teacher_is_presented_with_the_assign_modal(self, p1 = ""):
        pass

    def the_teacher_is_not_able_to_view_the_p1_toggle_switch(self, p1 = ""):
        pass

    def the_flag_new_assignment_modal__on_and_teacher_is_presented_with_the_assign_modal(self):
        pass

    def the_teacher_select_the_list_of_classes_from_choose_class_list_and_switches_on_the_take_the_assessment_offline_toggle_switch(self):
        pass

    def the_flag_new_assignment_modal__on_and_the_teacher_is_presented_with_the_new_assign_modal(self):
        pass

    def the_teacher_selects_the_class_from_the_choose_class_list_and_switches_on_the_p1_toggle_switch(self, p1 = ""):
        pass

    def the_teacher_selects_the_class_from_the_choose_class_list_and_switches_off_the_p1_toggle_switch(self, p1 = ""):
        pass

    def the_teacher_is_able_to_click_the_assign_button_to_assign_the_assessment_to_the_class(self):
        pass

    def he_should_see_the_unlock_the_assignment_now_toggle_switch_enabled(self):
        pass

    def the_teacher_is_presented_with_the_new_assign_modal_and_he_switches_off_take_the_assessment_offline_toggle_switch_and_clicks_more_options(self):
        pass

    def he_sees_the_date_and_time_option_is_enabled(self):
        pass

    def has_created_and_saved_a_question_bank_and_flag_new_assignment_modal__on(self):
        pass

    def has_created_and_saved_a_question_bank(self):
        pass

    def flag_new_assignment_modal__on_and_clicks_assign_button_to_assign_the_question_bank_and_is_presented_with_the_new_assign_modal(self):
        pass

    def has_created_and_saved_question_bank_and_clicked_the_assign_button_to_assign_the_question_bank(self):
        pass

    def is_presented_with_the_new_assign_modal_and_teacher_selects_the_list_of_classes_from_choose_classes_list(self):
        pass

    def has_created_and_saved_the_question_bank_and_flag_new_assignment_modal__off(self):
        pass

    def in_the_progress_tab_paper_testing_toggle_switch_is_off_for_that_assessment(self):
        pass

    def in_the_progress_tab_paper_testing_toggle_switch_is_on_for_that_assessment(self):
        pass

    def teacher_can_assign_the_question_bank_to_all_the_classes(self):
        pass

    def the_teacher_has_already_assigned_a_question_bank_to_the_class_to_be_taken_offline(self):
        pass

    def the_teacher_clicks_on_the_question_bank_progress_tab(self):
        pass

    def he_should_see_paper_testing_toggle_switch_set_to_on_and_the_test_books_button_should_be_enabled(self):
        pass

    def is_on_the_question_bank_progress_tab_and_can_see_that_the_paper_testing_toggle_switch_is_on_for_that_assessment(self):
        pass

    def he_clicks_on_the_test_books_button_under_the_paper_testing_toggle_switch(self):
        pass

    def he_can_download_the_assessment_to_be_taken_offline(self):
        pass

    def the_teacher_has_already_assigned_a_question_bank_to_the_class_not_to_be_taken_offline(self):
        pass

    def he_should_see_paper_testing_toggle_switch_set_to_off_and_should_not_see_the_test_books_button_under_this(self):
        pass

    def teacher_navigates_to_unit_assessment_page(self):
        pass

    def the_teacher_is_able_to_see_the_assign_button_for_unit_test(self):
        pass

    def the_teacher_is_on_the_unit_assessment_page(self):
        pass

    def is_able_to_see_the_assign_button_for_a_unit_test_and_the_flag_new_assignment_modal__on(self):
        pass

    def the_teacher_is_on_assign_tab_from_unit_assessment_page(self):
        pass

    def teacher_clicks_assign_button_for_a_unit_test(self):
        pass

    def the_teacher_clicks_the_assign_button(self):
        pass

    def the_assessment_is_assigned_to_that_class(self):
        pass

    def the_assessment_is_assigned_to_the_classes(self):
        pass

    def teacher_clicks_the_assign_button_for_a_unit_test(self):
        pass

    def the_teacher_is_on_assign_tab_from_the_unit_assessment_page(self):
        pass

    def teacher_clicks_assign_button_for_a_unit_assessment(self):
        pass

    def he_selects_a_class_in_the_new_assign_modal_and_switches_off_the_p1_toggle_switch(self, p1 = ""):
        pass

    def he_selects_a_class_in_the_new_assign_modal_and_switches_on_the_p1_toggle_switch(self, p1 = ""):
        pass

    def the_teacher_is_on_assign_tab_of_a_unit_assessment_page(self):
        pass

    def the_teacher_is_on_assign_tab_of_a_subject_unit_assessment_page(self):
        pass

    def a_teacher_is_on_the_assign_popover_of_a_quiz_opened_by_clicking_on_p1_button_from_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def teacher_sets_take_the_assessment_offline_toggle__on(self):
        pass

    def clicks_on_more_options(self):
        pass

    def he_sees_p1_and_p2_grayed_out(self, p1 = "", p2 = ""):
        pass

    def in_the_progress_tab_paper_testing_toggle_switch_is_on_for_all_classes_for_that_quiz(self):
        pass

    def a_student_on_the_final_exam_player_of_a_pre_ap_subject(self):
        pass

    def he_sees_in_the_question_navigation_bar_that_question_displayed_in_an_unfilled_black_outline_circle(self):
        pass

    def he_give_answers_to_a_p1_question(self, p1 = ""):
        pass

    def he_sees_that_the_appropriate_circle_for_that_question_in_the_question_navigation_turns_into_a_blue_filled_circle(self):
        pass

    def the_student_answers_a_question(self):
        pass

    def he_sees_a_black_line_following_these_questions_in_the_question_navigation_bar(self):
        pass

    def the_student_leaves_some_questions_unanswered(self):
        pass

    def he_sees_the_black_line_that_follows_the_question_circle_turning_blue_when_the_question_circle_turns_blue_as_well(self):
        pass

    def he_answered_some_questions_but_not_all_of_them(self):
        pass

    def the_student_exits_the_player(self):
        pass

    def then_opens_it_again(self):
        pass

    def he_sees_the_circles_and_the_lines_in_the_question_navigation_bar_keeping_their_state(self):
        pass

    def the_student_clicks_on_a_question_number_from_the_question_navigation_bar(self):
        pass

    def the_question_is_displayed_having_the_title_question_clicked_number(self):
        pass

    def the_student_clicks_on_an_p1_question_from_the_question_navigation_bar(self, p1 = "p1"):
        pass

    def the_question_displays_an_outline_around_itself_having_the_form_of_a_p2_circle(self, p2 = "p2"):
        pass

    def the_question_is_displayed_having_to_the_right_of_the_navigation_an_element_that_reads_question__the_question_the_user_is_currently_viewing_of__total_number_of_questions_in_the_quiz(self):
        pass

    def the_question_title_the_number_being_focused_in_the_navigation_bar_and_the_count_element__x_out_of_y_display_the_same_number(self):
        pass

    def the_student_cycles_p1_to_a_question_using_the_p2_navigation_arrows(self, p1 = "p1", p2 = "p2"):
        pass

    def the_student_clicks_on_the_p1_arrow_from_the_question_navigation_bar(self, p1 = ""):
        pass

    def he_is_taken_p2(self, p2 = ""):
        pass

    def the_student_clicks_on_the_p1_arrow_from_the_bottom_of_the_screen(self, p1 = ""):
        pass

    def a_student_on_the_p1_of_the_final_exam_player(self, p1 = "p1"):
        pass

    def the_user_clicks_on_the_p2(self, p2 = ""):
        pass

    def nothing_happens_and_the_arrow_is_disabled(self):
        pass

    def it_is_the_final_exam_period_for_a_pre_ap_subject(self):
        pass

    def the_student_opens_the_final_exam_player_for_the_quiz_that_was_assigned_to_his_class(self):
        pass

    def he_sees_the_correct_exam_title_to_the_right_side_of_the_logo_subject_name__quiz_title(self):
        pass

    def a_student_opens_the_final_exam_player_for_the_quiz_that_was_assigned_to_his_class(self):
        pass

    def he_sees_his_first_and_last_name_to_the_right_side_of_the_exam_title(self):
        pass

    def the_exam_player_displays_the_element_well_without_overlapping_other_ui_elements(self):
        pass

    def in_a_pretest_cohort_school(self):
        pass

    def the_p1(self, p1 = ""):
        pass

    def a_student_on_the_final_exam_player_of_a_subject(self):
        pass

    def it_is_the_final_exam_period_for_a_subject(self):
        pass

    def the_following_change_happens_p6(self, p6 = ""):
        pass

    def the_student_has_not_answered_all_the_questions(self):
        pass

    def the_pop(self):
        pass

    def the_popup_contains_warning_you_have_not_finished_answering(self):
        pass

    def the_popup_contains_warning_message_you_havent_filled_everything_out_yet(self):
        pass

    def the_student_has_answered_all_the_questions(self):
        pass

    def the_popup_does_not_contain_warning_message_you_havent_filled_everything_out_yet(self):
        pass

    def the_list_seen_is_ordered_alphabetical_by_student_last_name_student_first_name(self):
        pass

    def a_ap_pre_ap_teacher_on_p1_page__results_tab_question_level_view_mcq_question(self, p1 = "p1"):
        pass

    def is_able_to_see_the_assign_button_for_a_unit_test_and_the_flag_new_assignment_modal__off(self):
        pass

    def teacher_is_able_to_see_the_old_assign_popover_window(self):
        pass

    def teacher_is_able_to_see_the_assign_modal_window(self):
        pass

    def the_flag_new_assignment_modal__off(self):
        pass

    def teacher_is_able_to_see_the_old_assign_popover(self):
        pass

    def a_student_first_opening_the_final_exam_player_of_a_subject(self):
        pass

    def he_inspects_the_question_navigation_bar(self):
        pass

    def no_question_is_bookmarked(self):
        pass

    def he_clicks_on_the_bookmark_icon_next_to_a_unmarked_question(self):
        pass

    def the_bookmark_icon_fills_in_orange(self):
        pass

    def a_mini_orange_bookmark_icon_appears_above_its_question_in_the_question_navigation_bar(self):
        pass

    def he_clicks_on_the_filledin_orange_bookmark_icon_next_to_a_marked_question(self):
        pass

    def the_bookmark_icon_returns_to_an_orange_outline_state(self):
        pass

    def the_mini_bookmark_icon_disappears_from_its_question_circle_in_the_question_navigation_bar(self):
        pass

    def he_navigates_to_a_question(self):
        pass

    def he_sees_to_the_right_side_of_the_question_name_a_small_orange_empty_icon(self):
        pass

    def a_student_first_opening_a_final_exam_player_of_a_subject(self):
        pass

    def some_questions_have_been_marked_and_some_left_unmarked(self):
        pass

    def he_navigates_through_questions(self):
        pass

    def each_question_has_the_same_state_for_the_bookmark_icon_as_the_one_displayed_in_the_question_navigation_bar(self):
        pass

    def a_student_when_first_opening_a_final_exam_player_for_a_subject(self):
        pass

    def he_inspects_the_right_side_of_the_screen(self):
        pass

    def he_sees_under_the_tool_bar_a_standalone_white_box_with_a_black_submit_icon_looks_like_paper_with_arrow(self):
        pass

    def a_student_on_the_final_exam_player_for_a_subject(self):
        pass

    def he_hovers_over_the_submit_button(self):
        pass

    def the_submit_icon_is_highlighted_by_changing_its_color_from_black_to_blue(self):
        pass

    def shows_a_popover_with_text_submit_exam(self):
        pass

    def a_popover_with_text_submit_exam_is_displayed(self):
        pass

    def the_submit_icon_is_in_black(self):
        pass

    def he_answers_to_some_questions_of_the_player_but_not_all_of_them(self):
        pass

    def the_submit_icon_remains_black_not_highlighted(self):
        pass

    def he_answers_to_the_last_unanswered_question_of_the_player(self):
        pass

    def the_submit_icon_gets_automatically_highlighted_in_blue(self):
        pass

    def submit_exam_popover_is_displayed_near_it(self):
        pass

    def he_had_answered_to_p1_of_the_player(self, p1 = "p1"):
        pass

    def he_clicks_on_the_submit_button(self):
        pass

    def the_user_is_taken_to_the_submit_confirmation_popover(self):
        pass

    def a_student_hovering_over_the_submit_button_in_the_final_exam_player(self):
        pass

    def the_submit_exam_popover_is_displayed(self):
        pass

    def the_student_clicks_anywhere_else_in_the_screen(self):
        pass

    def the_popover_automatically_closes(self):
        pass

    def a_student_on_the_submit_confirmation_page_of_the_final_exam_player(self):
        pass

    def the_teacher_is_on_the_unit_assessment_page_assign_tab(self):
        pass

    def the_assign_modal_window_will_open_by_default_with_all_the_toggles_off(self):
        pass

    def the_assign_modal_window_will_open_by_default_with_the_section_quick_assign_expanded_and_more_options_collapsed(self):
        pass

    def the_assign_modal_window_will_contains_two_sections_quick_assign_and_more_options(self):
        pass

    def the_teacher_is_already_in_the_ua_assign_assign_modal_window(self):
        pass

    def the_teacher_looks_at_the_quick_assign_section(self):
        pass

    def he_sees_at_the_top_of_the_section_the_choose_classes_part(self):
        pass

    def in_the_bottom_of_the_section_he_sees_3_toggles_for_unlock_the_assessment_now_let_students_see_their_results_take_the_assessment_offline(self):
        pass

    def bellow_he_sees_the_text_your_students_can_begin_the_assessment_immediately_and_will_see_this_assignment_when_they_log_into_ap_classroom(self, your_students_can_begin_the_assessment_immediately_and_will_see_this_assignment_when_they_log_into_ap_classroom_ = "Your students can begin the assessment immediately and will see this assignment when they log into AP Classroom."):
        pass

    def the_teacher_is_already_in_the_ua_assign_assign_modal_window_quick_assign_section(self):
        pass

    def the_teacher_looks_at_the_unlock_the_assessment_now_toggle(self):
        pass

    def he_sees_on_the_right_side_a_blue_button_for_switching_onoff(self):
        pass

    def bellow_appears_the_text_your_students_can_begin_the_assessment_immediately_and_will_see_this_assignment_when_they_log_into_ap_classroom(self):
        pass

    def the_teacher_looks_at_the_let_students_see_their_results_toggle(self):
        pass

    def bellow_appears_the_text_students_can_view_their_multiple_choice_results_as_soon_as_they_complete_their_test_and_after_you_score_any_free_response_questions(self):
        pass

    def all_are_displayed_according_with_the_mockups_httpsentientstudiocomcb_fy4040_finalindex_starthtml_httpszplio2_g_oq9x_w(self):
        pass

    def the_teacher_looks_at_the_take_the_assessment_offline_toggle(self):
        pass

    def he_sees_on_the_right_side_a_button_for_switching_onoff(self):
        pass

    def bellow_appears_the_text_create_a_pdf_version_of_this_assessment_to_print_and_distribute_to_students_note_feedback_reports_are_only_available_for_you_and_your_students_if_scores_are_entered_online_enter_scores_and_find_our_ap_scoring_guidelines_online_in_the_progress_view_under_enter_scores(self):
        pass

    def after_one_blank(self):
        pass

    def the_teacher_is_already_in_the_ua_assign_assign_modal_window_more_options_section(self):
        pass

    def the_teacher_looks_at_the_set_date_and_time(self):
        pass

    def he_sees_bellow_the_text_specify_a_time_and_date_for_this_assessment_to_unlock_and_lock_automatically(self):
        pass

    def the_teacher_looks_at_the_set_time_limit(self):
        pass

    def he_sees_bellow_the_text_specify_a_time_limit_for_students_to_complete_the_assessment_students_will_see_a_timer_when_they_begin_when_times_up_students_can_continue_working_unless_you_manually_lock_the_assessment(self):
        pass

    def the_teacher_looks_at_the_rename_this_assessment_for_students(self):
        pass

    def he_sees_bellow_the_text_enter_a_unique_title_for_this_assessment_that_students_will_see_if_you_do_not_want_to_use_the_current_title(self):
        pass

    def the_teacher_is_already_in_the_ua_assign_assign_modal_window_for_an_assessment_with_at_least_one_frq_question_more_options_section(self):
        pass

    def the_teacher_looks_at_allow_student_scoring(self):
        pass

    def he_sees_bellow_the_text_students_will_be_able_to_view_the_scoring_guidelines_and_enter_scores_for_their_freeresponse_questions(self):
        pass

    def the_teacher_is_already_in_the_qb_assign_assign_modal_window_for_an_assessment_with_at_least_one_frq_question_more_options_section(self):
        pass

    def the_teacher_is_already_in_the_qb_assign_assign_modal_window_more_options_section(self):
        pass

    def he_expands_the_more_options_section(self):
        pass

    def he_sees_a_toggle_named_scramble_question_order_having_the_default_value_off(self):
        pass

    def the_teacher_is_already_in_the_qb_assign_assign_modal_window_quick_assign_section(self):
        pass

    def the_teacher_is_already_in_the_qb_assign_assign_modal_window(self):
        pass

    def the_teacher_is_on_the_question_bank_page_assign_tab(self):
        pass

    def the_teacher_is_already_in_the_assessments_assign_assign_modal_window_more_options_section(self):
        pass

    def the_teacher_is_already_in_the_assessments_assign_assign_modal_window_quick_assign_section(self):
        pass

    def a_student_on_a_question_of_the_final_exam_player_of_a_subject(self):
        pass

    def the_student_refreshes_the_page(self):
        pass

    def the_same_question_is_displayed_after_refresh_having_all_its_correct_elements_in_the_screen_title_content_focus_in_the_navigation_bar_x_out_total_element(self):
        pass

    def the_teacher_is_already_in_the_assessments_assign_assign_modal_window(self):
        pass

    def the_teacher_is_on_the_assessments_page_assign_tab(self):
        pass

    def they_look_like_in_the_mockups_httpsentientstudiocomcb_fy4040_finalindex_starthtml_httpszplio2_g_oq9x_w(self):
        pass

    def the_student_removes_the_answers_given_on_a_frq_question(self):
        pass

    def he_sees_the_the_appropriate_blue_outlined_circle_of_the_question_in_the_navigation_bar_changing_to_black(self):
        pass

    def the_blue_line_that_follows_this_circle_changes_also_to_black(self):
        pass

    def he_clicks_on_the_sharedunshared_icon_for_a_focus_quiz_unit_test(self):
        pass

    def he_sees_the_new_assign_modal_window(self):
        pass

    def it_looks_like_in_the_mockups_httpsentientstudiocomcb_fy4040_finalindex_starthtml_httpszplio2_g_oq9x_w(self):
        pass

    def an_ap_pre_ap_teacher_is_on_units_page_one_unit_expanded(self):
        pass

    def a_p1_in_the_usage_page_of_a_p2_subject_that_has_teacher_module_available(self, p1 = "", p2 = ""):
        pass

    def a_teacher_is_on_the_preview_window_of_one_assessment(self):
        pass

    def he_clicks_on_the_assign_button(self):
        pass

    def a_teacher_is_on_the_preview_window_of_one_focus_quiz_unit_test(self):
        pass

    def given_a_user_on_the_login_page(self):
        pass

    def whe(self):
        pass

    def a_p1_login_in(self, p1 = ""):
        pass

    def he_opens_usage_tab_for_a_p2_subject_that_has_teacher_modules_available(self, p2 = ""):
        pass

    def he_sees_teacher_modules_as_the_last_column_of_the_table_having_2_subcolumns_started_and_completed(self):
        pass

    def a_teacher_is_on_the_question_bank_create_tab_create_a_quiz_save_quiz(self):
        pass

    def a_coordadmin_login_in(self):
        pass

    def he_opens_usage_tab_for_a_subject_that_does_not_have_teacher_module_available(self):
        pass

    def he_does_not_see_any_teacher_modules_column_displayed_in_the_table(self):
        pass

    def the_teacher_looks_at_the_more_options_section(self):
        pass

    def he_sees_that_more_options_section_is_collapsed(self):
        pass

    def under_the_name_of_the_section_is_seen_the_text_set_date_and_time_limits_for_student_access_or_enable_additional_features_for_this_assessment(self):
        pass

    def he_sees_the_toolkit_panel_displayed_as_a_white_vertical_box_with_four_icons_in_this_order_p2(self, p2 = "p2"):
        pass

    def he_hovers_on_each_icon_from_the_toolkit_panel(self):
        pass

    def the_icon_is_highlighted_in_blue(self):
        pass

    def a_student_on_the_final_exam_player_of_p1(self, p1 = "p1"):
        pass

    def a_teacher_has_in_progress_x_modules_in_teacher_modules_tab_of_a_subject(self):
        pass

    def his_p2_logs_in_and_opens_usage_tab_for_the_above_subject(self, p2 = ""):
        pass

    def he_sees_started_subcolumn_of_teacher_modulesx_for_the_above_teacher(self):
        pass

    def a_teacher_has_completed_x_modules_in_teacher_modules_tab_of_a_subject(self):
        pass

    def he_sees_completed_subcolumn_of_teacher_modulesx_for_the_above_teacher(self):
        pass

    def a_student_on_score_by_rubric_page_of_a_frq_quiz(self):
        pass

    def he_navigates_to_the_last_page_of_the_scoring_form(self):
        pass

    def he_does_not_see_the_student_feedback_button(self):
        pass

    def a_teacher_has_x_modules_in_progress_and_y_modules_completed_in_teacher_modules_tab_of_a_subject(self):
        pass

    def he_completes_one_of_his_in_progress_modules(self):
        pass

    def he_sees_started_subcolumn_of_teacher_modulesx1_for_the_above_teacher(self):
        pass

    def sees_completed_subcolumn_of_teacher_modulesy1_for_the_above_teacher(self):
        pass

    def he_gives_answer_to_a_p1_question(self, p1 = ""):
        pass

    def a_green_popup_is_displayed_reading_auto_saved_at_hh_mm_ss_hhmms_stime_when_the_answer_is_given(self, auto_saved_at_hh_mm_ss = "Auto saved at: HH:MM:SS"):
        pass

    def he_has_given_an_answer_to_a_question(self):
        pass

    def the_student_changes_the_answer_to_that_question(self):
        pass

    def the_auto_saved_popup_is_displayed_again(self):
        pass

    def the_auto_saved_popup_is_displayed_for_a_couple_of_seconds(self):
        pass

    def then_closes_automatically(self):
        pass

    def he_sees_as_page_title_submit(self):
        pass

    def p1_questions_have_been_answered(self, p1 = ""):
        pass

    def he_clicks_on_no_button(self):
        pass

    def he_is_taken_back_to_the_test_player_to_the_last_question_he_was_on_before_clicking_submit(self):
        pass

    def there_are_unanswered_questions(self):
        pass

    def he_clicks_on_a_questions_link_from_the_questions_list(self):
        pass

    def he_is_taken_to_that_questions_page_in_the_test_player(self):
        pass

    def condition_questions_have_been_answered(self, p1 = ""):
        pass

    def he_inspect_the_last_sentence_of_the_page(self):
        pass

    def he_sees_are_you_sure_you_want_to_submit_your_exam_followed_by_2_buttons_no_and_yes(self):
        pass

    def there_p1_unanswered_questions(self, p1 = "p1"):
        pass

    def the_user_returns_to_the_player_and_gives_answer_to_p2_questions(self, p2 = ""):
        pass

    def submits_again_the_test(self):
        pass

    def p3_question_list(self, p3 = "p3"):
        pass

    def the_user_is_displayed(self):
        pass

    def the_user_is_displayed_the_edit_page(self):
        pass

    def a_student_has_answered_to_p1_questions_of_the_final_exam_player(self, p1 = "p1"):
        pass

    def he_clicks_on_yes_button_from_submit_confirmation_page(self):
        pass

    def he_navigates_to_submit_confirmation_page_by_clicking_on_submit_exam_button(self):
        pass

    def exit_page_is_displayed_with_the_following_elements_submit_title__you_have_successfully_submitted_your_exam_it_is_now_safe_to_exit_browser_text__exit_button(self):
        pass

    def a_student_on_the_exit_page_of_the_submit_outside_of_time_limit_screen(self):
        pass

    def the_student_clicks_on_exit_button(self):
        pass

    def he_exits_the_secure_browser(self):
        pass

    def the_exam_is_submitted(self):
        pass

    def he_inspects_the_bottom_of_the_screen(self):
        pass

    def he_sees_no_button_on_white_background_not_highlighted(self):
        pass

    def to_its_right_the_yes_button_being_highlighted_in_blue(self):
        pass

    def to_its_right_yes_button_being_highlighted_in_blue(self):
        pass

    def he_answers_to_all_the_questions_of_the_quiz(self):
        pass

    def clicks_on_submit_exam_button(self):
        pass

    def submit_confirmation_page_is_displayed_containing_the_following_elements_p2(self, p2 = "p2"):
        pass

    def he_has_p1_unanswered_questions(self, p1 = ""):
        pass

    def he_returns_back_to_the_exam_player_and_gives_answer_to_p2(self, p2 = "p2"):
        pass

    def then_clicks_again_on_submit_exam_button(self):
        pass

    def then(self):
        pass

    def he_no_longer_sees_the_unanswered_questions_section_in_the_submit_confirmation_page(self):
        pass

    def a_student_leaves_p1_unanswered_in_his_exam_player(self, p1 = "p1"):
        pass

    def he_clicks_on_submit_exam_button(self):
        pass

    def he_sees_in_the_submit_confirmation_page_the_unanswered_section_with_the_info_text_p2(self, p2 = ""):
        pass

    def a_student_leaves_cond_unanswered_in_his_exam_player(self, p1 = "p1"):
        pass

    def he_sees_p2_in_the_unanswered_questions_list(self, p2 = "p2"):
        pass

    def p3(self, p3 = "res"):
        pass

    def p3_jsdhfjds(self, p3 = ""):
        pass

    def p3_jshdaskjhdsa(self, p3 = "p3"):
        pass

    def fdh(self, pdjks = ""):
        pass

    def he_leaves_a_lot_of_unanswered_questions_and_clicks_on_submit_exam_button(self):
        pass

    def he_is_taken_to_submit_confirmation_page_and_the_list_of_unanswered_questions_has_a_scroll_bar_which_allows_navigation_in_the_list(self):
        pass

    def there_are_several_unanswered_questions(self):
        pass

    def the_user_returns_to_the_player_and_gives_answer_to_some_of_the_unanswered_questions(self):
        pass

    def the_unanswered_question_list_gets_updated_and_no_longer_displays_these_questions(self):
        pass

    def a_student_answers_p1_questions_of_the_final_exam_player(self, p1 = "p1"):
        pass

    def i_can_see_the(self):
        pass

    def i_can_see_the_prompt_section_of_the_question_in_preview_mode(self):
        pass

    def there_are_x_unanswered_questions(self):
        pass

    def the_user_returns_to_the_player_and_answers_y_unanswered_questions(self):
        pass

    def the_unanswered_question_number_changes_from_x_to_xy_in_the_text_info_of_the_submit_confirmation_popup(self):
        pass

    def it_is_the_final_exam_period_for_a_p1_subject(self, p1 = "p1"):
        pass

    def he_sees_the_college_board_p1_logo_in_the_left_upper_corner_of_the_screen(self, p1 = ""):
        pass

    def a_student_on_the_homepage_of_an_p2_subject_opened_from_a_mobile_device_on_portrait_view_having_a_p1_resolution(self, p1 = "p1", p2 = "p2"):
        pass

    def he_scrolls_up_and_down_on_a_longer_question(self):
        pass

    def he_sees_the_p1_as_locked_on_the_screen(self, p1 = "p1"):
        pass

    def the_browser_page_is_minimized(self):
        pass

    def the_student_scrolls_up_and_down_on_a_longer_question(self):
        pass

    def he_sees_the_header_navigation_controls_tools_and_zoom_control_and_white_space_in_between_locked_on_the_screen(self):
        pass

    def the_exam_contains_at_least_one_question_with_multiple_passages(self):
        pass

    def he_navigates_to_that_question_and_clicks_on_passage_two_tab(self):
        pass

    def passage_two_content_is_displayed(self):
        pass

    def the_exam_contains_a_question_with_multiple_passages(self):
        pass

    def he_navigates_to_the_multiple_passages_question(self):
        pass

    def he_is_able_to_view_its_passages_displayed_in_different_tabs(self):
        pass

    def the_exam_contains_a_question_with_x_passages(self):
        pass

    def he_navigates_to_that_question(self):
        pass

    def he_sees_a_bar_displaying_x_tabs_each_one_named_passage_one_passage_two_passage_x(self):
        pass

    def the_exam_contains_at_least_2_questions_with_multiple_passages(self):
        pass

    def he_navigates_to_question_a_and_clicks_on_passage_x(self):
        pass

    def switches_to_question_b(self):
        pass

    def he_sees_question_b_with_all_its_passages(self):
        pass

    def passage_one_is_displayed_by_default(self):
        pass

    def the_exam_contains_at_least_a_question_with_multiple_passages(self):
        pass

    def he_sees_passage_one_displayed_by_default(self):
        pass

    def the_exam_contains_a_question_with_a_number_of_passages_so_that_there_is_p1(self, p1 = "p1"):
        pass

    def he_is_able_to_view_its_passages_displayed_in_different_tabs_p2_available(self, p2 = "p2"):
        pass

    def he_navigates_to_a_question_with_multiple_passages(self):
        pass

    def he_navigates_to_a_question_with_multiple_passages_and_opens_a_passage_p1(self, p1 = ""):
        pass

    def the_passage_that_is_on_display_has_the_tab_name_black(self):
        pass

    def the_other_passage_tabs_names_are_blue(self):
        pass

    def the_exam_contains_a_question_with_more_than_3_passages(self):
        pass

    def he_clicks_on_back_next_nav_arrows_of_the_passage_bar(self):
        pass

    def he_can_navigate_through_passages(self):
        pass

    def a_student_viewing_a_question_with_multiple_passages_from_the_final_exam_player_of_a_subject(self):
        pass

    def he_navigates_to_the_p1_passage_of_the_question(self, p1 = "p1"):
        pass

    def he_does_not_see_a_p2_arrow_in_the_passage_nav_bar(self, p2 = "p2"):
        pass

    def a_student_on_a_question_with_more_than_3_passages_from_the_final_exam_player(self):
        pass

    def he_p1_over_an_arrow_from_the_passage_nav_bar(self, p1 = "p1"):
        pass

    def he_sees_the_arrow_displayed_in_p2_color(self, p2 = "p2"):
        pass

    def the_exam_contains_a_question_with_one_passage(self):
        pass

    def the_student_navigates_to_that_question(self):
        pass

    def he_sees_the_question_with_its_passage_without_any_navigation_tab_bars(self):
        pass

    def he_clicks_on_the_next_nav_arrow_of_the_passage_bar(self):
        pass

    def the_last_passage_becomes_the_first_one_in_the_passage_nav_bar(self):
        pass

    def a_student_on_a_question_with_multiple_passages_from_the_final_exam_player(self):
        pass

    def a_passage_is_displayed_as_p1(self, p1 = "p1"):
        pass

    def the_student_clicks_on_p2_button(self, p2 = "p2"):
        pass

    def the_passage_becomes_p3(self, p3 = "p3"):
        pass

    def the_button_changes_to_p3_followed_by_its_specific_icon(self, p3 = "p3"):
        pass

    def a_student_on_a_question_with_p1_passages_from_the_final_exam_player(self, p1 = "p1"):
        pass

    def the_student_inspects_the_screen(self):
        pass

    def he_p3_expand_collapse_button(self, p3 = "p3"):
        pass

    def a_student_on_the_submit_confirmation_page_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_inspects_the_header_of_the_screen(self):
        pass

    def he_sees_only_2_elements_college_board_logo__logo(self):
        pass

    def a_student_on_the_help_menu_page_of_a_final_exam_player_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_sees_only_2_elements_college_board_logo__ap_pre_ap_logo(self):
        pass

    def a_student_on_the_final_exam_player_of_a_subject(self):
        pass

    def he_clicks_on_the_help_menu_icon_from_the_toolkit_bar(self):
        pass

    def help_menu_page_is_opened(self):
        pass

    def help_menu_page_opens_and_displays_the_following_ui_elements_header_bar_title_timer_element_2_tabs_and_x_button(self):
        pass

    def help_menu_page_opens_and_displays_as_page_title_help(self, help = "Help"):
        pass

    def help_menu_page_opens_and_displays_under_the_page_title_at_the_top_left_the_timer_element_that_matches_the_style_on_test_player(self):
        pass

    def a_student_on_the_help_page_of_the_final_exam_player_of_a_subject(self):
        pass

    def he_clicks_on_the_x_button_or_outside_the_modal(self):
        pass

    def help_page_closes_and_user_is_taken_back_to_the_question_from_where_he_opened_help_menu(self):
        pass

    def help_page_opens_and_contains_2_tabs_displayed_in_this_order_tools_opened_by_default_and_graphing_calculator(self):
        pass

    def he_clicks_on_tools_tab(self):
        pass

    def he_sees_an_info_text_that_reads_click_a_test_icon_to_learn_more_about_it_and_its_functions_followed_by_5_icons_calculator_annotation_accessibility_bookmark_expand(self, click_a_test_icon_to_learn_more_about_it_and_its_functions = "Click a test icon to learn more about it and its functions."):
        pass

    def he_sees_the_selected_icon_becomes_black(self):
        pass

    def a_section_is_displayed_with_the_title_p1_in_bold(self, p1 = "p1"):
        pass

    def he_sees_the_first_subtab_calculator_opened_and_highlighted_by_default(self):
        pass

    def he_clicks_on_p1_icon_from_tools_tab(self, p1 = "p1"):
        pass

    def an_info_text_below_to_explain_what_this_tool_does(self):
        pass

    def he_clicks_on_p1_tab(self, p1 = "p1"):
        pass

    def the_tab_turns_black_and_underlined_while_p2_becomes_blue(self, p2 = "p2"):
        pass

    def he_clicks_on_the_graphing_calculator_tab(self):
        pass

    def he_sees_desmos_tutorial_video_on_how_to_use_the_graphing_calculator(self, help = "Help"):
        pass

    def he_sees_a_desmos_tutorial_video_on_how_to_use_the_graphing_calculator(self):
        pass

    def he_clicks_on_the_accessibility_icon_from_the_toolkit_bar(self):
        pass

    def accessibility_page_is_opened(self):
        pass

    def a_student_on_the_accessibility_page_of_a_final_exam_player(self):
        pass

    def a_student_on_the_accessibility_page_of_the_final_exam_player_of_a_subject(self):
        pass

    def accessibility_page_closes_and_user_is_taken_back_to_the_question_from_where_he_opened_accessibility_menu(self):
        pass

    def accessibility_page_opens_and_displays_under_the_page_title_at_the_top_left_the_timer_element_that_matches_the_style_on_test_player(self):
        pass

    def accessibility_page_opens_and_displays_as_page_title_accessibility_options(self):
        pass

    def he_clicks_on_font_size_tab(self):
        pass

    def he_sees_an_info_text_under_it_that_reads_change_the_background_and_foreground_colours_of_the_examination(self):
        pass

    def he_clicks_on_color_scheme_tab(self):
        pass

    def he_sees_an_info_text_under_it_that_reads_adjust_the_size_of_fonts_in_your_activity(self):
        pass

    def the_tab_turns_black_and_underlined_while_p2_tab_becomes_blue(self, p2 = "p2"):
        pass

    def accessibility_page_opens_and_contains_2_tabs_displayed_in_this_order_color_scheme_opened_by_default_and_font_size(self):
        pass

    def he_action(self, p2 = "p2"):
        pass

    def accessibility_page_opens_and_displays_2_buttons_at_the_bottom_of_the_page_cancel_and_ok_highlighted_on_blue(self):
        pass

    def he_selects_a_p1_tab(self, p1 = "p1"):
        pass

    def then_clicks_on_cancel_button(self):
        pass

    def the_user_is_returned_to_the_final_exam_player_where_he_does_not_see_any_p2_change(self, p2 = "p2"):
        pass

    def he_clicks_on_color_scheme_tab(self):
        pass

    def he_sees_inside_the_tab_an_info_text_followed_by_the_colors_displayed_as_radio_buttons_options_black_on_white_default_selected_by_default__grey_on_light_grey_purple_on_light_green__black_on_violet_yellow_on_navy_and_white_on_black(self):
        pass

    def he_sees_inside_the_tab_an_info_text_followed_by_the_font_size_options_displayed_as_radio_buttons_normal_100_selected_by_default__large_125__extra_large_150_huge_175(self):
        pass

    def the_user_sees_the_change_in_the_accessibillity_page(self):
        pass

    def then_clicks_on_ok_button(self):
        pass

    def the_user_is_returned_to_the_final_exam_player_where_he_sees_the_p2_change(self, p2 = "p2"):
        pass

    def he_selects_p1_option_from_color_scheme_tab(self, p1 = "p1"):
        pass

    def clicks_on_ok_button(self):
        pass

    def the_user_is_returned_to_the_final_exam_player_where_he_sees_the_text_of_the_questions_in_p2_color_on_p3_background_color(self, p2 = "p2", p3 = "p3"):
        pass

    def the_bars_panels_grids_and_navigation_buttons_the_other_way_around(self):
        pass

    def the_student_is_returned_to_the_player_where_he_sees_the_text_of_the_questions_in_p3_color_on_p2_background(self, p3 = "", p2 = ""):
        pass

    def the_user_is_returned_to_the_player_where_he_sees_the_text_of_the_questions_zoomed_out_to_p2_size(self, p2 = "p2"):
        pass

    def he_selects_p1_option_from_font_size_tab(self, p1 = "p1"):
        pass

    def the_other_elements_on_the_screen_are_not_affected_by_this(self):
        pass

    def a_student_on_the_accessibility_page_of_a_final_exam_player_opened_in_p1(self, p1 = "p1"):
        pass

    def he_the_page(self):
        pass

    def all_the_ui_elements_render_correct(self):
        pass

    def he_updates_p1_over_an_already_existing_selected_option(self, p1 = "p1"):
        pass

    def the_new_selected_setting_is_applied(self):
        pass

    def a_student_on_the_final_exam_player_page_opened_in_p1(self, p1 = "p1"):
        pass

    def he_uses_the_zoom_tool_to_zoom_inout(self):
        pass

    def test_player_zoom_inout_and_all_the_ui_elements_render_ok(self):
        pass

    def a_student_navigating_to_a_question_on_the_final_exam_player(self):
        pass

    def he_clicks_on__magnify_icon_at_the_bottom_of_the_page(self):
        pass

    def the_page_expands_and_shows_the_expanded_version_without_any_ui_issues_such_as_zoom_element_overlapping_next_button_etc(self):
        pass

    def the_expanded_form_of_the_zoom_tool_is_displayed_with_the_following_elements__arrow___magnify_glass__scroll_bar___magnify_glass__100_displayed_as_the_default_zoom_level(self):
        pass

    def a_student_navigating_to_a_p1_question_on_the_final_exam_player(self, p1 = "p1"):
        pass

    def the_user_clicks_the__magnify_icon_at_the_bottom_of_the_page(self):
        pass

    def the_zoom_tool_expands_without_any_ui_issues_such_as_zoom_element_overlapping_next_button_etc(self):
        pass

    def he_clicks_on_p1_magnify_icon(self, p1 = "p1"):
        pass

    def the_zoom_tool_has_already_been_expanded(self):
        pass

    def test_player_should_zooms_p2_with_one_level(self, p2 = "p2"):
        pass

    def a_student_on_a_question_on_the_final_exam_player(self):
        pass

    def the_user_clicks_the__arrow_from_the_zoom_tool(self):
        pass

    def the_expanded_zoom_widget_collapses_back_into_the_magnify_icon_in_the_white_box(self):
        pass

    def the_zoom_has_been_set_to_a_certain_value(self):
        pass

    def the_user_p1(self, p1 = "p1"):
        pass

    def final_exam_player_keeps_the_presetted_zoom_setting(self):
        pass

    def he_sees_only_2_elements_college_board_logo__p1_logo(self, p1 = "p1"):
        pass

    def a_student_on_the_accessibility_page_of_a_final_exam_player_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_sees_only_2_elements_college_board_logo__cond_logo(self, p1 = "p1"):
        pass

    def the_zoom_tool_is_collapsed(self):
        pass

    def the_user_hovers_over_the__magnify_icon(self):
        pass

    def the_icon_gets_highlighted_in_blue(self):
        pass

    def a_hover_message_is_displayed_zoom(self):
        pass

    def he_clicks_p2_on_the__magnify_glass_from_the_zoom_widget(self, p2 = "p2"):
        pass

    def test_player_zooms_to_p3(self, p3 = "p2"):
        pass

    def the_zoom_widget_is_expanded(self):
        pass

    def the_zoom_is_set_to_p1(self, p1 = "p1"):
        pass

    def a_student_on_the_final_exam_player_having_the_zoom_widget_expanded(self):
        pass

    def he_clicks_p2_on_the__magnify_glass_from_the_zoom_widget(self, p2 = "p2"):
        pass

    def the_zoom_tool_is_expanded(self):
        pass

    def the_user_zooms_inout_from_the_keyboard_using_for_eg_ctrl____ctrl__(self):
        pass

    def the_entire_browser_page_is_zoomed_inout(self):
        pass

    def this_action_has_no_effect_over_the_zoom_settings_of_the_test_player(self):
        pass

    def the_user_manually_drags_the_zoom_handle_towards_p1_magnify_icon(self, p1 = "p1"):
        pass

    def the_zoom_level_on_the_page_p2_in_10_increments(self, p2 = "p2"):
        pass

    def afterwards_clicks_once_on_the_p1_magnify_icon(self, p1 = "p1"):
        pass

    def the_user_manually_drags_the_zoom_handle_towards_150_level(self):
        pass

    def a_student_on_a_question_on_the_final_exam_player_having_the_zoom_tool_expanded(self):
        pass

    def the_zoom_level_on_the_page_gets_set_to_p2(self, p2 = "p2"):
        pass

    def the_user_clicks_on_p1_magnify_icon_from_the_zoom_tool_until_reaching_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def afterwards_manually_drags_the_zoom_handle_towards_a_150(self):
        pass

    def the_zoom_level_on_the_page_gets_set_to_150(self):
        pass

    def afterwards_collapses_the_zoom_tool(self):
        pass

    def the_zoom_level_remains_set(self):
        pass

    def a_student_on_the_submit_outside_of_time_limit_page_of_a_p1_final_exam(self, p1 = "p1"):
        pass

    def a_student_on_p1_of_the_final_exam_player(self, p1 = "p1"):
        pass

    def the_time_elapsed_hits_the_total_time_allotted_for_the_exam(self):
        pass

    def the_student_is_sent_automatically_to_the_submit_outside_time_limit_page(self):
        pass

    def he_is_taken_to_submit_popup_where_he_sees_the_following_ui_elements_title_submit__info_text__p2___no_yes_buttons(self, p2 = "p2"):
        pass

    def a_student_on_the_submit_outside_time_limit_page(self):
        pass

    def he_inspects_the_info_text_displayed_under_the_timer_element(self):
        pass

    def he_reads_your_test_time_has_expired_and_your_exam_has_been_submitted(self):
        pass

    def the_student_is_sent_automatically_to_the_submit_outside_time_limit_page_where_he_sees_the_timer_element_positioned_between_the_title_and_the_info_text(self):
        pass

    def the_timer_is_displayed_on_a_red_ribbon_and_has_the_value_hhmm_hhmm_where_the_values_are_equal(self):
        pass

    def he_clicks_on_the_ok_button(self):
        pass

    def the_user_is_redirected_to_the_exit_page(self):
        pass

    def a_student_on_the_submit_popup_of_a_timed_assessment(self):
        pass

    def he_clicks_on_submit_now_button(self):
        pass

    def submit_confirmation_popup_is_displayed_where_he_sees_a_title_submit_followed_by_an_info_text_you_have_successfully_submitted_your_assessment_and_an_exit_button(self):
        pass

    def a_student_on_the_cond_of_the_final_exam_player(self, p1 = "p1"):
        pass

    def the_student_clicks_on_the_back_button_from_the_browser_header(self):
        pass

    def he_exits_the_secure_browser_and_the_exam_is_submitted(self):
        pass

    def the_student_leaves_the_page_by_login_out_and_login_back_in(self):
        pass

    def he_sees_the_exam_as_submitted_and_no_longer_has_access_to_work_on_it(self):
        pass

    def the_user_zooms_in_to_a_bigger_value_using_the_zoom_widget(self):
        pass

    def the_test_player_is_zoomed_in_and_displays_vertical_and_horizontal_scroll_bars_to_allow_the_user_to_see_the_entire_content_of_the_screen(self):
        pass

    def he_logs_in_and_navigates_to_the_homepage_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_inspects_the_bottom_of_the_page(self):
        pass

    def he_sees_at_the_bottom_of_the_page_the_units_of_the_subject_displayed_each_unit_in_a_tab(self):
        pass

    def a_teacher_logs_in(self):
        pass

    def a_coordadmin_on_the_login_page(self, datatable = "||", free_text = ""):
        pass

    def the_student_clicks_on_begin_button_of_a_learnosity_assessment(self):
        pass

    def the_student_begins_a_timed_learnosity_assessment(self):
        pass

    def the_learnosity_player_is_used_for_taking_the_quiz(self):
        pass

    def a_student_is_taking_a_timed_learnosity_assessment(self):
        pass

    def the_student_is_on_the_learnosity_quiz_player(self):
        pass

    def the_student_is_seeing_the_countdown_timer_in_the_upper_right_corner(self):
        pass

    def the_countdown_timer_has_5_minutes_left_and_less(self):
        pass

    def the_the_countdown_timer_is_displayed_with_a_red_background(self):
        pass

    def he_logs_in_and_navigates_to_the_homepage_of_a_subject(self):
        pass

    def he_sees_units_label_displayed_as_title_of_the_units_section(self):
        pass

    def he_p2_on_the_right_side_of_the_units_title_a_filter_icon_followed_by_the_text_filter_units(self, p2 = "p2"):
        pass

    def for_each_unit_he_sees_the_tab_title_unit_number(self):
        pass

    def he_sees_the_unit_tabs_ordered_ascending_by_the_unit_number(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject(self):
        pass

    def he_clicks_on_a_unit_tab(self):
        pass

    def that_tab_becomes_highlighted_on_white(self):
        pass

    def he_sees_at_the_bottom_of_the_page_the_units_of_the_subject_displayed_each_unit_with_its_content_in_a_tab(self):
        pass

    def g(self):
        pass

    def a_teacher_is_on_the_progress_tab_of_unit_assessments(self):
        pass

    def an_assessment_was_assigned_to_students(self):
        pass

    def the_teacher_clicks_on_that_assessment(self):
        pass

    def no_student_has_started_that_assessment(self):
        pass

    def the_progress_bar_should_be_solid_gray_and_labeled_not_started(self):
        pass

    def at_least_one_student_has_started_the_assessment_but_not_submitted_it(self):
        pass

    def the_teacher_should_see_a_part_of_the_progress_bar_is_light_blue_labeled_p1(self, p1 = ""):
        pass

    def at_least_one_student_has_submitted_the_assessment(self):
        pass

    def the_teacher_should_see_a_part_of_the_progress_bar_is_dark_blue_and_labeled_complete(self):
        pass

    def a_teacher_is_on_the_progress_tab_of_question_bank(self):
        pass

    def the_assessment_has_no_fr_qs(self):
        pass

    def a_teacher_is_on_the_ua_progress_tab(self):
        pass

    def the_teacher_looks_at_progress_bar_for_one_assignment_where_no_students_have_started_the_assignment(self):
        pass

    def the_progress_tab_contains(self):
        pass

    def the_progress_bar_is_gray_and_the_text_not_started_appears_in_white_in_the_bar(self):
        pass

    def he_inspects_the_tab_of_a_unit_where_the_students_have_submitted_the_mcq_parts_of_the_progress_check(self):
        pass

    def he_sees_the_top_border_of_the_tab_colored_the_same_as_the_circle_within_the_tab(self):
        pass

    def a_teacher_on_question_bank_progress_tab(self):
        pass

    def the_teacher_looks_at_progress_bar(self):
        pass

    def there_are_opened_unlocked_assignments_where_no_students_have_started_the_assignment(self):
        pass

    def sees_that_the_progress_bar_is_gray_and_the_text_not_started_appears_in_white_in_the_bar(self):
        pass

    def sees_that_the_lock_icon_and_the_text_locked_appears_both_in_white_in_the_bar(self):
        pass

    def there_are_opened_unlocked_assignments_where_at_least_one_student_have_started_or_submitted(self):
        pass

    def sees_that_the_text_not_started_is_no_longer_written_on_the_bar(self):
        pass

    def sees_that_no_text_is_appearing_on_the_progress_bar(self):
        pass

    def the_progress_bar_should_be_solid_gray_and_labeled_not_started(self):
        pass

    def the_teacher_should_see_a_part_of_the_progress_bar_is_sky_blue_and_labeled_available_to_score(self):
        pass

    def one_student_has_not_started_that_assessment(self):
        pass

    def the_progress_bar_should_have_a_proportion_equal_to_1_divided_by_the_total_number_of_students_in_the_class_of_the_bar_dark_grey(self):
        pass

    def the_number_1_should_be_in_the_proportion(self):
        pass

    def one_student_has_started_but_not_submitted_that_assessment(self):
        pass

    def the_progress_bar_should_have_a_proportion_equal_to_1_divided_by_the_total_number_of_students_in_the_class_light_blue(self):
        pass

    def the_progress_bar_should_have_a_proportion_equal_to_1_divided_by_the_total_number_of_students_in_the_class_of_the_bar_dark_blue(self):
        pass

    def one_student_has_completed_that_assessment(self):
        pass

    def that_assessment_has_at_least_one_frq(self):
        pass

    def one_student_has_submitted_that_assessment(self):
        pass

    def the_progress_bar_should_have_a_proportion_equal_to_1_divided_by_the_total_number_of_students_in_the_class_sky_blue(self):
        pass

    def that_assessment_has_no_fr_qs(self):
        pass

    def a_teacher_is_on_the_progress_tab_of_assessments(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_that_has_more_than_11_units_available(self):
        pass

    def he_sees_the_first_11_units_of_the_subjects_displayed_in_visible_tabs(self):
        pass

    def that_assessment_is_locked(self):
        pass

    def a_teacher_visits_p1__progress__action_column(self, p1 = "", datatable = "||"):
        pass

    def the_teacher_will_see_open_assessment_with_green_background_and_white_text(self, p1 = ""):
        pass

    def test(self):
        pass

    def the_teacher_will_see_open_assessment_with_green_background_and_white_text(self):
        pass

    def all_students_have_submitted_that_assessment(self):
        pass

    def that_assessment_has_been_assigned_to_students(self):
        pass

    def that_assessment_has_been_assigned_to_studnets(self):
        pass

    def that_assessment_is_unlocked(self):
        pass

    def the_teacher_will_see_open_assessment_with_gray_background_and_white_text(self):
        pass

    def at_least_one_student_has_submitted_responses_to_that_assessment(self):
        pass

    def the_teacher_will_see_to_score_with_light_blue_background_and_white_text(self):
        pass

    def there_will_be_a_number_indicating_how_many_student_response_have_to_be_scored(self):
        pass

    def the_teacher_clicks_the_button_in_that_column(self):
        pass

    def the_teacher_will_be_taken_to_the_progress_view_of_that_assessment(self):
        pass

    def the_teacher_clicks_the_button_in_that_column(self):
        pass

    def the_teacher_clicks_on_the_button_in_that_column(self):
        pass

    def the_teacher_will_see_be_taken_to_the_progress_view_of_that_assessment(self):
        pass

    def the_quiz_becomes_unlocked(self):
        pass

    def the_question_details_slider_of_that_question_is_p1(self, p1 = "p1"):
        pass

    def the_due_date_final_due(self):
        pass

    def due_date_(self, datatable = "||"):
        pass

    def due_date__final_due(self):
        pass

    def the_quiz_should_be_unlocked_and_no_pop_up_message_is_displayed(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_with_multiple_unit_tabs_that_dont_fit_the_screen(self):
        pass

    def he_p1_over_an_arrow_from_the_unit_nav_bar(self, p1 = "p1"):
        pass

    def a_student_on_the_homepage_of_a_subject_with_only_one_unit_available_can_make_all_the_other_units_hidden_using_the_metadata_spreadsheet_import(self):
        pass

    def he_sees_the_unit_displayed_in_a_single_tab(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_with_multiple_units(self):
        pass

    def he_has_also_other_subjects_with_multiple_units(self):
        pass

    def navigates_to_another_subjects_with_multiple_units(self):
        pass

    def he_clicks_on_unit_3_tab(self):
        pass

    def he_sees_the_homepage_of_the_selected_subject_with_its_units_displayed(self):
        pass

    def unit_1_tab_is_opened_by_default(self):
        pass

    def the_unit_that_is_on_display_has_the_tab_name_black(self):
        pass

    def the_other_unit_tabs_names_are_blue(self):
        pass

    def the_subject_has_multiple_units_so_that_there_is_p1(self, p1 = "p1"):
        pass

    def the_teacher_inspects_the_bottom_of_the_screen(self):
        pass

    def he_is_able_to_view_the_units_displayed_in_different_tabs_p2_available(self, p2 = "p2"):
        pass

    def the_subject_has_multiple_units(self):
        pass

    def the_teacher_clicks_on_unit_2_tab(self):
        pass

    def unit_2_content_is_displayed(self):
        pass

    def he_navigates_to_the_p1_unit_tab(self, p1 = "p1"):
        pass

    def a_teacher_enrolled_in_a_single_subject_with_multiple_units(self):
        pass

    def he_sees_on_the_homepage_the_first_unit_tab_opened_by_default_along_its_content(self):
        pass

    def the_space_does_not_allow_the_display_of_all_the_units_tab(self):
        pass

    def he_clicks_on_back_next_nav_arrows_of_the_unit_nav_bar(self):
        pass

    def he_can_navigate_through_units(self):
        pass

    def there_is_not_s(self):
        pass

    def he_clicks_on_the_next_nav_arrow_of_the_unit_nav_bar(self):
        pass

    def the_last_unit_becomes_the_first_one_in_the_unit_nav_bar(self):
        pass

    def he_logs_in_and_navigates_to_the_homepage_of_a_subject_subject(self, p1 = "p1"):
        pass

    def a_teacher_on_the_login_page_opened_on_p2_using_p3(self, p2 = "p2", p3 = "p3"):
        pass

    def he_clicks_on_a_unit_tab_within_units_section(self):
        pass

    def he_sees_under_unit_title_the_specific_unit_resources_p2(self, p2 = "p2"):
        pass

    def a_teacher_on_the_homepage_of_a_p1_subject(self, p1 = "p1"):
        pass

    def he_sees_for_each_unit_tab_a_unit_title_displayed_under_it(self):
        pass

    def he_clicks_on_p2_resource_under_a_unit_tab_within_units_section(self, p2 = "p3"):
        pass

    def the_unit_resource_opens_in_a_new_tab_accordingly(self):
        pass

    def the_following_happens_p3(self, p3 = ""):
        pass

    def he_sees_under_unit_resources__the_specific_subunits_in_blue(self):
        pass

    def a_user_is_on_the_progress_page_of_unit(self):
        pass

    def a_user_is_on_the_progress_page_of_unit_for_a_subject(self):
        pass

    def the_user_hears_action_column_6__result_button(self):
        pass

    def the_user_hears_action_column_6_(self, datatable = "||"):
        pass

    def a_metadata_import_was_done_for_a_subject_with_units(self):
        pass

    def the_new_columns_p1_added_and_populated_in_the_spreadsheet(self, p1 = "p1"):
        pass

    def a_teacher_logs_in_and_navigates_to_the_above_subject_homepage(self):
        pass

    def clicks_on_a_unit_tab_from_units_section(self):
        pass

    def he_sees_under_unit_title_p2_displayed_as_rows_followed_by_the_data_populated_in_the_spreadsheet(self, p2 = "p2"):
        pass

    def the_new_columns_p1_added_but_not_populated_in_the_spreadsheet(self, p1 = "p1"):
        pass

    def he_does_not_see_any_additional_descriptive_information_under_the_unit_title_of_the_unit_tab(self):
        pass

    def the_columns_instructional_periods__ap_exam_weighting_were_not_added_in_the_spreadsheet(self):
        pass

    def incorrect_labels_were_added_in_the_columns_specific_for_instructional_periods__ap_exam_weighting_of_a_spreadsheet_file(self):
        pass

    def a_user_tries_to_import_the_above_file(self):
        pass

    def an_error_is_thrown_in_the_importer_tool_and_user_cannot_go_through_with_the_import_process(self):
        pass

    def the_new_instructional_periods_and_ap_exam_weighting_columns_were_added_and_populated_in_the_spreadsheet(self):
        pass

    def he_sees_under_unit_title_first_row_instructional_periods_with_its_data_populated_from_the_spreadsheet(self):
        pass

    def then_the_second_row_ap_exam_weighting_with_its_data_populated_from_the_spreadsheet(self):
        pass

    def a_metadata_import_was_done_for_a_subject_with_units_and_the_new_instructional_periods_and_ap_exam_weighting_columns_were_added_and_populated_in_the_spreadsheet(self):
        pass

    def the_new_instructional_periods_and_ap_exam_weighting_columns_were_added_and_populated_in_the_spreadsheet(self):
        pass

    def he_sees_under_unit_title_the_following_p2(self, p2 = "p2"):
        pass

    def he_sees_under_unit_title_instructional_periods_label_in_light_blue_followed_by_its_value_in_dark_blue(self):
        pass

    def ap_exam_weighting_label_in_dark_blue_followed_by_its_value_in_light_blue(self):
        pass

    def he_sees_the_p2_arrow_displayed_as_disabled_in_the_unit_nav_bar(self, p2 = "p2"):
        pass

    def a_metadata_import_was_done_for_a_p2_subject_having_units_with_skills_associated_to_its_topics(self, p2 = "p2"):
        pass

    def a_p1_logs_in_and_navigates_to_the_above_subject_homepage(self, p1 = "p1"):
        pass

    def he_sees_a_new_column_containing_skills_associated_to_the_subunits_on_the_left_side(self):
        pass

    def the_skills_column_was_not_added_in_the_spreadsheet(self):
        pass

    def he_does_not_see_any_skills_associated_to_its_subunits_nor_the_skills_column(self):
        pass

    def a_teacher_clicks_on_a_unit_tab_from_units_section_of_the_above_subject(self):
        pass

    def he_does_not_see_any_skills_associated_with_the_subunits_of_the_unit_nor_the_skills_column_on_the_screen(self):
        pass

    def user_is_displayed_a__tab_tab_with_a_blue_glow(self):
        pass

    def a_student_on_the_homepage_of_a_subject_with_all_the_units_marked_as_hidden(self):
        pass

    def he_sees_no_units_displayed(self):
        pass

    def he_logs_in_for_the_first_time(self):
        pass

    def first_unit_tab_with_its_content_is_opened_by_default(self):
        pass

    def a_multiple_subject_teacher_on_the_homepage_of_a_subject_with_units(self):
        pass

    def a_unit_tab_has_been_accessed(self):
        pass

    def he_navigate_to_a_different_page_of_the_same_subject(self):
        pass

    def then_returns_to_homepage(self):
        pass

    def he_sees_the_latest_unit_tab_accessed_opened_and_on_display(self):
        pass

    def a_p1_on_the_homepage_of_a_p2_subject_with_units(self, p1 = "p1", p2 = "p2"):
        pass

    def a_p1_with_multiple_ap_and_pre_ap_subjects_on_the_homepage_of_a_p2_subject_containing_units(self, p1 = "p1", p2 = "p2"):
        pass

    def he_navigate_to_a_different_page_of_a_p3_subject(self, p3 = "p3"):
        pass

    def then_returns_to_homepage_of_his_initial_subject(self):
        pass

    def a_multiple_subjects_teacher_on_the_homepage_of_a_subjects_with_units(self):
        pass

    def in_each_subject_he_opens_a_different_unit_tab(self):
        pass

    def he_navigates_back_to_each_subject_homepage(self):
        pass

    def he_sees_the_lastest_unit_tab_accessed_on_display_for_each_subject_along_its_content(self):
        pass

    def a_user_on_the_homepage_of_a_subjects_with_units(self):
        pass

    def he_cond(self, p2 = "p2"):
        pass

    def he_is_taken_to_the_homepage_of_the_above_subject(self):
        pass

    def a_teacher_opens_a_unit_tab_from_the_homepage_of_a_subjects(self):
        pass

    def he_clicks_on_an_assessment_link_under_that_unit(self):
        pass

    def then_clicks_on_close_preview_button_from_the_preview_of_that_assessment(self):
        pass

    def he_is_returned_to_the_homepage_of_the_subject_with_the_above_unit_tab_on_the_display_along_its_content(self):
        pass

    def a_teacher_on_a_unit_tab_from_the_homepage_of_a_subject(self):
        pass

    def he_navigates_to_ua_page__results_tab_of_an_assignment__class_student_performance_subtab__question_level__related_content__skills_section(self):
        pass

    def clicks_on_a_topic_belonging_to_a_different_unit_than_the_one_from_above(self):
        pass

    def he_is_taken_to_homepage_where_he_sees_on_display_the_unit_tab_that_holds_the_topic_selected_above(self):
        pass

    def a_student_on_the_progress_page(self):
        pass

    def has_a_submitted_learnosity_mixt_quiz_mcqfrq(self):
        pass

    def the_student_opens_the_review(self):
        pass

    def tries_to_change_any_answer(self):
        pass

    def he_cannot_change_any_answer(self):
        pass

    def his_previous_selection_will_be_highlighted_in_yellow_mcq_only(self):
        pass

    def he_will_not_see_correct_or_incorrect_answers_highlighted(self):
        pass

    def he_sees_the_latest_unit_tab_accessed_opened_along_with_its_content(self):
        pass

    def he_sees_the_latest_unit_tab_accessed_opened_with_its_content(self):
        pass

    def he_sees_the_lastest_unit_tab_accessed_on_display_along_its_content(self):
        pass

    def the_student_opens_the_score_page(self):
        pass

    def he_navigates_to_p1(self, p1 = "p1"):
        pass

    def from_there_uses_a_link_to_another_unit_for_the_above_subject_eg_httpsapclassroomcollegeboardorgsubject_idhomeunitnumber(self):
        pass

    def a_user_on_the_homepage_of_a_subject_having_on_display_a_specific_unit_tab_eg_unit_2(self):
        pass

    def the_initial_unit_tab_is_overriden_by_the_unit_tab_and_its_content_given_in_the_url(self):
        pass

    def the_list_of_allowed_users(self, datatable = ""):
        pass

    def trying_to_login_with_p1_and_without_p2(self, p1 = "", p2 = ""):
        pass

    def a_p1_logs_in(self, p1 = ""):
        pass

    def a_dataset_name_exists(self, datatable = "||", dataset_name = "Dataset name"):
        pass

    def that_dataset_name_action_a_class(self, dataset_name = "", action = "action"):
        pass

    def a_user_exists(self):
        pass

    def that_user_visits_page_progress(self, user = "", page = "Page"):
        pass

    def that_p1_visits_p2__progress(self, p1 = "", p2 = ""):
        pass

    def that_p1_will_see_all_ppc_assessments_already_assigned_to_the_class(self, p1 = ""):
        pass

    def those_ppc_assessments_are_locked(self):
        pass

    def he_sees_each_unit_and_its_content_displayed_in_a_tab(self):
        pass

    def a_page_to_recover_password_should_be_displayed(self):
        pass

    def a_teacher_on_the_password_recovery_page(self):
        pass

    def he_enters_a_valid_email(self):
        pass

    def the_email_is_in_the_system(self):
        pass

    def he_presses_on_request_reset_link(self):
        pass

    def the_teacher_will_receive_an_email_with_the_new_password(self):
        pass

    def the_email_is_not_in_the_system(self):
        pass

    def the_teacher_will_receive_an_error_message_that_the_email_is_not_in_the_system(self):
        pass

    def a_student_on_the_password_recovery_page(self):
        pass

    def the_student_will_receive_an_email_with_the_new_password(self):
        pass

    def the_student_will_receive_an_error_message_that_the_email_is_not_in_the_system(self):
        pass

    def a_student_on_the_create_account_page(self):
        pass

    def provides_for_password_not_matching_complexity_criteria(self):
        pass

    def an_error_message_regarding_the_password_match_is_thrown(self):
        pass

    def student_doesnt_fill_the_email_address(self):
        pass

    def error_is_show_that_the_email_fields_are_mandatory(self):
        pass

    def student_doesnt_fill_the_password(self):
        pass

    def error_is_show_that_the_password_field_is_mandatory(self):
        pass

    def from_there_uses_p2_as_link_to_another_unit_for_the_above_subject(self, p2 = "p2"):
        pass

    def student_doesnt_fill_the_field(self, field = "", datatable = "||"):
        pass

    def error_is_show_that_the_field_is_mandatory(self, p1 = ""):
        pass

    def he_is_taken_to_the_homepage_of_that_subject_where_he_sees_the_last_accessed_unit_ie_unit_2(self):
        pass

    def the_skills_column_was_added_in_the_spreadsheet_but_without_data_linked_to_it(self):
        pass

    def a_student_on_the_create_account(self):
        pass

    def a_user_on_the_login_page(self, datatable = "||", user = "User"):
        pass

    def the_user_does_not_have_an_accout(self, p1 = ""):
        pass

    def he_sees_the_register_get_started_button(self):
        pass

    def the_skills_column_was_added_in_the_spreadsheet_with_a_different_value_eg_practice__stimulus_type(self):
        pass

    def he_sees_the_imported_tag_label_as_column_name_for_the_skills_associated_with_the_subunits_of_the_unit(self):
        pass

    def a_teacher_on_the_create_account_page(self):
        pass

    def teacher_clicks_create_account_button(self):
        pass

    def a_teacher_on_the_create_account(self):
        pass

    def teacher_fills_in_the_join_code_and_the_rest_of_the_required_fields(self):
        pass

    def p1_associated_in_the_spreadsheet_to_a_subunit(self, p1 = "p1"):
        pass

    def a_teacher_clicks_on_the_unit_tab_containing_the_above_subunit(self):
        pass

    def sees_p2_associated_in_the_spreadsheet_with_the_subunit(self, p2 = "p2"):
        pass

    def multiple_skills_were_associated_in_the_spreadsheet_to_a_subunit_so_that_there_is_p1_space_on_the_screen(self, p1 = "p1"):
        pass

    def he_sees_all_the_skills_associated_with_that_subunit_displayed_p2(self, p2 = "p2"):
        pass

    def multiple_skills_were_associated_in_the_spreadsheet_p1_to_a_subunit(self, p1 = "p1"):
        pass

    def he_sees_the_skills_displayed_in_ascending_id_order_at_subunit_level_eg_1_a_1_b_2_b_3_a_3_c(self):
        pass

    def the_skills_column_was_not_added_in_the_spreadsheet_but_skill_data_was_added(self):
        pass

    def a_very_long_p1_label_was_added_in_the_spreadsheet(self, p1 = "p1"):
        pass

    def he_sees_the_long_elements_well_displayed_on_screen_without_causing_any_ui_issues(self):
        pass

    def multiple_skills_each_from_a_different_category_were_associated_each_to_a_different_subunit(self):
        pass

    def clicks_on_the_unit_tab_containing_all_the_above_units(self):
        pass

    def a_teacher_clicks_on_the_unit_tab_containing_all_the_above_subunits(self):
        pass

    def he_sees_for_p1_color_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def multiple_skills_each_from_a_different_category_were_associated_to_the_same_subunit(self):
        pass

    def a_metadata_import_was_done_for_multiple_subjects_with_units(self):
        pass

    def multiple_skills_categories_were_associated_to_subunits_of_these_subjects(self):
        pass

    def a_teacher_with_access_to_these_subjects_navigates_through_their_units(self):
        pass

    def a_teacher_is_on_the_unit_assessments_progress_tab(self):
        pass

    def he_sees_that_color_is_kept_across_subjects_for_the_same_skill_categories(self):
        pass

    def there_are_opened_unlocked_assignments_where_one_or_more_students_have_not_started_the_assignment(self):
        pass

    def the_teacher_sees_in_the_popup_an_empty_gray_circle_followed_by_the_gray_text_not_started_and_the_number_of_students_who_have_not_started_the_assessment(self):
        pass

    def the_number_of_students_is_displayed_with_bold_gray(self):
        pass

    def multiple_skills_from_the_same_category_eg_1_a_1_b_1_c_were_associated_to_a_subunit(self):
        pass

    def he_sees_that_color_is_kept_across_skills_of_the_same_category(self):
        pass

    def a_teacher_logs_in_and_from_subject_homepage_clicks_on_the_unit_tab_containing_the_above_subunit(self):
        pass

    def a_teacher_on_the_rpeap_final_app(self):
        pass

    def he_lands_on_the_my_exams_page(self):
        pass

    def sees_create_section_button(self):
        pass

    def sees_sections_list(self):
        pass

    def a_teacher_on_the_preap_final_app(self):
        pass

    def he_presses_on_create_section_button(self):
        pass

    def the_create_section_popover_is_displayed(self):
        pass

    def a_teacher_on_the_prea(self):
        pass

    def he_sees_a_pre_ap_program_dropdown(self):
        pass

    def the_dropdown_contains_prea_ap_subjects(self):
        pass

    def he_wants_to_create_a_new_section(self):
        pass

    def selects_prea_ap_whg_subject(self):
        pass

    def the_instructional_periods_checkboxes_will_appear(self):
        pass

    def the_teacher_will_be_able_to_select_any_of_them(self):
        pass

    def fills_up_all_required_fields(self):
        pass

    def the_section_is_not_created(self):
        pass

    def fills_up_only_section(self):
        pass

    def a_message_will_appear_to_fill_up_also_section_name(self):
        pass

    def the_section_will_not_be_created(self):
        pass

    def he_presses_on_cancel(self):
        pass

    def the_create_section_popup_is_closed(self):
        pass

    def the_section_is_created_successfully(self):
        pass

    def he_clicks_on_an_existing_class(self):
        pass

    def the_edit_section_popup_should_be_displayed(self):
        pass

    def a_teacher_on_the_edit_section_popup(self):
        pass

    def he_modifies_section_name_or_instructional_periods(self):
        pass

    def the_changes_are_not_saved(self):
        pass

    def he_clicks_save(self):
        pass

    def the_changes_are_saved(self):
        pass

    def he_clicks_on_delete(self):
        pass

    def he_confirms_the_delete(self):
        pass

    def the_section_is_deleted(self):
        pass

    def he_modifies_section_name(self):
        pass

    def the_new_columns_instructional_periods_and_ap_exam_weighting_were_added_and_populated_in_the_spreadsheet(self):
        pass

    def a_p1logs_in_and_navigates_to_the_above_subject_homepage(self, p1 = "p1"):
        pass

    def he_does_not_see_under_unit_title_p2_displayed_as_rows_followed_by_the_data_populated_in_the_spreadsheet(self, p2 = "p2"):
        pass

    def he_does_not_see_under_unit_title_any_info_about_instructional_periods_and_ap_exam_weighting(self):
        pass

    def sees_join_code_and_action_columns(self):
        pass

    def join_code_is_populated_with_a_7_alphanumerical_code(self):
        pass

    def clicks_on_a_unit_tab_from_units_section_of_the_homepage(self):
        pass

    def clicks_on_join_code_for_a_section(self):
        pass

    def a_popup_appears_with_details_about_the_section(self):
        pass

    def a_link_to_students_register_page(self):
        pass

    def the_message(self, free_text = ""):
        pass

    def there_are_opened_unlocked_assignments_where_one_or_more_students_have_started_but_not_submitted_the_assignment(self):
        pass

    def there_are_opened_unlocked_assignments_where_one_or_more_students_have_completedsubmitted_the_assignment(self):
        pass

    def the_teacher_sees_in_the_popup_a_dark_blue_check_mark_indicating_submitted_with_the_number_of_students_who_have_submitted_the_assessment(self):
        pass

    def there_are_open_unlocked_assignments_where_one_or_more_students_have_completedsubmitted_the_assessment(self):
        pass

    def a_teacher_is_on_the_question_bank_progress_tab(self):
        pass

    def the_text_is_gray(self):
        pass

    def the_text_color_is_gray(self):
        pass

    def in_one_of_the_pretest_courses_pre_ap_algebra_biology_english_world_history(self):
        pass

    def the_teacher_should_see_a_bannerlink_to_the_preap_final_exam(self):
        pass

    def not_in_a_pretest_cohort_school(self):
        pass

    def the_teacher_should_not_see_a_bannerlink_to_the_preap_final_exam(self):
        pass

    def not_in_one_of_the_pretest_courses_pre_ap_algebra_biology_english_world_history(self):
        pass

    def the_teacher_click_on_the_bannerlink_to_preap_final_exam(self):
        pass

    def he_is_redirected_to_preap_f_inal_exam_listing_page(self):
        pass

    def he_should_see_the_list_of_sections_from_apc(self):
        pass

    def the_feature_flag_is_turned_off_from_splitio(self):
        pass

    def select_any_instructional_periods(self):
        pass

    def saves_the_section(self):
        pass

    def the_instructional_periods_checkboxes_will_be_saved_successfully(self):
        pass

    def selects_any_other_prea_ap_subject_than_whg_subject(self):
        pass

    def the_instructional_periods_checkboxes_will_not_be_displayed(self):
        pass

    def presses_on_assign_button(self):
        pass

    def assign_final_exam_popup_is_displayed(self):
        pass

    def contains_info_about_exam_and_section(self):
        pass

    def the_info_is_not_editable(self):
        pass

    def the_teacher_can_select_duration_of_exam(self):
        pass

    def it_has_two_options_one_60_and_two_30(self):
        pass

    def the_teacher_can_select_date_of_exam_from_calendar_dropdown(self):
        pass

    def calendar_availability_is_limited_to_may_1_2019_through_june_14_2019(self):
        pass

    def he_fills_in_duration_and_date(self):
        pass

    def the_exam_is_assigned_successfully(self):
        pass

    def a_teacher_on_the_assign_final_exam_popup(self):
        pass

    def the_assign_button_changes_to_begin_exam(self):
        pass

    def an_edit_button_is_available_next_tot_the_begin_one(self):
        pass

    def presses_on_cancel_button(self):
        pass

    def the_exam_is_not_assigned(self):
        pass

    def there_is_an_assigned_exam(self):
        pass

    def he_presses_on_edit_button(self):
        pass

    def the_assign_exam_popup_appears(self):
        pass

    def the_teacher_is_able_to_modify_date_and_duration(self):
        pass

    def he_presses_on_begin_exam_button(self):
        pass

    def the_exam_is_opened_to_students(self):
        pass

    def the_exam_date_column_is_showing_the_set_start_date(self):
        pass

    def the_exam_date_column_is_showing_a_(self):
        pass

    def exam_date_is_greater_than_current_date(self):
        pass

    def begin_exam_is_inactive(self):
        pass

    def a_student_on_the_preap_final_exam_app(self):
        pass

    def sees_the_list_of_sections_that_he_joined_split_per_each_subject(self):
        pass

    def a_student_on_the_my_exams_page_preap_final(self):
        pass

    def the_exam_was_not_started_by_the_teacher(self):
        pass

    def the_student_will_see_an_information_message(self, free_text = ""):
        pass

    def the_begin_button_will_be_inactive(self):
        pass

    def the_exam_is_split_into_2_sessions(self):
        pass

    def a_question_from_a_quiz_was_marked_with_calculator_section_tag__p1_in_the_metadata_spreadsheet(self, p1 = "p1"):
        pass

    def a_teacher_opens_the_preview_of_the_above_quiz_from_p2_page(self, p2 = "p2"):
        pass

    def navigates_to_that_question(self):
        pass

    def he_p3_the_calculator_icon_between_the_question_number_and_the_bookmark_icon(self, p3 = "p3"):
        pass

    def a_p4_opens_the_preview_of_the_above_quiz_from_p2_page(self, p2 = "p2", p4 = "p4"):
        pass

    def a_student_opens_the_preview_of_the_above_quiz_from_p2_page(self, p2 = "p2"):
        pass

    def it_contains_overview_tab_which_displays_the_content_of_each_question(self):
        pass

    def an_ap_teacher_on_the_preview_form_of_a_quiz(self):
        pass

    def he_clicks_on_the_p1_arrow_from_the_question_navigation_bar(self, p1 = ""):
        pass

    def he_clicks_on_the_p1_arrow_from_the_bottom_of_the_screen(self, p1 = ""):
        pass

    def an_ap_teacher_on_the_accessibility_page_of_the_preview_form_of_a_quiz(self):
        pass

    def the_user_is_returned_to_the_preview_where_he_sees_the_text_of_the_questions_zoomed_out_to_p2_size(self, p2 = "p2"):
        pass

    def an_ap_teacher_viewing_a_question_with_multiple_passages_from_a_quiz_preview(self):
        pass

    def a_teacher_on_p1_page_opened_on_p4_browser(self, p1 = "", p4 = "p4"):
        pass

    def the_new_version_of_preview_opens_similar_to_the_student_final_exam_player(self):
        pass

    def he_clicks_on_click(self, p1 = "", free_text = "", datatable = "||"):
        pass

    def a_teacher_on_a_pre_ap_subject_p1_page(self, p1 = ""):
        pass

    def the_old_version_of_preview_is_displayed(self):
        pass

    def a_teacher_on_the_preview_form_of_an_ap_quiz(self):
        pass

    def he_inspects_the_upper_side_of_the_preview_mode(self):
        pass

    def he_sees_the_correct_quiz_title_to_the_right_side_of_the_logo_subject_name__quiz_title(self):
        pass

    def a_teacher_on_the_preview_mode_of_an_ap_quiz(self):
        pass

    def a_teacher_on_a_question_from_preview_mode_of_an_ap_quiz(self):
        pass

    def a_teacher_on_the_preview_mode_of_a_p1_quiz(self, p1 = "p1"):
        pass

    def he_inspects_the_toolkit_panel_on_the_right_side_of_the_screen(self):
        pass

    def he_does_not_any_submit_button(self):
        pass

    def he_refreshes_the_page(self):
        pass

    def the_quiz_contains_at_least_one_question_with_multiple_passages(self):
        pass

    def a_teacher_on_a_question_with_multiple_passages_from_the_preview_mode_of_an_ap_quiz(self):
        pass

    def a_teacher_on_the_help_page_of_the_preview_mode_of_an_ap_quiz(self):
        pass

    def a_teache_on_the_accessibility_page_of_the_preview_mode_of_an_ap_quiz(self):
        pass

    def a_teacher_on_the_accessibility_page_of_the_preview_mode_of_an_ap_quiz(self):
        pass

    def a_teacher_on_a_question_of_the_preview_mode_of_an_ap_quiz(self):
        pass

    def a_teacher_has_a_section_in_subject(self, subject = "", datatable = "||"):
        pass

    def a_teacher_has_a_class_in_subject(self, datatable = "||"):
        pass

    def a_teacher_has_a_class_in_subject(self):
        pass

    def the_teacher_assigns_an_exam_to_that_section(self):
        pass

    def the_teacher_selects_one_60_minute_exam(self):
        pass

    def the_section_is_assigned_one_60_minute_exam(self):
        pass

    def that_exam_is_for_the_subject_subject(self, subject = "subject"):
        pass

    def the_section_is_assigned_two_30_minute_exams(self):
        pass

    def the_teacher_selects_two_30_minute_exams(self):
        pass

    def that(self):
        pass

    def that_exam_is_randomly_selected_from_the_pool_of_available_exams_for_that_subject(self):
        pass

    def a_teacher_has_a_section_in_p1(self, p1 = ""):
        pass

    def a_teacher_has_a_section_in_subject(self, subject = "", datatable = "||"):
        pass

    def the_teacher_does_not_select_a_time_value_for_that_exam(self):
        pass

    def the_teacher_will_be_unable_to_assign_the_exam(self):
        pass

    def the_teacher_tries_to_assign_an_exam_to_that_section(self):
        pass

    def there_are_multiple_students_in_that_section(self):
        pass

    def all_students_in_that_section_have_the_same_exam_assigned_to_them(self):
        pass

    def a_student_in_a_section_for_p1(self, p1 = ""):
        pass

    def that_student_clicks_begin_exam(self, p1 = ""):
        pass

    def the_student_is_taken_to_the_final_exam_player(self):
        pass

    def the_exam_matches_the_subject_p1(self, p1 = ""):
        pass

    def the_student_clicks_begin_exam(self):
        pass

    def a_student_is_in_a_section_in_subject(self, subject = "", datatable = "||"):
        pass

    def that_student_has_been_assigned_two_30_minute_exams(self):
        pass

    def the_student_launches_one_of_the_exams(self):
        pass

    def the_exam_launches_in_the_final_exam_player(self):
        pass

    def the_student_has_30_minutes_to_complete_the_exam(self):
        pass

    def that_student_has_been_assigned_a_60_minute_exam(self):
        pass

    def the_student_launches_that_exam(self):
        pass

    def the_student_has_60_minutes_to_complete_the_exam(self):
        pass

    def the_user_is_returned_to_the_preview_where_he_sees_the_p2_change(self, p2 = "p2"):
        pass

    def the_preview_should_zooms_p2_with_one_level(self, p2 = "p2"):
        pass

    def the_preview_contains_a_question_with_a_number_of_passages_so_that_there_is_p1(self, p1 = "p1"):
        pass

    def he_clicks_on_a_question_number_from_the_question_navigation_bar(self):
        pass

    def he_is_returned_to_the_preview_where_he_sees_the_text_of_the_questions_in_p3_color_on_p2_background(self, p3 = "", p2 = ""):
        pass

    def the_preview_contains_a_question_with_multiple_passages(self):
        pass

    def he_is_taken_to_homepage_where_he_sees_only_the_homepage_url_without_the_unit_parameter_displayed(self):
        pass

    def teacher_is_on_the_qb_page_results_table(self):
        pass

    def he_sees_no_zoom_tool_available(self):
        pass

    def he_sees_the_icon_in_front_of_the_subunit_that_was_configured_in_the_metadata_spreadsheet(self):
        pass

    def a_configurable_subunit_header_is_displayed_p2(self, p2 = "p2"):
        pass

    def a_teacher_that_has_this_subject_logs_in(self):
        pass

    def inspects_units_section_from_the_homepage_of_the_pre_ap_subject(self):
        pass

    def inspects_units_section_from_the_homepage_of_that_ap_subject(self):
        pass

    def that_unit_contains_assessments_that_were_assigned_to_existing_classes(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject__on_a_unit_tab(self):
        pass

    def a_teacher_on_the_homepage_of_a_page__on_a_unit_tab(self):
        pass

    def a_question_from_a_quiz_was_marked_with_calculator_section_tag__p1_in_the_create_tab_of_question_bank_page(self, p1 = "p1"):
        pass

    def a_teacher_on_the_preview_of_an_assignment(self, p1 = ""):
        pass

    def a_p1_on_the_preview_of_a_quiz(self, p1 = "p1"):
        pass

    def he_clicks_on_the_calculator_icon(self):
        pass

    def the_calculator_allowed_popover_is_displayed(self):
        pass

    def he_navigates_to_a_question_marked_with_the_calculator_icon(self):
        pass

    def a_teacher_on_the_preview_of_a_quiz(self):
        pass

    def he_clicks_on_the_calculator_icon_from_a_calculator_allowed_question(self):
        pass

    def afterwards_clicks_p1(self, p1 = "p1"):
        pass

    def the_calculator_allowed_popup_is_dismissed(self):
        pass

    def a_teacher_on_the_preview_mode_of_a_p1_assessment(self, p1 = "p1"):
        pass

    def selects_a_class_and_assigns_it(self):
        pass

    def the_assessment_is_assigned_successfully(self):
        pass

    def the_students_from_that_class_can_start_working_on_it(self):
        pass

    def a_teacher_on_a_question_from_preview_page_of_a_quiz_opened_in_progress_tab(self):
        pass

    def a_teacher_on_the_preview_page_of_a_p1_quiz_opened_in_progress_tab(self, p1 = "p1"):
        pass

    def a_teacher_on_the_preview_page_of_a_quiz_opened_in_progress_tab(self):
        pass

    def a_teacher_on_a_question_with_multiple_passages_from_the_preview_page_of_a_quiz_opened_in_progress_tab(self):
        pass

    def a_teacher_on_the_accessibility_page_of_the_preview_page_of_a_quiz_opened_in_progress_tab(self):
        pass

    def he_clicks_on_the_quiz_title(self):
        pass

    def a_teacher_on_a_question_from_preview_page_of_a_quiz_opened_in_results_tab(self):
        pass

    def a_teacher_on_the_preview_page_of_a_p1_quiz_opened_from_results_tab(self, p1 = "p1"):
        pass

    def a_teacher_on_the_preview_page_of_a_quiz_opened_in_results_tab(self):
        pass

    def a_teacher_on_a_question_with_multiple_passages_from_the_preview_page_of_a_quiz_opened_in_results_tab(self):
        pass

    def a_teacher_on_the_accessibility_page_of_the_preview_page_of_a_quiz_opened_in_results_tab(self):
        pass

    def a_teacher_on_p1_page_of_a_quiz_opened_on_p4_browser(self, p1 = "", p4 = "p4"):
        pass

    def he_p1_from_a_calculator_allowed_question(self, p1 = "p1"):
        pass

    def a_teacher_using_screen_reader_on_the_preview_of_a_quiz(self):
        pass

    def the_screen_reader_sees_the_calculator_allowed_button(self):
        pass

    def the_calculator_allowed_element_is_highlighted(self):
        pass

    def he_sees_the_toolkit_panel_displayed_as_a_white_vertical_box_with_following_icons_in_this_order_p2(self, p2 = "p2"):
        pass

    def he_looks_at_the_student_performance_bar(self):
        pass

    def the_teacher_opens_a_specific_assessment(self):
        pass

    def teacher_sees_performance_bars_showing_number_of_students_that_have_submitted_the_assessment(self):
        pass

    def the_numbers_are_split_according_to_the_results(self):
        pass

    def the_soft_time_limit_was_reached(self):
        pass

    def a_student_on_the_submit_outside_of_time_limit_of_final_exam_player(self):
        pass

    def a_student_on_a_p1(self, p1 = "p1"):
        pass

    def he_answers_p3_the_questions_of_the_quiz(self, p3 = "p3"):
        pass

    def clicks_on_submit(self):
        pass

    def he_is_redirected_from_the_quiz_player_back_to_assignments_tab_of_assessments_page(self):
        pass

    def a_student_on_the_exit_page_of_a_quiz(self):
        pass

    def he_inspects_it(self):
        pass

    def a_student_on_the_exit_popup_of_a_quiz_p1(self, p1 = "p1"):
        pass

    def he_sees_exit_title__p2_text__exit_button(self, p2 = "p2"):
        pass

    def a_student_on_the_exit_popup_of_a_p1(self, p1 = "p1"):
        pass

    def he_clicks_on_exit_button(self):
        pass

    def he_clicks_onp3_unanswered_questions(self, p3 = "p3"):
        pass

    def a_student_submits_a_quiz_p1_time_limit_leaving_p2_unanswered_questions(self, p1 = "p1", p2 = "p2"):
        pass

    def the_student_clicks_on_p3_button_from_the_submit_popup(self, p3 = "p3"):
        pass

    def the_student_is_taken_p4(self, p4 = "p4"):
        pass

    def a_student_leaves_p1_unanswered_on_a_quiz_p3(self, p1 = "p1", p3 = "p3"):
        pass

    def the_student_clicks_on_submit_button(self):
        pass

    def he_sees_in_the_submit_popup_the_unanswered_section_with_the_info_text__p2_(self, p2 = ""):
        pass

    def a_student_on_a_quiz_with_p5_time_limit_containing_p1_unanswered_questions(self, p1 = "p1", p5 = "p5"):
        pass

    def the_time_elapsed_hits_the_total_time_allotted(self):
        pass

    def the_p2_popup_appears_on_the_screen_containing_the_following_elements_p5(self, p2 = "p2", p5 = "p5"):
        pass

    def a_student_on_a_quiz_with_soft_time_limit_containing_p1_unanswered_questions(self, p1 = "p1"):
        pass

    def a_student_on_a_soft_timed_limit_quiz_containing_p1_unanswered_questions(self, p1 = ""):
        pass

    def the_student_clicks_on_submit_now_button_from_the_soft_time_limit_reached_popup(self):
        pass

    def he_is_taken_to_the_submit_confirmation_popup_containing_submit_titlep2__info_text_are_you_sure_you_want_to_submit_your_assessment__no_yes_buttons(self, p2 = "p2"):
        pass

    def the_student_clicks_on_submit_now_button_and_then_on_yes_button_from_the_confirmation_popup(self):
        pass

    def he_is_taken_to_the_exit_popup(self):
        pass

    def the_student_clicks_on_submit_now_button_and_then_on_no_button_from_the_confirmation_popup(self):
        pass

    def he_is_taken_back_to_the_quiz_player(self):
        pass

    def the_student_clicks_on_submit_now_button_and_then_on_an_unanswered_question_link_from_the_confirmation_popup(self):
        pass

    def he_is_taken_back_to_the_quiz_player_to_that_specific_unanswered_question(self):
        pass

    def the_student_clicks_on_continue_button_from_the_soft_time_limit_reached_popup(self):
        pass

    def he_is_taken_back_to_the_quiz_player_where_he_can_continue_working_on_his_answers(self):
        pass

    def he_is_taken_back_to_the_quiz_player_where_he_sees_the_timer_disabled_and_set_to_0000(self):
        pass

    def a_student_on_a_soft_timed_limit_quiz_where_he_has_already_opened_p1_menu(self, p1 = ""):
        pass

    def the_soft_time_limit_reached_popup_is_displayed_over_the_p1_menu(self, p1 = "p1"):
        pass

    def a_teacher_first_opening_the_preview_of_a_p1_page(self, p1 = ""):
        pass

    def he_sees_the_performance_bar(self):
        pass

    def he_sees_a_performance_bar_with_light_gray_and_the_total_number_of_students_of_the_class_displayed_in_white(self):
        pass

    def we_have_a_mcq_only_assignment_where_no_student_submitted(self):
        pass

    def he_inspect_the_right_side_of_the_preview_page(self):
        pass

    def he_sees_under_the_toolkit_panel_a_collapsed_side_tab_that_reads_question_details_with_the_arrow_(self):
        pass

    def a_coord__admin_on_the_preview_of_a_p1(self, p1 = ""):
        pass

    def a_student_on_the_assessments_page__assign_tab(self):
        pass

    def he_opens_a_quiz_to_work_on_it(self):
        pass

    def he_does_not_see_inside_the_quiz_player_a_tab_named_question_details(self):
        pass

    def he_sees_under_the_toolkit_panel_a_collapsed_side_tab_that_reads_question_details__arrow_(self):
        pass

    def a_teacher_on_the_preview_page_of_a_question_inside_a_quiz_opened_on_p1(self, p1 = "p1"):
        pass

    def he_clicks_on_the_question_details_tab(self):
        pass

    def a_green_checkmark_appears_next_to_the_correct_answer(self):
        pass

    def the_slider_expands_and_displays_the_question_metadata_panel(self):
        pass

    def a_teacher_on_the_preview_page_of_a_mcq_question_inside_a_quiz(self):
        pass

    def a_green_rectangular_outline_surrounds_it(self):
        pass

    def a_teacher_on_the_preview_page_of_a_frq_question_inside_a_quiz(self):
        pass

    def the_slider_expands_and_displays_the_correct_metadata_panel_for_that_question_without_any_ui_action_on_the_question_itself(self):
        pass

    def a_teacher_first_opening_the_preview_page_of_a_quiz(self):
        pass

    def he_clicks_on_question_details_tab_for_a_p1(self, p1 = "p1"):
        pass

    def the_slider_expands_and_changes_its_name_to_hide_details__arrow_(self):
        pass

    def a_teacher_on_the_preview_page_of_a_p1_question_inside_a_quiz(self, p1 = "p1"):
        pass

    def the_slider_expands_and_displays_the_correct_metadata_panel_for_that_question_as_per_the_metadata_imported(self):
        pass

    def the_ui_elements_of_the_question_are_well_displayed_without_being_overlapped_by_the_question_details_slider(self):
        pass

    def he_navigates_through_the_questions_of_the_quiz(self):
        pass

    def the_slider_keeps_its_state_that_is_remains_p1(self, p1 = "p1"):
        pass

    def a_teacher_on_the_preview_page_of_a_question_inside_an_assessment(self):
        pass

    def a_teacher_on_the_preview_page_of_a_quiz(self):
        pass

    def the_question_details_slider_is_in_expanded_state(self):
        pass

    def the_teacher_changes_p1(self, p1 = "p1"):
        pass

    def the_slider_is_not_impacted_by_these_ui_changes(self):
        pass

    def a_teacher_on_the_preview_page_of_a_question_from_qb__create_tab(self):
        pass

    def he_clicks_on_next_previous_buttons_to_navigate_through_the_independent_questions_from_create_tab(self):
        pass

    def the_question_details_slider_keeps_its_state_that_is_remains_p1(self, p1 = "p1"):
        pass

    def the_question_details_slider_of_that_question_is_expanded(self):
        pass

    def opens_the_preview_of_p1_assessment(self, p1 = "p1"):
        pass

    def the_teacher_closes_the_preview_page_of_that_assessment(self):
        pass

    def the_question_details_slider_is_collapsed(self):
        pass

    def the_question_details_slider_is_in_expanded_state_for_a_specific_question(self):
        pass

    def the_teacher_clicks_on_the_hide_details_tab(self):
        pass

    def the_slider_reverts_to_the_collapsed_state_ie_the_slider_collapses_and_hides_its_informations(self):
        pass

    def a_teacher_on_the_preview_page_of_a_question_with_multiple_passages_tabs(self):
        pass

    def the_question_details_slider_is_in_state_for_a_specific_question(self):
        pass

    def the_teacher_clicks_on_collapse_expand_button_to_reveal_hide_the_content_of_the_question(self):
        pass

    def the_question_details_slider_remains_opened_and_is_not_impacted_by_change(self):
        pass

    def the_tab_changes_its_name_back_to_question_details_arrow__(self):
        pass

    def the_slider_reverts_to_the_collapsed_state(self):
        pass

    def the_indication_for_the_correct_answer_the_green_check_mark_and_the_highlighted_outline_disappears(self):
        pass

    def the_question_details_slider_is_in_p1_state_for_a_specific_question(self, p1 = "p1"):
        pass

    def the_question_details_slider_is_in_cond_state_for_a_specific_question(self, p1 = "p1"):
        pass

    def inspecting_its_accessibility_setting_of_the_p1_tab(self, p1 = "p1"):
        pass

    def the_element_is_structured_with_button_use_ariarolebutton_to_ensure_the_role_of_button_is_rendered_to_screen_reader(self, button = "button"):
        pass

    def the_question_details_tab_was_expanded_for_a_specific_question(self):
        pass

    def the_teacher_clicks_on_p1for_a_metadata_parent_category(self, p1 = "p1"):
        pass

    def that_p2(self, p2 = "p2"):
        pass

    def a_teacher_on_the_preview_page_a_quiz(self):
        pass

    def the_button_switches_to_p3(self, p3 = ""):
        pass

    def the_question_details_slider_p2(self, p2 = "p1"):
        pass

    def the_teacher_clicks_on_tab_from_the_keyboard_multiple_times(self):
        pass

    def some_of_the_metadata_parent_categories_of_the_question_are_expanded_and_some_are_collapsed(self):
        pass

    def screen_reader_sees_the_actionable_p1(self, p1 = "p1"):
        pass

    def a_metadata_parent_category_was_expanded_as_well(self):
        pass

    def the_teacher_collapses_the_question_details_panel(self):
        pass

    def reexpands_it_back_again(self):
        pass

    def the_above_metadata_parent_category_is_collapsed(self):
        pass

    def the_question_details_tab_and_a_metadata_parent_category_inside_it_were_expanded_for_a_specific_question(self):
        pass

    def the_teacher_clicks_multiple_times_on_tab_from_the_keyboard(self):
        pass

    def a_visual_focus_appears_on_p1(self, p1 = "p1"):
        pass

    def the_question_details_tab_is_already_expanded_for_a_specific_question(self):
        pass

    def the_unit_details_are_in_reading_order_positioned_inline_after_the_hide_details_element(self):
        pass

    def the_teacher_clicks_on_tab_from_the_keyboard_multiple_times_in_order_to_reach_the_unit_details_of_that_question(self):
        pass

    def the_question_details_tab_is_already_expanded_for_a_specific_mcq(self):
        pass

    def the_teacher_clicks_on_tab_from_the_keyboard_multiple_times_in_order_to_reach_the_correct_answer(self):
        pass

    def the_screen_reader_says_the_correct_answer_is_x_via_aria_alert__polite_or_aria_live_region(self):
        pass

    def he_inspects_the_right_side_of_the_preview_page(self):
        pass

    def a_teacher_in_the_progress_view_of_a_quiz_containing_p1_questions_from_p2_page(self, p2 = "", p1 = "p1"):
        pass

    def there_is_a_student_that_has_not_started_yet_working_on_that_quiz(self):
        pass

    def the_teacher_inspects_the_status_column_for_that_specific_student(self):
        pass

    def he_sees_the_status_set_to_not_started(self):
        pass

    def there_is_a_student_that_has_opened_an_assignment_but_has_not_yet_submitted_it(self):
        pass

    def he_sees_the_status_set_to_in_progress(self):
        pass

    def a_teacher_in_the_progress_view_of_a_quiz_containing_only_mcq_questions(self):
        pass

    def there_is_a_student_that_has_submitted_the_assignment_but_the_autoscoring_is_not_yet_completed(self):
        pass

    def he_sees_the_status_set_to_submitted(self):
        pass

    def a_teacher_in_the_progress_view_of_a_quiz_containing_p1_questions(self, p1 = "p1"):
        pass

    def there_is_a_student_that_has_submitted_the_quiz(self):
        pass

    def the_assignment_was_not_yet_scored_by_anyone_not_the_teacher_nor_the_student(self):
        pass

    def p2_has_started_scoring_it_but_has_not_yet_finished(self, p2 = "p2"):
        pass

    def he_sees_the_status_set_to_score_started(self):
        pass

    def he_sees_the_status_set_to_scored(self):
        pass

    def p2_has_finished_scoring_it(self, p2 = "p2"):
        pass

    def a_teacher_on_the_units_dashboard_of_a_subject_homepage(self):
        pass

    def there_p2_linked_to_a_subunit(self, p2 = "p2"):
        pass

    def he_clicks_on_p3_skill_abbreviation_chip(self, p3 = "p3"):
        pass

    def a_popover_opens_showing_title_subtitle__full_text_description_for_that_skill__x_button_p4(self, p4 = "p4"):
        pass

    def there_is_a_student_that_has_submitted_the_assignment_and_autoscoring_is_complete(self):
        pass

    def he_sees_the_status_set_to_complete(self):
        pass

    def a_teacher_in_the_progress_view_of_a_quiz_containing_also_frq_questions(self):
        pass

    def there_is_a_student_that_has_p1(self, p1 = "p1"):
        pass

    def a_teacher_in_the_progress_view_of_a_quiz(self):
        pass

    def he_tries_to_navigate_using_tab_from_the_keyboard_to_the_status_element_of_each_student(self):
        pass

    def he_sees_the_status_element_is_not_actionable_and_has_no_visual_focus(self):
        pass

    def he_hears_the_screen_reader_rendering_that_specific_status_value(self):
        pass

    def he_clicks_on__p1__status_for_a_student(self, p1 = "p1"):
        pass

    def a_teacher_in_the_progress_view_of_a_quiz_containing_p1_status_for_a_number_of_students(self, p1 = "p1"):
        pass

    def the_teacher_inspects_the_progress_scoring_bar_displayed_at_the_top_of_the_table(self):
        pass

    def he_sees_the_specific_status_the_same_number_of_students(self):
        pass

    def a_teacher_in_the_progress_view_of_a_mcq_only_quiz_containing_submitted_status_for_x_individual_students(self):
        pass

    def complete_status_for_y_individual_students(self):
        pass

    def he_sees_that_in_there_xy_number_of_students_with_the_status_complete(self):
        pass

    def a_teacher_in_the_progress_view_of_a_frq_quiz_containing_submitted_status_for_x_individual_students(self):
        pass

    def score_started_status_for_y_individual_students(self):
        pass

    def he_sees_that_in_there_xy_number_of_students_with_the_status_available_to_score(self):
        pass

    def a_student_from_that_class_starts_working_on_the_above_quiz_without_submitting_it(self):
        pass

    def the_teacher_sees_in_the_progress_scoring_bar_the_number_of_in_progress_students_increases_with_one_unit(self):
        pass

    def in_the_progress_scoring_bar_the_number_of_in_progress_students_increases_with_one_unit(self):
        pass

    def a_teacher_in_the_progress_view_of_a_mcq_only_quiz(self):
        pass

    def a_student_from_that_class_submits_the_above_quiz_but_the_autoscoring_is_not_yet_complete(self):
        pass

    def the_teacher_sees_in_the_progress_scoring_bar_the_number_of_available_to_score_students_increases_with_one_unit(self):
        pass

    def in_the_progress_scoring_bar_the_number_of_complete_students_increases_with_one_unit(self):
        pass

    def a_student_from_that_class_submits_the_above_quiz_without_any_scoring_action(self):
        pass

    def the_teacher_sees_complete_as_individual_status_for_that_student(self):
        pass

    def a_teacher_in_the_progress_view_of_a_frq_quiz(self):
        pass

    def a_student_from_that_class_submits_the_above_quiz_and_autoscoring_is_complete(self):
        pass

    def in_the_progress_scoring_bar_the_number_of_available_to_score_students_increases_with_one_unit(self):
        pass

    def the_teacher_finished_scoring_the_quiz_for_that_specific_student(self):
        pass

    def the_teacher_inspects_the_status_column_for_that_student(self):
        pass

    def the_teacher_has_started_scoring_it_but_has_not_yet_finished(self):
        pass

    def the_teacher_sees_in_the_progress_scoring_bar_the_number_of_complete_students_increases_with_one_unit(self):
        pass

    def a_student_from_that_class_submits_the_above_quiz(self):
        pass

    def the_teacher_has_started_scoring_it_without_finishing_yet_the_scoring_action(self):
        pass

    def the_teacher_scores_it(self):
        pass

    def a_student_from_a_class_submits_a_frq_quiz(self):
        pass

    def the_teacher_goes_to_the_progress_view_of_that_quiz(self):
        pass

    def he_sees_in_the_progress_scoring_bar_the_number_of_complete_students_increases_with_one_unit(self):
        pass

    def a_metadata_import_was_done_for_p1_subject_on_operational(self, p1 = ""):
        pass

    def a_teacher_enrolled_in_that_subject_logs_in(self):
        pass

    def he_is_taken_to_the_subject_homepage_where_he_sees_unit_assessment_progress_check_tab_added(self):
        pass

    def a_teacher_enrolled_in_that_subject_logs_into_p2(self):
        pass

    def he_does_not_see_any_unit_outline_info_on_the_homepage_nor_any_new_ua_tab(self):
        pass

    def a_p1_teacher_on_the_login_page_from_operational(self, p1 = ""):
        pass

    def he_logs_in_to_the_apc(self):
        pass

    def he_is_taken_to_the_subject_homepage_where_he_does_not_see_any_unit_outline_info(self):
        pass

    def he_is_taken_to_the_subject_homepage_where_he_sees_the_correct_metadata_imported_in_the_units_dashboard(self):
        pass

    def a_teacher_enrolled_in_that_subject_logs_in(self):
        pass

    def a_ppc_was_imported_for_fym_p1_library(self, p1 = ""):
        pass

    def a_teacher_enrolled_in_that_subject_goes_to_ua_progress_check_tab(self):
        pass

    def he_sees_all_the_relevant_content_of_the_ppc_as_it_was_imported_from_the_package(self):
        pass

    def some_ets_packages_were_imported_for_p1_subject_on_operational(self, p1 = ""):
        pass

    def a_metadata_import_ets_import_was_done_for_p1_subject_on_operational(self, p1 = ""):
        pass

    def a_teacher_enrolled_in_the_above_subject_logs_in(self):
        pass

    def a_metadata_import_is_done_with_configured_practice_questions_for_a_subject_that_has_units_and_qb_tab(self):
        pass

    def navigates_to_that_subject_homepage(self):
        pass

    def he_sees_in_the_resource_column_a_new_resource_displayed_as_the_last_one_for_its_topic_containing_a_specific_icon__practice_questions_hyperlinked_label(self):
        pass

    def he_sees_in_the_resource_column_one_practice_questions_linked_per_topic_which_matches_what_was_configured_in_the_spreadsheet(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_containing_practice_questions_links_in_the_units_dashboard(self):
        pass

    def the_teacher_clicks_on_a_practice_question_link(self):
        pass

    def he_is_redirect_to_qb__create_tab_having_the_filters_set_to_unit_topic__skill_source(self):
        pass

    def a_p4_on_p1_page_of_a_p2_quiz_opened_in_p5(self, p1 = "", p2 = "p2", p4 = "p4", p5 = "p5"):
        pass

    def the_user_inspects_the_page(self):
        pass

    def he_sees_the_following_horizontally_oriented_tabs_p3(self, p3 = "p3"):
        pass

    def a_p4_first_opening_p1_page_of_a_p2_quiz(self, p1 = "", p2 = "p2", p4 = "p4"):
        pass

    def he_sees_p3_tab_opened_by_default(self, p3 = "p3"):
        pass

    def a_p4_on_the_p1_page_of_a_p2_quiz(self, p1 = "", p2 = "p2", p4 = "p4"):
        pass

    def he_sees_under_the_tabs_ribbon_the_class_the_quiz_was_assigned_to(self):
        pass

    def a_metadata_spreadsheet_was_imported_for_a_specific_subject(self):
        pass

    def the_following_configuration_was_done_in_the_file_p1(self, p1 = "p1"):
        pass

    def a_teacher_enrolled_in_that_subject_navigates_to_progress_check__results_page_for_a_mcq_quiz(self):
        pass

    def he_sees_p2_as_name_of_the_first_tab(self, p2 = "p2"):
        pass

    def in_the_course_outline_tab_a_column_was_added_curriculum_check_tab_label_having_a_specific_value(self):
        pass

    def he_sees_the_curriculum_check_tab_label_value_as_name_of_the_first_tab(self):
        pass

    def he_sees_in_the_top_right_corner_on_the_ribbon_bar_near_the_timer_element_an_x_button_displayed_in_gray(self):
        pass

    def a_student_in_the_player_view_of_a_quiz(self):
        pass

    def he_hovers_over_the_x_button_from_the_top_right_corner(self):
        pass

    def a_tool_tip_message_is_displayed_save_and_exit(self):
        pass

    def then_clicks_somewhere_else_in_the_screen(self):
        pass

    def the_tool_tip_message_for_the_x_button_disappears(self):
        pass

    def there_is_no_metadata_tag_added_in_the_topics_and_skills_column(self):
        pass

    def he_sees_topics_and_skills_tab_displayed_without_any_ui_issues_even_though_there_is_no_content_in_it(self):
        pass

    def he_clicks_on_p3_tab_and_inspects_its_url(self, p3 = "p3"):
        pass

    def he_sees_as_the_page_url_p5(self, p5 = "p5"):
        pass

    def an_ap_teacher_on_progress_check_results_page_of_an_mcq_only_quiz(self):
        pass

    def the_teacher_clicks_on_topics_and_skills_tab(self):
        pass

    def the_user_clicks_on_p4(self, p4 = "p4"):
        pass

    def he_sees_a_topics_and_skills_table_with_3_columns_topic_skill_parts(self):
        pass

    def he_sees_that_the_first_column_of_the_topics_and_skills_table_has_the_name_of_the_subunits_label_field_from_the_course_outline_tab_of_configuration_sheet(self):
        pass

    def an_ap_teacher_on_progress_check_results_page_of_an_mcq_only_quiz_opened_in_p1(self, p1 = "p1"):
        pass

    def a_teacher_on_the_progress_check__results_page(self):
        pass

    def he_clicks_on_an_mcq_only_quiz(self):
        pass

    def he_sees_topics_and_skills_questions_and_students_tabs_matching_the_comps_when_it_comes_to_color__highlight_behavior_httpsprojectsinvisionappcomdmainconsole15264970348294235preview(self):
        pass

    def he_sees_topics_and_skills_table_matching_the_comps_when_it_comes_to_color__highlight_behavior_httpsprojectsinvisionappcomdmainconsole15264970344073880preview(self):
        pass

    def a_teacher_on_the_progress_check__results_page_for_an_ap_mcq_only_quiz(self):
        pass

    def he_clicks_on_the_topics_and_skills_tab(self):
        pass

    def he_sees_that_the_second_column_of_the_topics_and_skills_table_has_the_name_of_the_widget_tag_column_label_from_the_course_outline_tab_of_configuration_sheet(self):
        pass

    def he_sees_the_table_rows_are_alternating_gray_and_white_starting_with_gray(self):
        pass

    def he_sees_that_the_third_column_of_the_topics_and_skills_table_has_the_name_class_avg_average_points_earnedpossible(self):
        pass

    def a_teacher_on_progress_check_results_page_of_mcq_quiz(self):
        pass

    def the_teacher_clicks_on_an_mcq_only_quiz__topics_and_skills_tab(self):
        pass

    def short_nameblank_in_the_resources_tab_of_the_metadata_spreadsheet_imported_for_this_quiz(self):
        pass

    def that_quiz_is_part_b_of_the_multiple_pp_cs_of_a_unit(self):
        pass

    def he_sees_inside_the_table_the_column_specific_for_part_b_having_as_name_part_b_average_points_earnedpossible(self):
        pass

    def a_teacher_opens_for_that_subject__progress_check_page__results_tab_of_an_mcq_only_quiz(self):
        pass

    def a_teacher_opens_that_subjects_progress_check_page__results_tab__mcq_only_quiz__topics_and_skills_subtab(self):
        pass

    def he_sees_the_first_column_of_the_table_populated_with_the_values_taken_from_the_display_name_column_subunits_tab_of_the_imported_file(self):
        pass

    def he_sees_the_second_column_of_the_table_populated_with_values_taken_from_the_sub_skill_1_n_column_subunits_tab_of_the_spreadsheet_file(self):
        pass

    def he_sees_a_separate_entry_in_the_list_for_each_topic__skill_mapping(self):
        pass

    def a_metadata_spreadsheet_was_imported_for_a_specific_subject_having_longer_values_setup_in_display_name__sub_skill_1_n_columns_from_subunit_tab(self):
        pass

    def he_sees_the_longer_values_properly_displayed_in_the_topics_and_skills_table(self):
        pass

    def he_sees_the_table_properly_displayed_without_any_ui_issues_having_the_style_indicated_in_the_mockups(self):
        pass

    def we_have_a_mcq_only_assignment_where_all_students_submitted(self):
        pass

    def he_looks_at_the_student_performance_bar_for_that_assignment(self):
        pass

    def we_have_a_mcq_only_assignment_where_just_one_student_didnt_submitted(self):
        pass

    def he_clicks_on_an_assignment_title__questions_subtab__click_on_a_question(self):
        pass

    def the_performance_bar_is_showing_corresponding_shade_of_yellow_green_and_gray_according_with_students_results(self):
        pass

    def he_clicks_on_an_assignment_title__questions_subtab(self):
        pass

    def he_sees_a_performance_bar_near_the_question_title(self):
        pass

    def he_looks_at_one_question_from_the_assignment(self):
        pass

    def he_clicks_on_an_assignment_title__questions_tab(self):
        pass

    def a_teacher_on_p1_page__results_tabassignment_title_questions_tab(self, p1 = "p1"):
        pass

    def the_performance_bar_is_showing_corresponding_colors_of_red_green_and_gray_according_with_students_results_incorrect_correct_no_results(self):
        pass

    def a_teacher_on_place_page__results_tab_questions(self, place = "p1"):
        pass

    def he_clicks_on_the_student_name_from_the_student_performance_popover_for_an_assignment(self):
        pass

    def he_is_redirected_to_the_individual_student_page(self):
        pass

    def a_teacher_on_p1_page__results_tab_open_an_assignment_students_tab_individual_student_page(self, p1 = "p1"):
        pass

    def he_looks_in_the_individual_student_page(self):
        pass

    def he_sees_a_performance_bar_near_the_question_title_for_each_question_of_the_assignment(self):
        pass

    def the_performance_bar_is_showing_corresponding_shade_of_yellow_green_and_gray_according_with_students_results0_to_249925_to_499950_to_749975_to_100_no_results(self):
        pass

    def the_perfor(self):
        pass

    def he_sees_that_the_performance_bar_is_spilt_in_4_tiers_dark_yellow_light_yellow_light_greendark_green(self):
        pass

    def he_navigates_with_tab_to_the_student_performance_bar(self):
        pass

    def he_sees_a_visual_focus_appears_on_the_student_performance_bar(self):
        pass

    def the_screen_reader_reads_the_score_of_the_student_x_out_y_points(self):
        pass

    def a_vertical_line_indicating_student_score_is_displayed_on_the_bar_in_the_appropriate_place_within_those_tiers(self):
        pass

    def he_sees_that_the_performance_bar_is_spilt_in_4_performance_tiers_dark_yellowlight_yellowlight_greendark_green_corresponding_to_the_ranges_0_to_249925_to_499950_to_749975_to_100(self):
        pass

    def he_looks_at_the_student_score_displayed_on_the_student_performance_bar(self):
        pass

    def he_sees_the_student_score_as_the_report_from_total_gained_points_by_the_student_from_the_entire_assignmenttotal_possible_points_that_the_student_could_gain_from_the_entire_assignment(self):
        pass

    def he_sees_that_the_performance_bar_is_spilt_in_4_equal_performance_tiers_dark_yellowlight_yellowlight_greendark_green_corresponding_to_the_ranges_0_to_249925_to_499950_to_749975_to_100(self):
        pass

    def the_width_of_each_performance_category_within_the_bar_is_determined_by_the_percent_of_students_in_the_class_who_fall_into_that_category(self):
        pass

    def he_sees_that_the_performance_bar_is_spilt_in_maximum_4_performance_categories_plus_no_results(self):
        pass

    def in_each_category_is_shown_the_correct_number_of_students(self):
        pass

    def a_teacher_assigns_a_progress_check_mcq_quiz_to_a_class(self):
        pass

    def the_teacher_navigates_to_progress_check_page__results_tab__mcq_quiz__topics_and_skills_subtab(self):
        pass

    def there_is_no_submission_from_the_students_side_yet(self):
        pass

    def he_sees_in_the_parts_column_the_skilltopic_pairings_related_to_the_questions_of_the_above_quiz_displayed_as_blank(self):
        pass

    def there_are_students_that_have_submitted_a_progress_check_mcq_quiz(self):
        pass

    def there_are_students_that_have_taken_the_quiz_and_submitted_it(self):
        pass

    def he_sees_in_the_parts_column_of_this_specific_assignment_the_average_points_earned_possible_for_the_students_that_have_submitted_the_quiz(self):
        pass

    def the_correct_score_is_displayed_next_to_the_question_11(self):
        pass

    def the_student_answered_incorrectly(self):
        pass

    def a_teacher_has_assigned_a_p1_progress_check_mcq_quiz_to_a_class(self, p1 = "p1"):
        pass

    def the_correct_score_is_displayed_next_to_the_question_01(self):
        pass

    def the_score_is_displayed_as_scored_points_total_points(self):
        pass

    def there_are_3_mcq_parts_part_a_part_b_and_part_c_linked_to_the_same_unit_for_an_ap_subject(self):
        pass

    def a_teacher_enrolled_in_that_subject_assigns_part_a_and_part_c_to_the_same_class(self):
        pass

    def he_navigates_to_progress_checks__results_page_for_that_specific_part_c_assignment_using_p1(self, p1 = "p1"):
        pass

    def he_sees_in_the_topics_and_skills_table_3_parts_columns_part_a_part_b_and_part_c(self):
        pass

    def there_is_no_column_for_part_b(self):
        pass

    def a_teacher_enrolled_in_that_subject_assigns_part_a_and_part_c_to_the_same_class_1_and_part_b_to_class_2_only_once(self):
        pass

    def he_navigates_to_progress_checks__results_page_for_the_part_b_assignment_assigned_to_class_2(self):
        pass

    def he_sees_in_the_topics_and_skills_table_just_one_part_column_part_b(self):
        pass

    def a_teacher_on_progress_check_results_page_of_an_mcq_quiz(self):
        pass

    def leaves_part_b_unassigned(self):
        pass

    def he_sees_inside_the_table_the_columns_specific_for_the_other_unselected_assignments_of_the_unit_having_the_name_part_x(self):
        pass

    def a_teacher_enrolled_in_that_subject_assigns_them_to_same_class(self):
        pass

    def the_teacher_navigates_to_progress_checks__results_page_for_part_b_assignment(self):
        pass

    def he_sees_in_the_topics_and_skills_table_in_part_a_column_the_label_unlock_for_all_the_topicskill_rows_linked_to_that_part_a_assignment(self):
        pass

    def part_a_is_locked_and_has_never_been_opened(self):
        pass

    def all_the_other_topicskill_cells_of_the_part_a_column_are_marked_with_the_lock_icon(self):
        pass

    def clicks_on_the_unlock_link_displayed_in_part_a_column(self):
        pass

    def he_is_taken_to_the_progress_page_of_the_part_a_assignment_where_he_can_unlock_the_quiz(self):
        pass

    def part_a_is_open_and_p1(self, p1 = "p1"):
        pass

    def he_sees_in_the_topics_and_skills_table_in_part_a_column_the_label_view_progress_for_all_the_topicskill_rows_linked_to_that_part_a_assignment(self):
        pass

    def the_lock_icon(self):
        pass

    def it_has_a_red_color_d0021b(self):
        pass

    def clicks_on_the_view_progress_link_displayed_in_part_a_column(self):
        pass

    def he_is_taken_to_the_progress_page_of_the_part_a_assignment(self):
        pass

    def part_a_has_submissions_scores_for_80_of_the_students_in_the_class(self):
        pass

    def he_sees_in_the_topics_and_skills_table_in_part_a_column_the_label_view_results_for_all_the_topicskill_rows_linked_to_that_part_a_assignment(self):
        pass

    def clicks_on_the_view_results_link_displayed_in_part_a_column(self):
        pass

    def he_is_taken_to_the_results_page_of_the_part_a_assignment_with_topics_and_skills_tab_on_display(self):
        pass

    def part_a_has_the_view_results_state_and_is_marked_as_p1(self, p1 = "p1"):
        pass

    def the_teacher_marks_is_at_as_complete(self):
        pass

    def he_is_taken_to_the_progress_page_of_the_part_a_assignment_where_he_can_mark_the_quiz_as_open(self):
        pass

    def part_a_has_the_view_progress_state_and_it_is_p1(self, p1 = "p1"):
        pass


    def he_deletes_the_part_a_assignment_from_progress_tab(self):
        pass

    def navigates_to_progress_checks__results_page_for_that_specific_part_c_assignment(self):
        pass

    def he_sees_part_ab_c_columns(self):
        pass

    def there_is_a_topicskill_row_that_is_not_linked_to_part_a(self):
        pass

    def part_a_is_p1(self, p1 = "p1"):
        pass

    def he_sees_in_the_topics_and_skills_table_in_part_a_column_the_above_topic_skill_cell_displayed_as_empty(self):
        pass

    def the_correct_score_is_displayed_next_to_the_green_check_mark_11_mc_point(self):
        pass

    def the_correct_score_is_displayed_next_to_the_red_x_01_mc_point(self):
        pass

    def he_sees_all_the_questions_from_that_assignment(self):
        pass

    def his_results_for_each_question(self):
        pass

    def the_student_didnt_responded_to_that_question(self):
        pass

    def teacher_is_on_a_subject_homepage(self):
        pass

    def he_sees_in_the_top_navigation_progress_dashboard_tab_being_displayed(self):
        pass

    def a_teacher_clicks_on_the_progress_dashboard_tab(self):
        pass

    def he_sees_in_each_cell_that_has_data_the_denominator_equal_to_the_number_of_questions_tagged_with_that_particular_skilltopic_pair(self):
        pass

    def that_quiz_has_x_questions_linked_to_a_particular_skilltopic_pair(self):
        pass

    def the_teacher_navigates_to_progress_check_page__results_tab__mcq_quiz__topics_and_skills_subtab__part_column_for_this_specific_quiz(self):
        pass

    def the_teacher_navigates_to_that_specific_mcq_progress_check_results_page__topics_and_skills_subtab__part_column_for_this_specific_quiz(self):
        pass

    def he_sees_in_that_particular_skilltopic_cell_the_numerator_is_the_rounded_down_average_score_of_all_students_who_submitted_results(self):
        pass

    def that_quiz_has_some_questions_linked_to_a_particular_skilltopic_pair(self):
        pass

    def the_teacher_navigates_to_that_specific_mcq_progress_checks_results_page_topics_and_skills_subtab__part_column_for_this_specific_quiz(self):
        pass

    def he_sees_that_particular_skilltopic_cell_colored_in_p2(self, p2 = "p2"):
        pass

    def for_the_questions_linked_to_a_particular_skilltopic_pair_students_have_the_average_score_numerator_divided_by_denominator_value_enclosed_in_p1(self, p1 = "p1"):
        pass

    def the_performance_bar_is_showing_corresponding_colors_of_red_yellow_green_and_gray_according_with_students_results_no_credit_partial_credit_full_credit_no_results(self):
        pass

    def the_assignment_is_a_multipart_frq(self):
        pass

    def he_sees_each_part_title_in_a_separate_row_below_the_question_title_for_each_frq(self):
        pass

    def he_sees_a_performance_bar_near_the_part_title_for_each_question_of_the_assignment(self):
        pass

    def that_the_performance_tiers_were_configured_to_specific_values_different_than_the_defaults_ones_in_the_metadata_spreadsheet_and_imported(self):
        pass

    def the_teacher_navigates_to_a_mcq_progress_checks_results_page_topics_and_skills_subtab__part_column(self):
        pass

    def he_sees_the_cell_colors_and_values_being_encapsulated_in_the_new_performance_tiers(self):
        pass

    def we_have_a_frq_only_assignment_where_just_one_student_didnt_submitted(self):
        pass

    def we_have_a_frq_only_assignment_where_all_students_submitted(self):
        pass

    def he_clicks_on_the_assignment(self):
        pass

    def he_looks_at_the_student_performance_bar_for_a_question_part_multipart_questions(self):
        pass

    def he_looks_at_the_student_performance_bar_for_the_question_part_multipart_question(self):
        pass

    def he_sees_a_performance_bar_near_the_question_part_title_for_each_question_part_multipart_question(self):
        pass

    def he_clicks_on_the_performance_bar_for_the_question_part(self):
        pass

    def the_performance_bar(self):
        pass

    def the_performance_popover_is_showing_corresponding_categories_of_red_yellow_green_and_gray_according_with_students_results_no_credit_partial_credit_full_credit_no_results(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_with_units_opened_on_p1(self, p1 = "p1"):
        pass

    def the_students_are(self):
        pass

    def there_are_skills_linked_to_a_subunit(self):
        pass

    def he_clicks_on_a_skill_abbreviation_chip(self):
        pass

    def the_students_are_ordered_alphabetically_in_each_score_category(self):
        pass

    def he_sees_the_popover_title_having_the_same_value_as_the_skill_chip_ie_as_defined_in_the_metadata_spreadsheet_subject_framework_tab__subskillsub_practice_identifier_level_3_1_a_2_c_etc(self):
        pass

    def no_results_category_is_not_displayed(self):
        pass

    def a_popover_will_still_display_no_credit_partial_credit_and_full_credit_categories_even_if_no_student_is_in_those_categories(self):
        pass

    def the_question_is_multipart(self):
        pass

    def he_clicks_on_the_student_name_from_the_student_performance_popover_for_a_question_part(self):
        pass

    def no_color_swatch_vertical_line_appears_next_to_each_students_name(self):
        pass

    def there_are_skills_linked_to_subunits(self):
        pass

    def he_sees_the_popover_title_having_the_color_matching_the_color_of_the_skill_chip(self):
        pass

    def he_sees_the_popover_subtitle_displayed_between_the_title_and_the_info_text(self):
        pass

    def the_subtitle_has_the_value_of_the_skill_category_as_defined_in_the_metadata_spreadsheet_subject_framework_tab__skill_column__level_2(self):
        pass

    def he_sees_an_info_text_displayed_in_the_popover_under_the_subtitle(self):
        pass

    def the_info_text_matches_the_text_of_the_subskillsubpractice_as_defined_in_the_metadata_spreadsheet_subject_framework_tab__level_3(self):
        pass

    def there_are_multiple_skills_linked_to_a_subunit(self):
        pass

    def the_teacher_clicks_on_the_p1_skill_chip(self, p1 = "p1"):
        pass

    def he_sees_the_p2_nav_arrow_in_the_popover_displayed_as_disabled(self, p2 = "p2"):
        pass

    def teacher_clicks_on_progress_dashboard_tab(self):
        pass

    def he_sees_a_filtering_placeholder_which_is_operative_with_a_combo_box_for_district_and_school_dropdowns_and_a_participation_checkbox(self):
        pass

    def the_teacher_clicks_on_the_active_p1_nav_arrow(self, p1 = "p1"):
        pass

    def the_teacher_clicks_on_a_skill_chip_which_is_not_the_first_nor_the_last(self):
        pass

    def a_teacher_on_the_popover_of_a_skill_opened_from_units_dashboard(self):
        pass

    def there_are_multiple_skills_linked_to_that_subunit(self):
        pass

    def he_is_taken_to_the_popover_of_the_p1_skill_in_the_order_they_are_displayed(self, p1 = "p1"):
        pass

    def it_was_opened_and_then_locked(self):
        pass

    def part_a_p1(self, p1 = "p1"):
        pass

    def it_was_opened_and_then_marked_as_completed(self):
        pass

    def the_teacher_clicks_on_x_button_displayed_in_the_top_right_corner(self):
        pass

    def the_popover_is_closed(self):
        pass

    def the_teacher_clicks_outside_the_popover_on_an_empty_space_in_the_screen(self):
        pass

    def the_popover_remains_opened_for_that_specific_skill(self):
        pass

    def the_teacher_clicks_on_a_different_skill_linked_to_p1_subunit(self, p1 = "p1"):
        pass

    def the_initial_popover_closes_and_a_new_popover_opens_for_the_new_clicked_skill(self):
        pass

    def a_teacher_on_the_popover_of_a_skill_opened_from_units_dashboard(self):
        pass

    def a_skill_with_longer_description_was_linked_to_a_subunit(self):
        pass

    def a_teacher_clicks_on_that_specific_skill_in_the_units_dashboard(self):
        pass

    def the_skill_popover_opens_and_displays_its_elements_with_a_vertical_scroll_bar(self):
        pass

    def a_teacher_on_the_units_dashboard_and_there_are_multiple_skills_linked_to_a_subunit(self):
        pass

    def the_teacher_clicks_on_a_skill_and_the_space_is_p1_in_the_user_viewport(self, p1 = "p1"):
        pass

    def the_skill_popover_opens_p2_selected_skill(self, p2 = "p2"):
        pass

    def the_teacher_p1(self, p1 = "p1"):
        pass

    def the_selected_skill_chip_is_highlighted_in_blue(self):
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

    def the_teacher_clicks_on_stimulus_button(self):
        pass

    def the_question_is_displayed(self):
        pass

    def he_sees_the_response_on_the_left_side_of_the_page(self):
        pass

    def he_sees_scoring_instructions_on_the_right_side_of_the_page(self):
        pass

    def scoring_options_below_the_scoring_instructions(self):
        pass

    def the_teacher_selects_a_specific_score(self):
        pass

    def the_score_specific_feedback_is_displayed(self):
        pass

    def the_score_specific_feedback_includes_also_selectable_checkboxes(self):
        pass

    def the_score_is_saved_automatically(self):
        pass

    def a_checkmark_appears_below_the_question_number_in_the_scoring_navigator(self):
        pass

    def he_sees_a_placeholder_for_course_summary__a_video_link_placeholder_and_a_p1_button(self, p1 = ""):
        pass

    def a__role_on_the_login_page_opened_on__env_using__browser(self):
        pass

    def navigates_to_progress_check_page_results_tab(self):
        pass

    def the_teacher_view_all_the_assignments_results_for_his_classes(self):
        pass

    def navigates_to_progress_check_page_results_tab(self):
        pass

    def the_assignment_is_mcq(self):
        pass

    def the_teacher_view_only_the_assignments_which_have_at_least_one_student_from_the_class_that_was_fully_scored(self):
        pass

    def he_sees_that_the_per(self):
        pass

    def a_teacher_on_progress_check_results_page(self):
        pass

    def he_clicks_on_student_performance_bar_for_an_assignment(self):
        pass

    def he_sees_all_the_students_which_are_not_fully_scored_displayed_in_the_no_results_category_light_gray_color(self):
        pass

    def he_clicks_on_the_student_performance_bar_for_an_assignment(self):
        pass

    def he_looks_at_the_performance_bar(self):
        pass

    def we_have_an_assignment_where_no_student_submitted(self):
        pass

    def the_students_have_not_been_yet_scored(self):
        pass

    def just_one_student_is_not_scored(self):
        pass

    def the_question_has_more_than_one_score_parts(self):
        pass

    def below_the_question_title_there_is_a_nav_that_displays_left_and_right_arrows_and_the_names_of_each_scorepart(self):
        pass

    def the_teacher_clicks_on_one_of_the_score_parts(self):
        pass

    def the_corresponding_scoring_instructions_and_scores_appear_for_that_part(self):
        pass

    def the_teacher_clicks_on_the_scoring_parts_navigation_arrows(self):
        pass

    def the_scoring_parts_are_shown_in_a_carousel_way(self):
        pass

    def is_not_switching_from_one_part_to_another(self):
        pass

    def selects_one_of_the_navigation_arrows_lower_side(self):
        pass

    def he_scores_an_assessment_with_multiple_score_parts(self):
        pass

    def the_teacher_will_see_the_next_scoring_part(self):
        pass

    def is_at_the_last_scoring_part_of_the_question(self):
        pass

    def the_teacher_will_see_the_next_question(self):
        pass

    def the_user_is_pressing_tab_key(self):
        pass

    def he_can_navigate_to_all_scoring_parts_from_one_to_the_other(self):
        pass

    def he_will_see_a_visual_focus_for_the_selectednavigated_area(self):
        pass

    def is_using_a_screen_reader_nvda(self):
        pass

    def the_screen_reader_will_read_the_whole_modal(self):
        pass

    def the_students_have_been_scored(self):
        pass

    def the_question_part_has_more_than_1_point_to_be_scored(self):
        pass

    def he_sees_that_the_performance_popover_is_displaying_4_performance_tiers_dark_yellowlight_yellowlight_greendark_green_corresponding_to_the_ranges_0_to_249925_to_499950_to_749975_to_100(self):
        pass

    def he_looks_at_the_student_performance_popover_window(self):
        pass

    def he_sees_that_the_students_are_ordered_first_by_the_student_score_report_and_then_alphabetically_by_first_name_and_then_last_name_in_each_score_category(self):
        pass

    def he_sees_that_for_each_student_is_displayed_the_student_score(self):
        pass

    def students_are(self):
        pass

    def the_students_are_displayed_under_each_category_according_with_their_results(self):
        pass

    def at_the_bottom_is_displayed_the_total_number_of_students_from_each_category_followed_by_an_icon(self):
        pass

    def the_points_are_displayed_as_whole_numbers_with_no_decimal_points(self):
        pass

    def he_sees_that_the_performance_popover_is_displaying_4_performance_categories_dark_yellowlight_yellowlight_greendark_green_corresponding_to_the_ranges_0_to_249925_to_499950_to_749975_to_100(self):
        pass

    def he_sees_in_the_popover_4_categories_plus_no_results(self):
        pass

    def all_the_students_are_all_displayed_in_the_no_results_column(self):
        pass

    def student_is_on_the_results_page(self):
        pass

    def x_sign_appears_next_to_the_incorrect_answer(self):
        pass

    def feedback_is_displayed_at_the_bottom_of_the_screen(self):
        pass

    def feedback_about(self):
        pass

    def feedback_about_the_answer_is_displayed_at_the_bottom_of_the_screen(self):
        pass

    def student_can_see_feedback_about_the_answer_at_the_bottom_of_the_page(self):
        pass

    def student_can_see_question_name(self):
        pass

    def student_can_see_question(self):
        pass

    def student_can_see_answer_options(self):
        pass

    def student_results_toggle_is_on_for_that_assessment(self):
        pass

    def student_results_toggle_is_off_for_that_assessment(self):
        pass

    def the_student_should_not_see_that_assessment_displayed_in_the_results_page(self):
        pass

    def student_sees_status_as_p1_in_results_page(self, p1 = ""):
        pass

    def the_teacher_clicks_on_student_view_button(self):
        pass

    def a_modal_is_displayed_showing_the_stimulus_and_student_answer(self):
        pass

    def an_x_button_is_displayed_in_the_top_right_corner_of_the_modal(self):
        pass

    def opens_student_view_modal(self):
        pass

    def he_can_navigate_to_student_view(self):
        pass

    def he_naviga(self):
        pass

    def the_screen_reader_will_read_each_of_the_scoring_parts(self):
        pass

    def the_teacher_clicks_on_score_average_cell_from_topics_and_skills_tab(self):
        pass

    def a_popover_is_displayed_with_a_list_of_students_down_the_left_hand_side_and_a_list_of_questions_along_the_top(self):
        pass

    def a_an_ap_teacher_on_progress_check_results_page_of_an_mcq_only_quiz(self):
        pass

    def a_teacher_on_progress_check_results_page_of_an_mcq_only_quiz_opened_from_p1(self, p1 = "p1"):
        pass

    def a_popover_is_displayed_containing_a_list_of_students_down_the_left_hand_side__a_list_of_questions_along_the_top__info_text__x_button(self):
        pass

    def a_teacher_on_a_performance_cell_popover_opened_from_topics_and_skills_tab_of_a_progress_check_mcq(self):
        pass

    def he_clicks_outside_the_popover(self):
        pass

    def the_popover_closes(self):
        pass

    def the_teacher_clicks_on_the_x_button_from_the_top_right_corner(self):
        pass

    def he_clicks_on_a_score_average_cell_from_topics_and_skills_tab(self):
        pass

    def he_sees_inside_the_popover_displayed_a_list_of_questions_ordered_by_the_the_sequence_they_are_administered_in_the_assignment(self):
        pass

    def the_teacher_inspects_the_list_of_questions(self):
        pass

    def he_sees_inside_the_popover_displayed_each_question_number_is_the_questions_position_in_the_quiz(self):
        pass

    def the_teacher_inspects_the_list_of_students(self):
        pass

    def he_sees_inside_the_popover_displayed_a_list_of_students_alphabetized_by_first_name_then_last_name(self):
        pass

    def a_teacher_on_progress_check_results_page_of_an_mcq_only_quiz(self):
        pass

    def he_sees_inside_the_popover_displayed_a_info_text_displayed_at_the_top_on_average_students_earned_x_of_y_points_where_xnumerator_of_the_cell_and_ydenominator_of_the_cell(self):
        pass

    def the_teacher_clicks_on_a_score_average_cell_from_topics_and_skills_tab(self):
        pass

    def he_sees_inside_the_popover_displayed_only_the_questions_linked_to_that_specific_topicskill_pair(self):
        pass

    def he_sees_inside_the_popover_displayed_a_list_of_students_that_can_be_scrolled_if_necessary(self):
        pass

    def he_sees_inside_the_popover_displayed_all_the_students_that_submitted_the_quiz(self):
        pass

    def he_sees_the_popover_having_different_widths_depending_on_the_number_of_questions_linked_to_that_topicskill_pair(self):
        pass

    def he_sees_inside_the_popover_displayed_the_student_names_that_submitted_the_quiz_displayed_as_links(self):
        pass

    def he_sees_inside_the_popover_displayed_the_question_numbers_displayed_as_links(self):
        pass

    def he_clicks_on_a_student_link(self):
        pass

    def he_clicks_on_a_question_link(self):
        pass

    def he_is_taken_to_the_overview_of_questionlevel_performance_for_the_student_subject_idassessmentsresultsquiz_idstudentsstudent_id(self):
        pass

    def he_is_taken_to_the_class_performance_detail_view_for_that_particular_question_eg_25assessmentsresults110327questions581219(self):
        pass

    def he_clicks_on_a_score_average_cell_from_topics_and_skills_tab_where_the_students_have_answered_p1(self, p1 = "p1"):
        pass

    def have_submitted_the_quiz(self):
        pass

    def the_teacher_selects_a_specific_question(self):
        pass

    def the_question_number_had_2_circles_around_it(self):
        pass

    def the_student_answered_the_question(self):
        pass

    def the_question_circle_in_filled_in_blue(self):
        pass

    def the_teacher_selects_the_lowest_score(self):
        pass

    def an_x_appears_below_the_question_number_in_the_scoring_navigator(self):
        pass

    def the_teacher_selects_an_average_score(self):
        pass

    def an_o_appears_below_the_question_number_in_the_scoring_navigator(self):
        pass

    def he_sees_that_the_performance_bar_is_spilt_in_maximum_4_performance_categories_dark_yellowlight_yellowlight_greendark_green_corresponding_to_the_ranges_0_to_249925_to_499950_to_749975_to_100(self):
        pass

    def a_category_is_displayed_only_if_at_least_one_student_fall_into_that_category(self):
        pass

    def the_teacher_scores_only_some_parts(self):
        pass

    def no_icon_is_displayed_below_the_question_number_in_the_scoring_navigator(self):
        pass

    def the_teacher_selects_the_highest_score(self):
        pass

    def the_teacher_scores_all_the_parts(self):
        pass

    def a_corresponding_icon_is_displayed_below_the_question_number_in_the_scoring_navigator(self):
        pass

    def when(self):
        pass

    def the_popup_will_disappear_after_1_second(self):
        pass

    def the_score_is_saved_automatically_displaying_a_popup_with_timestamp(self):
        pass

    def a_p3_on_the_homepage_of_a_p1_subject_where_course_resources_were_configured_in_the_metadata_spreadsheet_and_imported(self, p1 = "p1", p3 = "p3"):
        pass

    def he_inspects_the_first_tab_from_unit_dashboard(self):
        pass

    def he_sees_course_displayed_as_first_tab(self):
        pass

    def the_teacher_selects_a_checkbox_for_a_specific_score(self):
        pass

    def he_navigates_to_the_next_question_or_scoring_part(self):
        pass

    def he_inspects_the_course_tab(self):
        pass

    def the_teacher_is_adding_some_student_feedback(self):
        pass

    def he_saves_the_feedback_popup(self):
        pass

    def he_sees_that_each_p2_matches_the_p4_column_cell_from_the_resources_tab_of_the_imported_metadata_spreadsheet(self, p2 = "p2", p4 = "p4"):
        pass

    def the_teacher_is_scoring_some_questions(self):
        pass

    def he_closes_the_scoring_page_score_by_rubric_without_submitting(self):
        pass

    def he_returns_to_the_scoring_page(self):
        pass

    def the_scoring_page_is_opened_at_the_last_saved_screen_while_scoring(self):
        pass

    def he_clicks_submit(self):
        pass

    def the_student_is_able_to_see_his_results(self):
        pass

    def he_scores_all_parts_and_questions(self):
        pass

    def a_p3_on_the_homepage_of_an_p1_subject_opened_from_p6(self, p1 = "p1", p3 = "p3", p6 = "p6"):
        pass

    def he_does_not_click_submit_button(self):
        pass

    def the_student_is_not_able_to_see_his_results(self):
        pass

    def mcq(self):
        pass

    def he_clicks_on_course_tab(self):
        pass

    def he_sees_p3_on_the_homepage_of_a_p1_subject(self, p1 = "p1", p3 = "p3"):
        pass

    def he_sees_the_tab_p2_matches_the_p4_of_unit_0_row_from_the_units_tab_of_the_imported_metadata_spreadsheet(self, p2 = "p2", p4 = "p4"):
        pass

    def he_sees_2_subunits_resources_for_teachers_and_resources_for_students_as_configured_in_the_subunits_tab_of_the_metadata_spreadsheet(self):
        pass

    def he_sees_the_resources_icon_displayed_in_front_of_the_subunits_configured_from_the_subunits_tab_of_metadata_config(self):
        pass

    def he_sees_the_resources_that_were_configured_in_the_metadata_spreadsheet_as_p1_displayed_p2(self, p1 = "p1", p2 = "p2"):
        pass

    def the_resources_that_were_configured_in_the_metadata_spreadsheet_as_p1_are_p2_for_him(self, p1 = "p1", p2 = "p2"):
        pass

    def there_are_students_that_p1(self, p1 = ""):
        pass

    def the_teacher_of_that_class_goes_to_progress_checks_page__results__topics_and_skills_tab_of_the_above_progress_check_mcq(self):
        pass

    def a_student_submitted_a_progress_check_mcq_and_p1_a_question(self, p1 = "p1"):
        pass

    def clicks_on_the_performance_cell_popover_containing_the_above_question(self):
        pass

    def he_sees_for_the_above_student_the_question_marked_with_a_p2(self, p2 = "p2"):
        pass

    def he_has_p1_a_question_from_that_quiz(self, p1 = "p1"):
        pass

    def a_student_has_not_submitted_yet_a_progress_check_mcq(self):
        pass

    def he_sees_for_the_above_student_the_question_marked_with_no_results_label(self):
        pass

    def a_student_has_not_started_yet_a_progress_check_mcq(self):
        pass

    def he_sees_for_the_above_student_all_the_questions_of_the_cell_marked_with_one_no_results_label(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_where_skills_were_configured_in_the_metadata_spreadsheet(self):
        pass

    def he_does_not_skills_column_for_this_tab_even_though_it_is_displayed_for_all_the_other_regular_unit_tabs(self):
        pass

    def a_student_on_the_homepage_of_a_subject_that_has_shared_student_resources_but_no_shared_teacher_resources(self):
        pass

    def he_does_not_see_resources_for_teachers_subunit(self):
        pass

    def the_teacher_of_that_class_has_shared_student_resources_but_not_shared_any_teacher_resources(self):
        pass

    def the_student_clicks_on_course_tab(self):
        pass

    def the_teacher_of_that_class_has_not_shared_any_resources_with_his_students_yet(self):
        pass

    def a_teacher_has_not_shared_yet_any_course_resources_with_a_class_for_a_specific_subject(self):
        pass

    def a_student_from_that_class_goes_to_the_above_subject_homepage(self):
        pass

    def he_does_not_see_course_tab_at_all(self):
        pass

    def metadata_import_was_done_linking_p1_course_resources_to_the_course_subunits(self, p1 = ""):
        pass

    def he_sees_those_resources_associated_to_the_specific_subunits(self):
        pass

    def he_clicks_on_pdf_link_from_course_tab(self):
        pass

    def the_resource_file_downloads_and_can_be_opened(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_where_course_resources_were_not_added_in_the_metadata_spreadsheet(self):
        pass

    def he_sees_unit_1_displayed_as_first_tab(self):
        pass

    def a_teacher_on_p1_page__results_tab_of_an_mcq_ap_assignment__p4_subtab_opened_from_p3(self, p1 = "p1", p3 = "p3", p4 = "p4"):
        pass

    def the_teacher_clicks_on_an_individual_question(self):
        pass

    def he_sees_on_the_right_side_of_the_screen_section_named_related_questions_on_this_quiz_displaying_a_list_of_question_links(self):
        pass

    def he_does_not_see_on_the_right_side_of_the_screen_the_related_questions_on_this_quiz_section(self):
        pass

    def a_teacher_on_assessments_page__results_tab_of_an_p1_ap_assignment__p2_subtab_opened_from_p3(self, p1 = "", p2 = "", p3 = ""):
        pass

    def a_teacher_on_assessments_page__results_tab_of_a_pre_ap_assignment__p2_subtab(self, p2 = ""):
        pass

    def a_teacher_on_progress_checks_page__results_tab_of_an_ap_assignment__questions_subtab(self):
        pass

    def he_sees_under_related_questions_on_this_quiz_section_a_list_with_all_the_questions_from_the_same_assignment_linked_to_the_same_topicskill_pair(self):
        pass

    def a_teacher_on_progress_checks_page__results_tab_of_an_ap_assignment__students_individual_student_subtab(self):
        pass

    def he_sees_under_related_questions_on_this_quiz_section_the_list_of_related_questions_displayed_in_sequential_order_order_they_appear_on_the_assignment(self):
        pass

    def the_teacher_clicks_on_a_question_that_is_the_only_one_linked_to_a_specific_topicskill_pair(self):
        pass

    def he_sees_no_related_questions_on_this_quiz_section_for_it(self):
        pass

    def a_teacher_on_qb_page__results_tab_of_an_ap_assignment__questions_subtab(self):
        pass

    def he_does_not_see_under_the_related_questions_on_this_quiz_list_the_currently_viewed_item(self):
        pass

    def he_sees_under_the_related_questions_on_this_quiz_section_the_list_of_questions_having_as_item_identified_the_question_number_question_x(self):
        pass

    def a_teacher_on_qb_page__results_tab_of_an_ap_assignment__individual_students_subtab(self):
        pass

    def then_on_a_question_number_from_the_related_questions_on_this_quiz_section(self):
        pass

    def he_is_taken_to_that_specific_question_hyperlink_to_resultsquiz_idquestionsitemitem_id(self):
        pass

    def a_teacher_on_p1_page__results_tab_of_an_frq_ap_assignment__p2_subtab(self, p1 = "", p2 = ""):
        pass

    def a_teacher_on_qb_page__results_tab_of_a_mixed_ap_assignment__questions_subtab(self):
        pass

    def the_teacher_clicks_on_an_individual_p1_question(self, p1 = "p1"):
        pass

    def he_result(self, p2 = "p2"):
        pass

    def the_teacher_clicks_on_an_individual_question_tagged_with_multiple_p1(self, p1 = "p1"):
        pass

    def he_p2_under_related_questions_on_this_quiz_section_a_list_of_questions_tagged_with_all_p1_as_the_this_one(self, p2 = "p2", p1 = "p1"):
        pass

    def student_is_on(self):
        pass

    def a_student_is(self):
        pass

    def the_x_button_becomes_highlighted_in_blue(self):
        pass

    def the_x_button_becomes_again_grey(self):
        pass

    def he_should_see_the_course_outline_related_to_the_specific_subject(self):
        pass

    def a_student_on_the_final_exam_pilot_page_opened_on_an_p1_browser_session(self, p1 = "p1"):
        pass

    def he_opens_an_exam_session(self):
        pass

    def he_does_not_see_in_the_top_right_corner_an_x_button(self):
        pass

    def a_student_working_on_a_non_timed_assignment_opened_from_p1(self, p1 = "p1"):
        pass

    def he_clicks_on_the_x_button_from_the_top_right_corner(self):
        pass

    def a_popup_is_displayed_having_title_save_and_exit__message_your_progress_has_been_saved_you_have_not_yet_submitted_the_assignment_do_you_want_to_exit_the_assignment__no_and_yes_buttons(self):
        pass

    def a_student_working_on_a_timed_assignment_opened_from(self):
        pass

    def a_popup_is_displayed_having_title_save_and_exit__message_you_havent_submitted_your_timed_assessment_if_you_leave_this_page_the_timer_will_continue_to_run_and_your_response_will_not_be_submitted_are_you_sure_you_want_to_leave_this_page__no_and_yes_buttons(self):
        pass

    def a_student_on_the_save_and_exit_popup_for_exiting_a_quiz(self):
        pass

    def he_clicks_on_the_x_button_from_the_top_right_corner_and_then_on_the_no_button_from_the_save_and_exit_popup(self):
        pass

    def the_popup_closes_and_he_is_taken_back_in_the_assignment_to_p1(self, p1 = "p1"):
        pass

    def he_clicks_on_the_yes_button(self):
        pass

    def he_is_able_to_reach_the_x_button_from_the_top_right_corner_which_becomes_highlighted(self):
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

    def a_student_on_p1_from_a_quiz_player(self, p1 = "p1"):
        pass

    def then_on_the_no_button_from_the_save_and_exit_popup(self):
        pass

    def the_popup_closes_and_he_is_taken_back_to_the_assignment(self):
        pass

    def a_student_on_the_save_and_exit_popup_opened_inside_of_a_quiz_player(self):
        pass

    def the_popup_closes_and_he_is_taken_back_to_assignments_tab_url__assessmentsassignments(self):
        pass

    def a_student_on_a_quiz_player(self):
        pass

    def he_tabs_through_the_screen(self):
        pass

    def reaches_the_x_button_from_the_top_right_corner(self):
        pass

    def the_screen_reader_reads_it_as_close_button(self):
        pass

    def he_clicks_on_enter_key_from_the_keyboard_while_being_with_the_visual_focus_on_the_x_button_from_the_top_right_corner(self):
        pass

    def the_save_and_exit_popup_is_opened(self):
        pass

    def the_screen_reader_reads_the_text_inside_the_save_and_exit_popup(self):
        pass

    def a_student_on_the_save_and_exit_popup_from_a_quiz_player(self):
        pass

    def he_tabs_through_its_elements(self):
        pass

    def p1_button_is_reached_and_becomes_highlighted(self, p1 = "p1"):
        pass

    def p1_button_is_read_by_the_screen_reader(self, p1 = "p1"):
        pass

    def he_sees_the_subject_dropdown_on_the_left_corner_of_the_page(self):
        pass

    def a_teacher__subject_teacher(self):
        pass

    def the_teacher_is_on_the(self):
        pass

    def the_teacher_is_on(self):
        pass

    def teacher_is_on_the_homepage_of__subject(self, datatable = "||"):
        pass

    def he_sees_course_outline_that_pertains_to__subject(self):
        pass

    def teacher_is_p1_teacher(self, p1 = ""):
        pass

    def he_clicks_on_progress_check_tab(self):
        pass

    def teacher_is_on_p1_homepage(self, p1 = ""):
        pass

    def he_can_see_assessments_that_belong_to_p1(self, p1 = ""):
        pass

    def teacher_is_on_progress_check_tab(self):
        pass

    def he_can_assign_the_assessment_that_belongs_to_p1_subject(self, p1 = ""):
        pass

    def he_can_assign_an_assessment_that_belongs_to_p1_subject(self, p1 = ""):
        pass

    def he_can_assign_assessment_that_belong_to_p1(self, p1 = ""):
        pass

    def to_p1_class(self, p1 = ""):
        pass

    def a_teacher_on_progress_checks__results_tab__quiz_level_questions_tab(self):
        pass

    def he_clicks_on_a_question_that_has_multiple_correct_answers(self):
        pass

    def he_sees_all_correct_answers_have_a_green_checkmark_next_to_them(self):
        pass

    def he_sees_at_question_level_the_top_correct_answer_with_a_green_rectangle_around_it(self):
        pass

    def he_sees_the_top_correct_answer_with_its_feedback_shown_below_the_question(self):
        pass

    def a_teacher_on_progress_checks__results_tab__quiz_level_questions_tab__individual_question_with_multiple_correct_answers(self):
        pass

    def he_clicks_on_an_answer_option_which_is_p1(self, p1 = "p1"):
        pass

    def he_sees_only_one_p2_rectangle_around_the_selected_answer(self, p2 = "p2"):
        pass

    def a_teacher_on_qb__create_tab(self):
        pass

    def he_clicks_on_place(self, p1 = "", free_text = "", datatable = "||"):
        pass

    def question_preview_page_is_displayed_without_p2(self, p2 = "p2"):
        pass

    def he_clicks_on_preview_button_for_a_p1_question(self, p1 = "p1"):
        pass

    def question_preview_page_is_opened_successfully_having_the_following_elements_question_content_answer_area_add_button_pencil_icon_toolbar_x_button_question_details_slider_leftright_nav_arrows(self):
        pass

    def a_teacher_on_qb__create_tab_which_contains_y_number_of_questions_in_total(self):
        pass

    def he_clicks_on_question_number_x_from_the_question_table_list(self):
        pass

    def question_preview_opens_and_displays_on_the_upper_right_side_the_element_x_of_y(self):
        pass

    def he_opens_the_preview_for_the_p1_question_from_the_table(self, p1 = "p1"):
        pass

    def question_preview_opens_and_has_the_p2_nav_arrow_disabled(self, p2 = "p2"):
        pass

    def a_teacher_on_the_preview_of_a_question_opened_from_qb__create_tab(self):
        pass

    def he_clicks_on_the_p1_nav_arrow(self, p1 = ""):
        pass

    def he_is_taken_to_the_preview_of_the_p2_question_where_he_sees_p3(self, p2 = "p2", p3 = "p3"):
        pass

    def he_sees_res(self):
        pass

    def he_is_taken_back_to_create_tab_to_the_page_that_contains_that_question(self):
        pass

    def he_clicks_on_the_preview_button_from_rightmost_column_where_he_is_building_an_assessment(self):
        pass

    def he_sees_the_question_as_if_its_part_of_an_assessment_preview_because_he_is_previewing_the_assessment_not_the_question(self):
        pass

    def he_clicks_on_a_question_title_link_from_rightmost_column_where_he_is_building_an_assessment(self):
        pass

    def he_sees_the_question_preview_without_being_displayed_as_part_of_the_assessment(self):
        pass

    def he_clicks_on_the_question_details_slider(self):
        pass

    def the_slider_opens_and_displays_the_metadata_of_the_question(self):
        pass

    def he_clicks_on_any_button_from_the_toolkit_panel(self):
        pass

    def the_specific_menu_opens(self):
        pass

    def he_clicks_on_the_pencil_button_from_the_top_right_corner(self):
        pass

    def he_is_taken_to_the_edit_form_of_that_specific_question(self):
        pass

    def he_clicks_on_the_add_button_from_the_top_right_corner(self):
        pass

    def the_question_is_added_to_the_assessment_that_is_building_in_the_background_without_closing_the_preview(self):
        pass

    def the_add_button_becomes_disabled(self):
        pass

    def the_question_is_added_to_the_quiz_in_the_background_and_the_add_button_becomes_disabled(self):
        pass

    def a_teacher_has_added_a_question_to_a_quiz_that_is_being_build(self):
        pass

    def he_removes_the_question_from_the_quiz(self):
        pass

    def opens_that_question_preview(self):
        pass

    def he_sees_the_add_button_displayed_as_enabled(self):
        pass

    def he_opens_the_preview_of_a_question_with_shared_prompt_mcms(self):
        pass

    def he_sees_that_the_preview_looks_the_same_as_when_previewing_an_assessment_from_progress_checks__assign(self):
        pass

    def a_filter_has_been_set_in_the_left_panel(self):
        pass

    def the_teacher_opens_the_preview_of_a_question_from_the_filtered_list(self):
        pass

    def clicks_on_left_right_nav_arrows(self):
        pass

    def he_is_able_to_navigate_between_questions_that_meet_my_filter_criteria_without_closing_the_preview(self):
        pass

    def he_clicks_on_the_right_nav_arrow_until_reaching_the_preview_of_a_question_from_page_2(self):
        pass

    def then_closes_the_question_preview(self):
        pass

    def a_teacher_on_the_preview_of_a_question_from_page_1_of_qb__create_tab(self):
        pass

    def a_filter_p1_set_in_the_left_panel_for_the_metadata(self, p1 = "p1"):
        pass

    def he_ends_up_on_page_2_of_the_create_tab(self):
        pass

    def there_is_a_big_number_of_questions_in_the_list(self):
        pass

    def the_teacher_opens_a_question_preview(self):
        pass

    def from_here_navigates_through_questions(self):
        pass

    def preview_form_updates_and_loads_in_a_timely_manner(self):
        pass

    def he_clicks_on_the_assign_button_for_a_newly_created_quiz(self):
        pass

    def he_sees_in_the_assign_popup_the_scramble_question_option_available(self):
        pass

    def a_teacher_on_qb__assign_tab(self):
        pass

    def he_clicks_on_the_assign_button_for_a_quiz(self):
        pass

    def a_teacher_assigns_a_quiz_with_scramble_question_option_on_to_2_classes(self):
        pass

    def the_students_from_the_2_classes_submit_the_responses_for_the_quiz(self):
        pass

    def he_observes_that_the_questions_order_is_different_for_the_two_quizzes(self):
        pass

    def opens_each_quiz_and_looks_at_the_questions_order_in_p1_tab(self, p1 = "p1"):
        pass

    def a_teacher_assigns_a_quiz_with_scramble_option_on_to_2_classes(self):
        pass


    def a_teacher_is_already_on_qb__assign_tab_assign_modal(self):
        pass

    def the_info_text_each_class_will_see_the_questions_in_a_different_order(self):
        pass

    def the_info_text_each_class_will_see_the_questions_in_a_different_order(self):
        pass

    def a_student_from_one_of_the_classes_submits_the_quiz(self):
        pass

    def goes_to_assessments__progress_tab__click_on_review_button(self):
        pass

    def he_sees_the_question_order_from_the_quiz_player_is_maintained_in_progress_review(self):
        pass

    def he_goes_to_question_bank__progress_tab__enter_score_page_for_each_of_the_2_quizzes(self):
        pass

    def he_sees_the_questions_order_is_different_for_the_two_quizzes(self):
        pass

    def goes_to_assessments__results_page__clicks_on_the_quiz(self):
        pass

    def he_sees_the_questions_order_from_the_quiz_player_is_maintained_in_results_tab(self):
        pass

    def a_student_on_a_quiz_player_opened_from_a_mobile_device_on_portrait_view(self):
        pass

    def he_navigates_to_an_mcq_with_no_associated_passages(self):
        pass

    def the_question_is_displayed_the_same_way_as_on_desktop_view_in_a_single_column_on_full_page(self):
        pass

    def he_selects_an_mcq_response_and_navigates_to_another_question(self):
        pass

    def he_sees_the_autosave_popover_positioned_on_top_of_the_page(self):
        pass

    def he_no_longer_sees_the_zoom_tool_as_on_desktop(self):
        pass

    def a_student_on_a_quiz_player_opened_from_a_mobile_p1_device_on_portrait_view(self, p1 = "p1"):
        pass

    def a_student_first_opening_a_quiz_player_from_a_mobile_device_on_portrait_view(self):
        pass

    def a_student_first_opening_a_a_quiz_player_from_a_mobile_device_on_portrait_view(self):
        pass

    def he_sees_on_the_upper_nav_bar_a_small_orange_empty_icon(self):
        pass

    def some_questions_have_been_bookmarked_and_some_left_unbookmarked(self):
        pass

    def each_question_keeps_its_bookmark_state(self):
        pass

    def he_no_longer_sees_the_submit_button_as_on_desktop(self):
        pass

    def he_sees_instead_of_the_toolkit_panel_from_desktop_view_a__button(self):
        pass

    def clicks_on_the__button(self):
        pass

    def the_toolkit_panel_gets_expanded_displaying_all_the_tool_calculator_when_necessary__annotation_help_accessibility_submit_button(self):
        pass

    def he_navigates_to_an_mcq_marked_with_p1(self, p1 = "p1"):
        pass

    def he_p2_the_calculator_icon_to_the_left_side_of_question_title(self, p2 = "p2"):
        pass

    def he_navigates_to_a_p1_frq_question_without_passages_and_without_multipart(self, p1 = "p1"):
        pass

    def he_sees_2_tabs_at_the_top_question_question_number_and_my_response(self):
        pass

    def he_navigates_to_a_regular_mcq_question_without_passages(self):
        pass

    def he_sees_the_question_and_its_option_answers_in_a_single_page(self):
        pass

    def he_navigates_to_a_multipart_p1_frq_question(self, p1 = "p1"):
        pass

    def he_res(self, p2 = "p2"):
        pass

    def he_navigates_to_p1_question_with_a_passage(self, p1 = "p1"):
        pass

    def user_p1_is_on_progress_dashboard(self, p1 = ""):
        pass

    def a_user_is_on_the_progress_dashboard_page(self):
        pass

    def he_clicks_on_course_summary_tab(self):
        pass

    def he_clicks_on_course_summary(self):
        pass

    def he_clicks_on(self):
        pass

    def he_clicks_on__tab(self):
        pass

    def he_sees_a_table_with_district_and_school_listing(self):
        pass

    def he_can_see_performance_data_in_cells_for_each_school(self):
        pass

    def table_header_displays_points_possible_for_each_unit(self):
        pass

    def he_sees_each_cell_value_equal_to_average_score_of_all_retakes_for_assessments_in_that_unit(self):
        pass

    def school_listing_displays_the_correct_list_of_schools_that_the_teacher_is_in(self):
        pass

    def the_school_listing_displays_the_correct_list_of_schools_that_the_teacher_is_in(self):
        pass

    def he_sees_a_table_which_displays_aggregate_data(self):
        pass

    def he_can_see_performance_data_in_cells_for_each_section_for_a_particular_school(self):
        pass

    def he_can_see_performance_data_in_cells_at_school_level(self):
        pass

    def he_can_see_4_drop_downs_for_district_school_section_student_hierarchy_based_on_his_role(self):
        pass

    def he_clicks_on_the_course_summary(self):
        pass

    def he_sees_performance_data_displayed_in_the_cells_for_mcq(self):
        pass

    def the_color_of_each_cell_is_equal_to_the_aggregate_value_divided_by_the_points_possible_for_each_unit(self):
        pass

    def the_color_code_of_each_cell_equals_the_aggregate_data_divided_by_points_possible_for_each_unit(self):
        pass

    def he_sees_color_of_the_cells_same_as_row_color_for_the_units_that_are_not_accessed(self):
        pass

    def a_teacher_on_the_homepage_of_a_p1_subject_without_classes_created_yet(self, p1 = "p1"):
        pass

    def the_teacher_inspects_the_create_a_class_widget(self):
        pass

    def he_sees_create_a_section_class_button(self, p1 = ""):
        pass

    def he_sees_2_elements_an_info_message_p2(self, p2 = ""):
        pass

    def a_button_create_a_class_section(self):
        pass

    def he_clicks_on_create_class_button_from_the_create_a_class_widget(self):
        pass

    def a_teacher_on_the_p1_page_of_a_subject_without_any_classes_created_yet(self, p1 = "p1"):
        pass

    def a_teacher_on_the_homepage_of_a_subject_with_at_least_one_class_created(self):
        pass

    def only_one_class_has_been_created(self):
        pass

    def a_teacher_on_the_homepage_of_a_subject_with_classes_already_created(self):
        pass

    def clicks_on_back_to_ap_classroom_button(self):
        pass

    def he_edits_a_class_in_apro(self):
        pass

    def he_sets_in_the_url_the_following_parameter_p1(self, p1 = "p1"):
        pass

    def a_teacher_of_any_page_of_a_subject_with_classes(self):
        pass

    def he_is_redirected_to_the_homepage_where_class_widget_displays_class_x_and_unit_widget_displays_unit_y(self):
        pass

    def he_inspects_the_main_elements_of_the_class_progress_widget(self):
        pass

    def he_inspects_the_inside_elements_of_a_section_display(self):
        pass

    def he_sees_3_columns_quiz_titles_column_performanceprogress_bars_column_and_actions_column(self):
        pass

    def he_sees_that_the_second_column_has_2_sections_latest_results_displayed_as_first_preceded_by_assignments_in_progress_bars(self):
        pass

    def a_teacher_has_assigned_the_same_quiz_to_2_different_classes(self):
        pass

    def he_navigates_to_each_class_in_the_class_widget(self):
        pass

    def he_sees_the_above_quiz_displayed_for_both_classes_with_specific_information_per_class(self):
        pass

    def a_teacher_has_assigned_p1_assignments_to_a_class(self, p1 = "p1"):
        pass

    def he_navigates_to_that_specific_class_in_the_class_widget(self):
        pass

    def he_p2_a_show_more_button_displayed_in_the_bottom_right_corner(self, p2 = "p2"):
        pass

    def a_teacher_has_assigned_more_than_3_quizzes_to_a_class(self):
        pass

    def by_default_the_first_6_quizzessorting_rules_appliedare_displayed_on_the_screen(self):
        pass

    def the_others_are_hidden(self):
        pass

    def clicks_on_show_more_button(self):
        pass

    def the_show_more_button_changes_to_show_less(self):
        pass

    def the_screen_expands_to_displays_a_total_of_x_assignments_rows(self):
        pass

    def then_on_show_less(self):
        pass

    def clicks_on_show_more_button__afterwards_on_show_less(self):
        pass

    def the_screen_collapses_to_displays_the_default_3_assignments_rows(self):
        pass

    def the_show_less_button_changes_back_to_show_more(self):
        pass

    def a_teacher_has_assigned_a_ppc_and_a_qb_quiz_to_a_class(self):
        pass

    def the_qb_quiz_assign_date_p1_ppc_assign_date(self, p1 = ""):
        pass

    def both_quizzes_p2(self, p2 = "p2"):
        pass

    def the_teacher_navigates_to_that_specific_class_in_the_class_widget(self):
        pass

    def he_sees_the_ppc_row_elevated_before_the_qb_row_in_the_p3_section(self, p3 = "p3"):
        pass

    def a_teacher_has_not_yet_manually_assigned_pp_cs_to_a_class_still_in_the_initial_autoassigned_state(self):
        pass

    def he_sees_the_quiz_in_p2_section_having_a_gray_bar_in_the_second_column_that_reads_p3_preceded_by_a_lock_icon(self, p2 = "p2", p3 = "p3"):
        pass

    def he_sees_that_they_have_in_the_actions_column_a_p2_button(self, p2 = "p2"):
        pass

    def a_teacher_has_not_assigned_yet_any_pp_cs_nor_q_bs_to_a_class(self):
        pass

    def he_clicks_on_p2_button_of_that_quiz_from_class_widget(self, p2 = "p2"):
        pass

    def he_is_taken_to_that_p3_progress_page(self, p3 = "p3"):
        pass

    def he_sees_in_the_assignment_in_progress_section_an_info_text_in_the_first_column_you_have_no_assignments_in_progress(self):
        pass

    def in_the_second_column_a_gray_bar_with_the_text__progress_will_appear_here(self):
        pass

    def a_teacher_has_assigned_multiple_p1_to_a_class(self, p1 = ""):
        pass

    def some_of_the_assignments_are_in_progress_and_some_have_already_results(self):
        pass

    def he_sees_first_the_bars_for_results_then_progress_bars(self):
        pass

    def a_teacher_has_assigned_multiple_pp_cs_to_a_class(self):
        pass

    def the_assignments_p1(self, p1 = ""):
        pass

    def he_sees_the_pp_cs_sorted_by_unit_desc(self):
        pass

    def a_teacher_has_assigned_multiple_q_bs_to_a_class(self):
        pass

    def he_sees_the_quiz_slots_sorted_by_last_date_of_student_score_desc(self):
        pass

    def a_teacher_p1(self, p1 = "p1"):
        pass

    def a_teacher_cond(self, p1 = "p1"):
        pass

    def a_teacher_has_assigned_an_mcq_p2_only_to_a_class(self, p2 = "p2"):
        pass

    def a_teacher_has_assigned_an_mcq_p1only_to_a_class(self, p1 = ""):
        pass

    def less_than_80_of_students_have_submitted_the_quiz(self):
        pass

    def he_sees_the_quiz_row_having_a_results_barsecond___vicolumn_progress_ew_buttonthird_column(self):
        pass

    def the_quiz_in_p2_state(self, p2 = ""):
        pass

    def a_teacher_on_the_homepage_of_a_subject_with_quizzes_in_progress_for_a_class(self):
        pass

    def he_clicks_on_view_progress_button_of_a_quiz_progress_row_from_class_widget(self):
        pass

    def he_is_taken_to_that_quiz_progress_page(self):
        pass

    def there_is_a_p1_quiz_that_has_results(self, p1 = ""):
        pass

    def the_teacher_clicks_on_view_results_button_of_that_quiz_results_row_from_class_widget(self):
        pass

    def he_is_taken_to_the_quiz_results_page(self):
        pass

    def _80_of_students_have_p3(self, p3 = "p3"):
        pass

    def he_sees_the_quiz_row_having_a_results_barsecond_column__view_results_buttonthird_column(self):
        pass

    def a_teacher_has_assigned_a_p1_to_a_class(self, p1 = ""):
        pass

    def there_is_a_quiz_assigned_with_students_in_progress__0_and_0_submissions_to_score(self):
        pass

    def the_teacher_inspect_the_class_widget_for_the_above_quiz(self):
        pass

    def he_sees_the_quiz_row_having_a_view_progress_button_displayed_in_actions_column(self):
        pass

    def a_teacher_has_assigned_an_p1_frq_to_a_class(self, p1 = ""):
        pass

    def less_than_100_of_students_have_been_scored(self):
        pass

    def he_sees_the_quiz_row_having_a_view_progress_barsecond_column__view_progress_buttonthird_column(self):
        pass

    def he_sees_the_quiz_row_having_a_progress_barsecond_column__view_progress_buttonthird_column(self):
        pass

    def there_are_80_submission_scored100(self):
        pass

    def he_sees_the_quiz_having_2_rows_one_in_assignments_in_progress_with_a_progress_bar_and_one_in_latest_results_section_having_a_results_bar(self):
        pass

    def there_is_a_p1_quiz_assigned_with_students_in_progress__0(self, p1 = "p1"):
        pass

    def submitted_available_to_score__x__0(self):
        pass

    def he_sees_the_quiz_row_having_a_x_submissions_to_scorebutton_displayed_in_actions_column(self):
        pass

    def there_is_a_quiz_having_available_submissions_to_score(self):
        pass

    def the_teacher_clicks_on_the_x_submissions_to_score_button_from_the_class_widget_for_that_quiz(self):
        pass

    def he_is_taken_to_the_quiz_progress_page(self):
        pass

    def is_presented_with_one_welcome_video(self):
        pass

    def student_is_on_the_welcome_video_page_opened_from__device(self, datatable = "||"):
        pass

    def a_student_is_on_welcome_video_page_opened_from_a_p1_device(self, p1 = ""):
        pass

    def the_student_is_not_logging_in_for_the_first_time(self):
        pass

    def this_card_displays_across_multiple_devices(self):
        pass

    def a_teacher_on_the_p1(self, p1 = "p1"):
        pass

    def he_clicks_on_the_assign_button_of_a_p2_quiz(self, p2 = ""):
        pass

    def he_p3_scramble_question_order_toggle_inside_the_assign_modal(self, p3 = "p2"):
        pass

    def he_p3_take_assessment_offline_toggle_inside_the_assign_modal(self, p3 = "p2"):
        pass

    def the_student_fills_the_answer_to_1_question(self):
        pass

    def student_is_enrolled_in_ap_course(self):
        pass

    def ap_student_is_on_login_page(self):
        pass

    def the_student_submitted_response_for_the_follow_on_question(self):
        pass

    def the_student_is_done_watching_the_video_and_responding_to_follow_on_question(self):
        pass

    def he_does_not_see_the_to_do_card_anymore_when_student_logs_in_again(self):
        pass

    def a_teacher_has_assigned_more_than_6_quizzes_to_a_class(self):
        pass

    def the_assignments_are_in_the_state_of_displaying_p1(self, p1 = ""):
        pass

    def a_teacher_assigned_multiple_p2_to_a_class(self, p2 = ""):
        pass

    def user_is_redirected_to_create_tab(self):
        pass

    def teacher_clicks_publish(self, p1 = "", p2 = ""):
        pass

    def i_click_on_author_new_question__mcq(self):
        pass

    def the_teacher_is_able_to_see_learnosity_mcq_form_with_title_question_answers_correct_answer_and_tags_fields(self):
        pass

    def a_student_hasnt_started_yet_a_p1_quiz(self, p1 = "p1"):
        pass

    def he_goes_to_progress_page(self):
        pass

    def he_hasnt_yet_started_that_quiz(self):
        pass

    def he_does_not_see_that_quiz_in_the_list(self):
        pass

    def a_student_has_a_quiz_in_p1_state(self, p1 = "p1"):
        pass

    def he_sees_that_quiz_in_the_list(self):
        pass

    def a_student_has_a_quiz_in_progress(self):
        pass

    def the_teacher_deletes_that_quiz(self):
        pass

    def the_student_goes_to_progress_page(self):
        pass

    def he_no_longer_sees_the_quiz_displayed_in_the_list(self):
        pass

    def a_cond_logs_in(self, p1 = ""):
        pass

    def he_goes_to_p2(self, p2 = ""):
        pass

    def p3_adas(self, p3 = ""):
        pass

    def a_p1_on_qb__create_tab(self, p1 = ""):
        pass

    def he_can_preview_that_question_content(self):
        pass

    def he_clicks_on_a_p2(self, p2 = "", free_text = "", datatable = "||"):
        pass

    def a_coordadmin_on_qb__create_page(self):
        pass

    def he_clicks_on_author_new_question_button(self):
        pass

    def he_can_create_a_new_question(self):
        pass

    def a_coord(self):
        pass

    def he_clicks_on_the_add_button_from_p4(self, p4 = "p1"):
        pass

    def he_is_able_to_add_questions_to_the_create_quiz_widget(self):
        pass

    def a_coord_on_qb__create_tab(self):
        pass

    def he_adds_a_couple_of_question_to_create_quiz_widget(self):
        pass

    def a_title_to_the_new_quiz(self):
        pass

    def he_clicks_on_save_button(self):
        pass

    def the_quiz_is_created_and_saved_successfully(self):
        pass

    def an_admin_on_qb__create_page(self):
        pass

    def he_has_created_a_new_quiz(self):
        pass

    def he_clicks_on_assign_button_for_that_quiz(self):
        pass

    def assign_popover_is_opened_but_it_shows_no_classes(self):
        pass

    def he_sees_in_the_asssign_popup_a_yellow_text_block_in_the_middle_with_the_text_teachers_select_1_or_more_classes_and_any_of_the_following_options_to_assign_assessments(self, teachers_select_1_or_more_classes_and_any_of_the_following_options_to_assign_assessments = "Teachers select 1 or more classes and any of the following options to assign assessments."):
        pass

    def an_admin_on_qb__create_tab(self):
        pass

    def he_sees_in_the_assign_popup_under_the_first_column_unlock_schedule_a_text_classes_appear_here(self):
        pass

    def he_sees_in_the_assign_popup_assign_button_as_disabled(self):
        pass

    def cancel_button_as_enabled(self):
        pass

    def gi(self):
        pass

    def a_teacher_on_the_page(self, p1 = "p1"):
        pass

    def he_clicks_on_the_user_menu_from_the_top_right_corner(self):
        pass

    def he_sees_teacher_menu_containing_the_following_options_my_account_my_ap_my_courses_sign_out(self):
        pass

    def a_coord_on_the_p1(self, p1 = "p1"):
        pass

    def he_sees_coord_menu_containing_the_following_options_my_account_my_ap_my_courses_sign_out(self):
        pass

    def he_sees_the_student_menu_containing_the_following_options_my_account_my_ap_my_courses_ap_stories_sign_out(self):
        pass

    def a(self):
        pass

    def a_cc_logs_in(self, p1 = ""):
        pass

    def he_goes_to_a_p2_subject_homepage(self, p2 = ""):
        pass

    def he_sees_no_class_widget_displayed(self):
        pass

    def he_sees_the_following_yellow_banner_text_displayed_under_the_welcome_banner_teacher_see_progress_and_results_for_each_class_they_teach_here_once_theyve_been_set_up_in_ap_registration_and_ordering(self):
        pass

    def he_goes_to_p2_page__assign_tab(self, p2 = ""):
        pass

    def he_sees_at_the_top_of_the_tab_the_following_yellow_banner_text_p3(self, p3 = "p3"):
        pass

    def he_opens_assign_popup_by_clicking_on_the_assign_button(self):
        pass

    def a_p1_on_p2_page__assign_tab(self, p1 = "", p2 = "p2"):
        pass

    def he_sees_under_the_3_classes_columns_the_following_yellow_banner_text_p3(self, p3 = "p3"):
        pass

    def a_p1_on_p3__assign_tab(self, p1 = "", p3 = "p3"):
        pass

    def he_can_preview_that_quiz_content(self):
        pass

    def a_p1(self, p1 = "p1"):
        pass

    def an_info_text_is_displayed_in_gray_italics_in_the_first_assignment_column_classes_appear_here(self):
        pass

    def he_goes_to_p2_page__progress_tab(self, p2 = ""):
        pass

    def he_sees_at_the_top_of_the_tab_the_following_yellow_banner_text_after_teachers_assign_assessments_they_monitor_student_progress_and_score_submissions_here(self):
        pass

    def no_assignments_are_listed_on_this_page(self):
        pass

    def a_message_text_is_displayed_there_are_no_assignments_in_progress(self):
        pass

    def a_student_logs_into_from_a_mobile_device(self):
        pass

    def he_goes_to_assessments__results_page(self):
        pass

    def he_sees_for_all_the_quizzes_the_correct_start_date(self):
        pass

    def he_sees_all_the_quizzes_for_which_he_has_results_available_displayed_with_a_clickable_title_without_being_called_title(self):
        pass

    def he_sees_for_all_the_quizzes_the_correct_due_date(self):
        pass

    def he_sees_in_black_the_time_limit_since_the_time_taken_was_smaller_than_the_time_limit(self):
        pass

    def a_student_submits_a_quiz_withint_the_time_limit_set_for_it(self):
        pass

    def a_student_submits_a_quiz_outside_the_time_limit_set_for_it(self):
        pass

    def he_sees_in_orange_the_time_limit_since_the_time_taken_was_higher_than_the_time_limit(self):
        pass

    def a_student_submits_a_quiz(self):
        pass

    def that_quiz_is_scored(self):
        pass

    def the_student_goes_to_assessments__results_page(self):
        pass

    def he_sees_the_same_performance_bar_as_in_desktop_view_with_the_correct_results_he_has_obtained(self):
        pass

    def a_p1_subject_homepage(self, p1 = "p1"):
        pass

    def he_navigates_to_p2_page__results_tab(self, p2 = ""):
        pass

    def he_sees_all_the_assignments_result_for_all_teachers_in_their_schools_for_that_subject(self):
        pass

    def a_teacher_on_p1_page(self, p1 = ""):
        pass

    def he_opens_the_preview_of_a_quiz(self):
        pass

    def that_quiz_contains_a_question_tagged_with_calculator_active__required_or_allowed(self, calculator_active = "Calculator Active", required = "Required"):
        pass

    def he_p3_the_calculator_icon_to_the_right_side_of_the_question_title(self, p3 = "p3"):
        pass

    def that_quiz_contains_a_question_tagged_with_calculator_active__p2(self, p2 = ""):
        pass

    def a_teacher_on_question_bank__create_tab(self):
        pass

    def he_opens_the_preview_of_a_question(self):
        pass

    def that_question_is_tagged_with_calculator_active__p2(self, p2 = ""):
        pass

    def a_student_on_p1_page(self, p1 = "p1"):
        pass

    def he_p4_that_contains_a_question_tagged_with_calculator_active__p2(self, p2 = "", p4 = "p4"):
        pass

    def he_sees_a_district_school_class_filter_displayed_above_the_regular_filters(self):
        pass

    def a_teacher_on_results_tab_of_progress_check_page(self):
        pass

    def he_navigates_to_results_tab_of_progress_check_qb_page(self):
        pass

    def he_does_not_see_any_district_school_class_filter_displayed_above_the_regular_filters(self):
        pass

    def a_coord_on_the_homepage_of_a_subject(self):
        pass

    def he_does_not_see_any_student_filter_displayed_above_the_regular_filters_nor_under_class_filter(self):
        pass

    def an_admin_on_the_homepage_of_a_subject(self):
        pass

    def he_does_not_see_in_the_school_filter_groups_that_dont_have_classes_for_the_selected_subject(self):
        pass

    def an_admin_on_the_homepage_of_a_subject_that_has_results_and_classes_available_only_from_a_single_district(self):
        pass

    def he_sees_the_district_filter_preselected_with_the_only_available_district_option(self):
        pass

    def an_coord_on_the_homepage_of_a_subject_that_has_results_and_classes_available_only_from_a_single_school(self):
        pass

    def he_sees_the_school_filter_preselected_with_the_only_available_school_option(self):
        pass

    def an_coord_on_the_homepage_of_a_subject_that_has_only_one_class_available(self):
        pass

    def he_sees_the_class_filter_preselected_with_the_only_available_class_option(self):
        pass

    def a_coord_on_the_homepage_of_a_subject_that_has_results_and_classes_available_from_multiple_districts(self):
        pass

    def he_sees_the_district_filter_preselected_with_the_first_district_in_alphabetical_order(self):
        pass

    def a_coord_on_the_homepage_of_a_subject_that_has_results_and_classes_available_from_multiple_schools(self):
        pass

    def he_sees_the_school_filter_preselected_with_all_schools_option(self):
        pass

    def a_coord_on_the_homepage_of_a_subject_that_has_results_and_multiple_classes_available(self):
        pass

    def he_sees_the_class_filter_preselected_with_all_classes_option(self):
        pass

    def a_coord_on_the_results_tab_of_qb_page(self):
        pass

    def there_are_multiple_schools_available_in_the_school_filter(self):
        pass

    def the_coord_selects_all_schools_from_school_filter(self):
        pass

    def the_filter_displayed_all_the_results_from_all_the_schools_available_for_that_user(self):
        pass

    def in_groups_column_class_nameschool_name_are_displayed(self):
        pass

    def a_p1_on_the_results_tab_of_p2_page(self, p1 = "p1", p2 = "p2"):
        pass

    def the_user_selects_a_p3_from_p3_filter(self, p3 = "p3"):
        pass

    def the_page_is_filtered_accordingly(self):
        pass

    def a_student_on_assessments__results_page_opened_from_a_mobile_device_on_portrait_view(self):
        pass

    def he_clicks_on_part_a_to_display_its_results(self):
        pass

    def there_are_2_parts_connected_through_the_same_unit_part_a_has_results_and_part_b_is_locked__p1(self, p1 = "p1"):
        pass

    def he_sees_part_block_icon_locked_label_in_a_card_beneath_the_performance_summary_for_the_part_a_at_the_top_of_the_page_and_at_the_bottom_of_the_page_after_all_the_tag_pairs_are_displayed(self, card = "card"):
        pass

    def there_are_2_parts_connected_through_the_same_unit_part_a_has_results_and_part_b_is_unlocked__not_started(self):
        pass

    def he_sees_part_b_begin_cta_in_a_card_beneath_the_performance_summary_for_the_part_a_at_the_top_of_the_page_and_at_the_bottom_of_the_page_after_all_the_tag_pairs_are_displayed(self, card = "card"):
        pass

    def there_are_2_parts_connected_through_the_same_unit_part_a_has_results_and_part_b_is_unlocked__started(self):
        pass

    def he_sees_part_b_continue_cta_in_a_card_beneath_the_performance_summary_for_the_part_a_at_the_top_of_the_page_and_at_the_bottom_of_the_page_after_all_the_tag_pairs_are_displayed(self, card = "card"):
        pass

    def there_are_2_parts_connected_through_the_same_unit_part_a_has_results_and_part_b_is_awaiting_results_teacher_has_not_made_results_visible_to_students(self):
        pass

    def he_sees_part_b_awaiting_results_label_in_a_card_beneath_the_performance_summary_for_the_part_a_at_the_top_of_the_page_and_at_the_bottom_of_the_page_after_all_the_tag_pairs_are_displayed(self, card = "card"):
        pass

    def there_are_2_parts_connected_through_the_same_unit_part_a_has_results_and_part_b_is_awaiting_results_currently_being_autoscored(self):
        pass

    def he_sees_part_b_refresh_for_results_cta_in_a_card_beneath_the_performance_summary_for_the_part_a_at_the_top_of_the_page_and_at_the_bottom_of_the_page_after_all_the_tag_pairs_are_displayed(self, card = "card"):
        pass

    def there_are_2_parts_connected_through_the_same_unit_part_a_has_results_and_part_b_is_scored__p1(self, p1 = "p1"):
        pass

    def he_sees_part_b_view_results_cta_in_a_card_beneath_the_performance_summary_for_the_part_a_at_the_top_of_the_page_and_at_the_bottom_of_the_page_after_all_the_tag_pairs_are_displayed(self, card = "card"):
        pass

    def he_sees_all_the_tag_pairs_linked_to_part_a_and_part_b_in_alphabetical_order_as_cards_tag_pairs_for_part_a_having_scores(self):
        pass

    def tag_pairs_for_part_b_having_a_lock_icon_on_grey_background(self):
        pass

    def tag_pairs_for_part_b_having_an_unlock_icon_on_grey_background(self):
        pass

    def tag_pairs_for_part_b_have_a_label_in_progress_on_grey_background(self):
        pass

    def tag_pairs_for_part_b_having_a_label_awaiting_results_on_grey_background(self):
        pass

    def tag_pairs_for_part_b_having_the_correct_score_on_the_correct_performance_colored_bar(self):
        pass

    def he_goes_to_assessments__assign_tab(self):
        pass

    def he_sees_all_the_autoassigned_quizzes_having_the_following_columns_available_p3(self, p3 = "p3"):
        pass

    def sees_the_same_p3_as_on_desktop(self, p3 = "p3"):
        pass

    def he_goes_to_assessments__progress_tab(self):
        pass

    def he_sees_the_all_the_assignments_displayed_on_individual_cards_having_all_the_informations_as_on_desktop_title_start_date_due_time_limit_status_action(self):
        pass

    def he_sees_all_the_autoassigned_quizzes_having_the_following_informations_available_title_start_date_due_time_limit_status_action(self):
        pass

    def a_p2_on_the_homepage_of_a_subject_with_a_unit_on_display(self, p2 = "p2"):
        pass

    def he_navigatesto_another_page_of_the_site_eg_progress_checks_question_bank(self):
        pass

    def he_logs_out_closes_the_browser(self):
        pass

    def then_opens_the_browser_and_logs_in_with_the_same_username_on_the_same_device(self):
        pass

    def a_multiple_subjects_p1_on_the_homepage_of_a_subject_with_a_unit_on_display(self, p1 = "p1"):
        pass

    def then_opens_the_browser_and_logs_in_with_the_same_username_on_a_different_device(self):
        pass

    def he_does_not_see_the_last_unit_accessed_on_the_first_device(self):
        pass

    def he_logs_out_from_the_browser__close_it__opens_it_again__logs_in_with_the_same_username_on_the_same_device(self):
        pass

    def navigates_back_to_each_subject_homepage(self):
        pass

    def user_a_on_the_homepage_of_a_subject_with_a_unit_on_display_logs_out_from_that_browser(self):
        pass

    def he_logs_out_from_that_browser(self):
        pass

    def another_user_b_logs_in_on_the_same_browser_device(self):
        pass

    def access_a_different_unit(self):
        pass

    def that_user_b_logs_out_from_that_browserdevice_pair(self):
        pass

    def user_a_logs_back_in(self):
        pass

    def he_sees_the_last_unit_tab_accessed_on_display_for_each_subject_along_its_content(self):
        pass

    def he_navigates_to_another_page_of_the_site_eg_progress_checks_question_bank(self):
        pass

    def a_p1_on_the_qb_page_create_tab(self, p1 = "p1"):
        pass

    def he_clicks_on_the_preview_button_of_a_p2_quiz_just_created_and_saved(self, p2 = "p2"):
        pass

    def he_clicks_on_scoring_guide_button(self):
        pass

    def a_teacher_on_qb_page_create_tab(self):
        pass

    def he_clicks_on_the_preview_button_of_a_quiz_just_created_and_saved(self):
        pass

    def he_sees_a_scoring_guide_button(self):
        pass

    def he_does_not_see_scoring_guide_button_in_the_preview_form(self):
        pass

    def a_p1_on_qb_page_create_tab(self, p1 = "p1"):
        pass

    def teacher_lands_on_the_course_homepage_and_sees_p1_in_the_page_header(self, p1 = ""):
        pass

    def teacher_navigates_to_progress_checks_page(self):
        pass

    def the_teacher_is_able_to_see_the_assign_button_for_a_progress_check(self):
        pass

    def a_teacher_on_assign_tab_from_progress_checks_page(self):
        pass

    def clicks_assign_button_for_a_progress_check(self):
        pass

    def the_quiz_player_is_displayed(self):
        pass

    def he_is_able_to_click_submit_button(self):
        pass

    def make_sure_you_have_at_least(self, free_text = ""):
        pass

    def teacher_navigates_to_progress_checks_progress_tab(self):
        pass

    def coord_1_login_to_ap_classroom(self):
        pass

    def clicks_on_modify_selections(self):
        pass

    def pre_ap_final_exam_administration_model_is_displayed(self):
        pass

    def coord_1_clicks_on_opt_out_for_one_subject(self):
        pass

    def subject_row_is_disabled(self):
        pass

    def coord_1_deselect_opt_out(self):
        pass

    def subject_row_is_enabled(self):
        pass

    def coord_belongs_to_one_school(self):
        pass

    def coord_clicks_on_modify_selection_on_home_page_of_ap_classroom(self):
        pass

    def pre_ap_final_exam_model_is_displayed_with_no_selctions(self):
        pass

    def wh(self):
        pass

    def coord_opt_out_from_one_subject(self):
        pass

    def click_submit(self):
        pass

    def coord_is_displayed_with_confirmation_message(self, free_text = ""):
        pass

    def coord_click_cancel(self):
        pass

    def coord_is_taken_back_to_the_modal(self):
        pass

    def coord_submit_again(self):
        pass

    def click_on_optout(self):
        pass

    def coord_is_taken_back_to_the_home_page_with_the_banner_showing(self):
        pass

    def teacher_is_not_shown_the_final_exam_on_the_assignment_page(self):
        pass

    def in_database_the_correct_preference_is_saved(self):
        pass

    def coord_opt_out_from_final_exam(self):
        pass

    def coord_clicks_on_modify_selection(self):
        pass

    def deselect_opt_out(self):
        pass

    def the_subject_row_is_not_disabled(self):
        pass

    def coord_select_exam(self):
        pass

    def clicks_submit(self):
        pass

    def coord_is_take_to_the_home_page(self):
        pass

    def the_selection_is_updated_in_the_database(self, free_text = ""):
        pass

    def preference_is_not_saved_in_the_db(self):
        pass

    def tester_change_registration_start_date_in_db_to_start_date(self, start_date = "Start Date"):
        pass

    def coord_login(self):
        pass

    def modify_banner_will_be_result(self, result = "Result"):
        pass

    def coord_assign_an_exam(self):
        pass

    def click_on_opt_out(self):
        pass

    def the_exam_is_deselected_and_only_opt_out_is_selected(self):
        pass

    def the_subject_row_is_disabled(self):
        pass

    def coord_clicks_submit(self):
        pass

    def coord_belongs_to_two_schools(self):
        pass

    def coord_clicks_on_modify_banner(self):
        pass

    def model_with_the_coord_school_is_shown(self):
        pass

    def coord_clicks_on_the_plus_sign(self):
        pass

    def the_school_final_exam_preference_is_shown_to_the_user(self):
        pass

    def coord_opt_out_from_an_exam_for_one_of_the_school(self):
        pass

    def coord_is(self):
        pass

    def coord(self):
        pass

    def coord_clicks_opt_out(self):
        pass

    def coord_is_taken_back_to_the_model_window(self):
        pass

    def submit_changes_to_modify(self):
        pass

    def coord_clicks_on_the_second_school(self):
        pass

    def the_button_shows_as_submit_and_greyed_out(self):
        pass

    def coord_opt_out_from_exam_for_a_course_for_one_school(self):
        pass

    def coord_clicks_on_modify_banner(self):
        pass

    def clicks_on_modify_for_school(self):
        pass

    def deselect_opt_out(self):
        pass

    def select_exam(self):
        pass

    def modify_button_is_displayed(self):
        pass

    def database_is_updated(self):
        pass

    def coord_click_on_submit_when_opt_out_from_final_exam(self):
        pass

    def coord_clicks_on_cancel(self):
        pass

    def coord_is_taken_back_to_selection_model(self):
        pass

    def coord_dismiss_the_selection_model(self):
        pass

    def clicks_on_modify_button_on_banner(self):
        pass

    def the_pervious_selection_is_not_saved(self):
        pass

    def coord_select_different_preference(self, datatable = "||"):
        pass

    def coord_logout(self):
        pass

    def login(self):
        pass

    def final_exam_preference_is_persisted(self):
        pass

    def coordinate_belongs_to_one_school(self):
        pass

    def coord_is_displayed_with_model_to_select_perference(self):
        pass

    def coord_opt_out_from_an_exam_for_a_subject(self):
        pass

    def this_subject_row_is_diabled(self):
        pass

    def coord_clicks_on_submit(self):
        pass

    def select_opt_out_for_all_other_subjects(self):
        pass

    def coord_is_displayed_with_confirmation_message_with_the_subject_names(self):
        pass

    def deselect_opt_out_for_the_subject_selected_before(self):
        pass

    def coord_modify_selection_for_an_already_opt_out_subject(self):
        pass

    def coord_select_winter_exam(self):
        pass

    def coord_is_taken_back_to_the_home_page(self):
        pass

    def coord_assign_a_final_exam_for_a_subject(self):
        pass

    def coord_opt_out_from_exam(self):
        pass

    def coord_is_displayed_with_confirmation_message_for_this_subject(self):
        pass

    def coord_is_taken_back_to_home_page(self):
        pass

    def coord_select_preference_for_final_exam(self, datatable = "||"):
        pass

    def coord_clears_browser_cache(self):
        pass

    def click_on_modify(self):
        pass

    def information_is_persisted(self):
        pass

    def coord_belongs_to_two_school(self):
        pass

    def model_is_displayed_with_two_school_name(self):
        pass

    def coord_clicks_on_plus_sign(self):
        pass

    def final_exam_preference_is_displayed_to_the_user(self):
        pass

    def coord_clicks_on_opt_out_for_one_subject(self):
        pass

    def confirmation_message_is_displayed(self, free_text = ""):
        pass

    def coord_confirms_the_dialog(self):
        pass

    def coord_is_taken_back_to_the_model(self):
        pass

    def submit_button_is_now_modify(self):
        pass

    def coord_is_taken_back_to_the_selection_model(self):
        pass

    def feature_flag_is_turned_on(self):
        pass

    def coord_logins_in(self):
        pass

    def coord_is_able_to_see_the_the_model_for_exam_preference(self):
        pass

    def can_see_the_modify_banner(self):
        pass

    def feature_flag_is_turned_off(self):
        pass

    def coord_can_not_see_the_model(self):
        pass

    def coord_can_not_see_modify_banner(self):
        pass

    def teacher_does_not_see_exam_for_this_subject(self):
        pass

    def teacher_is_enrolled_in_a_subject(self):
        pass

    def teacher_is_enrolled_in_the_subject(self):
        pass

    def teacher_see_exam_for_winter(self):
        pass

    def teacher_does_not_see_the_exam_anymore(self):
        pass

    def there_are_two_teachers_enrolled_in_subject_one_for_each_school(self):
        pass

    def teacher_does_not_see_the_final_exam_in_the_assignment_tab(self):
        pass

    def two_teachers_are_enrolled_in_a_subjects_each_one_of_the_teacher_is_at_different_school(self):
        pass

    def teachers_do_not_see_the_exam_anymore(self):
        pass

    def there_is_a_teacher_enrolled_in_all_subjects(self):
        pass

    def teacher_see_the_correct_exam_for_each_subject(self, datatable = "||"):
        pass

    def each_teacher_sees_the_correct_administrated_final_exam(self, datatable = "||", free_text = ""):
        pass

    def there_a_teacher_at_each_school_enrolled_in_all_subjects(self):
        pass

    def teacher_is_administered_to_see_final_exam(self):
        pass

    def teacher_go_to_assignment_tab(self):
        pass

    def click_on_filter_by_exam(self):
        pass

    def the_correct_exam_is_shown(self):
        pass

    def a_quiz_has_at_least_3_questions(self):
        pass


    def teacher_clicks_on(self):
        pass

    def connection_card_is_show_on_top_with_reportable_skill(self):
        pass

    def number_of_questions(self):
        pass

    def the_average_of_the_class(self):
        pass



    def teacher_navigate_to_assign_tab(self):
        pass

    def preview_button_is_not_displayed(self):
        pass

    def teacher_navigate_to_progress_tab(self):
        pass

    def quiz_title_is_black_and_not_clickable(self):
        pass

    def a_navigates_to_progress_checks__results_page_for_part_b_assignment_(self):
        pass

    def he_sees_inside_the_table_in_part_a_column_the_label_not_assigned_for_all_the_rows_linked_to_that_part_a_assignment(self):
        pass

    def also_the_same_cta_above_the_column(self):
        pass


    def the_teacher_navigates_to_progress_checks__results_page_for_part_b_assignment__topic_and_skills_table(self):
        pass

    def clicks_on_the_not_assigned_cta_from_part_a_column_title(self):
        pass

    def assign_modal_opens_displaying(self):
        pass