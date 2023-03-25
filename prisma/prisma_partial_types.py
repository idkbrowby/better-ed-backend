from prisma.models import User

User.create_partial(
    "UserInLogin_",
    include={
        "username",
        "password",
    },
)

User.create_partial("UserProfile", include={"id", "username", "email", "created_at"})