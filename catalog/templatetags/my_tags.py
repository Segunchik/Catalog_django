from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"

@register.filter(name='has_group')
def has_group(user, group_name):
    """Проверяет, принадлежит ли пользователь к указанной группе"""
    if not user or not user.is_authenticated:
        return False
    return user.groups.filter(name=group_name).exists()
