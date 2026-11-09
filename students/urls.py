
from django.urls import path

from . import views
from . import api_views


urlpatterns = [

    # --------------------------------
    # HOME PAGE
    # --------------------------------

    path(
        "",
        views.home,
        name="home"
    ),

    # --------------------------------
    # STUDENT WEB PAGES
    # --------------------------------

    path(
        "students/",
        views.student_list,
        name="student_list"
    ),

    path(
        "students/register/",
        views.student_register,
        name="student_register"
    ),

    # --------------------------------
    # STUDENT APIs - PUBLIC ACCESS
    # --------------------------------

    # GET: Display all students
    path(
        "api/students/",
        api_views.student_list_api,
        name="student_list_api"
    ),

    # POST: Create a student
    path(
        "api/students/create/",
        api_views.student_create_api,
        name="student_create_api"
    ),

    # DELETE: Delete a student
    path(
        "api/students/<int:student_id>/delete/",
        api_views.student_delete_api,
        name="student_delete_api"
    ),

    # --------------------------------
    # LOGIN AND LOGOUT
    # --------------------------------

    path(
        "login/",
        views.user_login,
        name="user_login"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "logout/",
        views.user_logout,
        name="user_logout"
    ),

    # --------------------------------
    # SESSION EXAMPLES
    # --------------------------------

    path(
        "save-student-name/",
        views.save_student_name,
        name="save_student_name"
    ),

    path(
        "show-student-name/",
        views.show_student_name,
        name="show_student_name"
    ),

    # --------------------------------
    # PROTECTED API
    # --------------------------------

    path(
        "api/protected/",
        views.protected_view,
        name="protected_view"
    ),

]
