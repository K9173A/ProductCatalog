/**
 * Displays form with data.
 * @param form - form object.
 * @param data - html data to be used to fill the form.
 */
const initForm = (form, data) => {
  // Inserts form fields into the <form>
  form.html(data.form_html);
  // Creates special widget for the date field of the form
  form.find('[name="date"]').datepicker({
    format: 'yyyy-mm-dd',
    uiLibrary: 'bootstrap4'
  });
};

$(function () {
  // Sends form for the creation of a new item.
  // If successful, renews list of items.
  $('#add-button').on('click', function () {
    let modal = $(this).parents('.modal').first();
    let form = modal.find('form');
    $.post(
      form.attr('action'),
      form.serialize(),
      data => {
        if (data.form_is_valid) {
          $('table tbody').html(data.products_html);
          modal.modal('toggle');
        }
        else {
          initForm(form, data)
        }
      });
  });

  // Shows item creation modal window
  $('#modal').on('show.bs.modal', function () {
    let form = $(this).find('form');
    $.get(form.attr('action'), data => initForm(form, data));
  });
});
