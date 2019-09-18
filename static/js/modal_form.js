$(function () {
  $('.js-create-product').click(function () {
    $.ajax({
      url: $(this).attr('data-url'),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $('#modal-product').modal('show');
      },
      success: function (data) {
        $('#modal-product .modal-content').html(data.html_form);
      }
    });
  });

  $('#modal-product').on('submit', '.js-product-create-form', function () {
    $.ajax({
      url: $(this).attr('action'),
      data: $(this).serialize(),
      type: $(this).attr('method'),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $('#product-table tbody').html(data.html_product_list);
          $('#modal-product').modal('hide');
        }
        else {
          $('#modal-product .modal-content').html(data.html_form);
        }
      }
    });
    return false;
  });
});