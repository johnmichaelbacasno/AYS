$(function() {
  $('#table').bootstrapTable({
    data: [
      {
        'service_id': 0,
        'service_title': 'Marks Spa',
        'service_description': 'I love to read, hang out with friends, watch football, listen to music, and learn new things.',
        'service_user_id': 0,
        'service_user_rating': 5,
        'service_user_level': 1,
        'service_user_is_trusted': true,
        'service_date_posted': '2021-12-25',
        'service_schedule': '2021-12-25',
        'service_location': 'Iligan City',
        'service_type': 'Beauty',
        'service_category': 'Spa and Salon',
        'service_amount': 500
      }
    ]
  })
})

function customViewFormatter (data) {
  var template = $('#profileTemplate').html();
  var view = '';

  $.each(data, function (i, row) {
    var stars = ''
    for (i = 0; i < row.service_user_rating; i++) {
      stars += '<span class="fa fa-star"></span> ';
    }

    var trusted = ''
    if (row.service_user_is_trusted) {
      trusted = '<span class="badge badge-info tags">Trusted</span>';
    }
    else {
      trusted = '';
    }

    view += template.replace('%TITLE%', row.service_title)
      .replace('%DESCRIPTION%', row.service_description)
      .replace('%USER_ID%', row.service_user_id)
      .replace('%USER_RATING%', stars)
      .replace('%USER_LEVEL%', row.service_user_level)
      .replace('%USER_IS_TRUSTED%', trusted)
      .replace('%DATE_POSTED%', row.service_date_posted)
      .replace('%SCHEDULE%', row.service_schedule)
      .replace('%LOCATION%', row.service_location)
      .replace('%TYPE%', row.service_type)
      .replace('%CATEGORY%', row.service_category)
      .replace('%AMOUNT%', row.service_amount);
  })

  return `<div class="row mx-0">${view}</div>`;
}