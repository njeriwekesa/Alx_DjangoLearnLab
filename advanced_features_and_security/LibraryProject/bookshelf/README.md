# Managing Permissions and Groups in Django

This project demonstrates how to implement role-based access control in Django using **custom permissions** and **groups**. Permissions are defined at the model level and assigned to user groups, which are then enforced in views.

---

## 1. Custom Permissions

Custom permissions are defined in the `bookshelf` app within `models.py`.

Example permissions added to the `Book` model:

- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

These permissions represent allowed actions on Book objects and are created automatically when migrations are applied.

---

## 2. Groups Configuration

User access is managed using Django groups. The following groups are created using the Django admin interface:

### Viewers
- `can_view`

### Editors
- `can_view`
- `can_create`
- `can_edit`

### Admins
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

Permissions are assigned to groups rather than individual users to simplify access control and follow best practices.

---

## 3. Assigning Users to Groups

Users are assigned to groups through the Django admin panel:

- Navigate to **Admin → Users**
- Select a user
- Assign one or more groups under the *Groups* section
- Save changes

Users inherit permissions based on their group membership.

---

## 4. Enforcing Permissions in Views

Permissions are enforced in views using Django’s `@permission_required` decorator.

Example:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...
