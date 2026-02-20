from django.apps import AppConfig


class TeacherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "teacher"

    # ✅ Auto load signals when app starts
    def ready(self):
        try:
            import teacher.signals
        except ImportError:
            pass
