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
  let deleteItemUrl = null;

  // Sends form for the creation of a new item.
  // If successful, renews list of items.
  $('#add-button').on('click', function () {
    let modal = $('#modal-create-product');
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

  // Sends request to the server to delete selected item.
  // If successful, renews list of items.
  $('#delete-button').on('click', function () {
    $.ajax({
      url: deleteItemUrl,
      success: function (data) {
        $('table tbody').html(data.products_html);
        $('#modal-confirm-delete').modal('toggle');
      }
    })
  });

  // Saves url for item deleting when delete button is being pressed.
  $('#product-table').on('click', '.delete-btn', function (event) {
    deleteItemUrl = event.target.dataset.url;
  });

  // Shows item creation modal window.
  $('#modal-create-product').on('show.bs.modal', function () {
    let form = $(this).find('form');
    $.get(form.attr('action'), data => initForm(form, data));
  });
});
