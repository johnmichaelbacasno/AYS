$(function() {
  $('#table').bootstrapTable({
    data: [
      {
        'name': 'Mike',
        'image': 'https://robohash.org/68.186.255.198.png',
        'follower': 10,
        'following': 123,
        'snippets': 12
      },
      {
        'name': 'Tim',
        'image': 'https://robohash.org/18.146.255.198.png',
        'follower': 70,
        'following': 23,
        'snippets': 42
      },
      {
        'name': 'Jorge',
        'image': 'https://robohash.org/63.186.255.198.png',
        'follower': 40,
        'following': 74,
        'snippets': 567
      },
      {
        'name': 'Luke',
        'image': 'https://robohash.org/68.186.155.198.png',
        'follower': 550,
        'following': 23,
        'snippets': 52
      },
      {
        'name': 'Mike',
        'image': 'https://robohash.org/68.186.255.198.png',
        'follower': 10,
        'following': 123,
        'snippets': 12
      },
      {
        'name': 'Tim',
        'image': 'https://robohash.org/18.146.255.198.png',
        'follower': 70,
        'following': 23,
        'snippets': 42
      },
      {
        'name': 'Jorge',
        'image': 'https://robohash.org/63.186.255.198.png',
        'follower': 40,
        'following': 74,
        'snippets': 567
      },
      {
        'name': 'Luke',
        'image': 'https://robohash.org/68.186.155.198.png',
        'follower': 550,
        'following': 23,
        'snippets': 52
      },
      {
        'name': 'Mike',
        'image': 'https://robohash.org/68.186.255.198.png',
        'follower': 10,
        'following': 123,
        'snippets': 12
      },
      {
        'name': 'Tim',
        'image': 'https://robohash.org/18.146.255.198.png',
        'follower': 70,
        'following': 23,
        'snippets': 42
      },
      {
        'name': 'Jorge',
        'image': 'https://robohash.org/63.186.255.198.png',
        'follower': 40,
        'following': 74,
        'snippets': 567
      },
      {
        'name': 'Luke',
        'image': 'https://robohash.org/68.186.155.198.png',
        'follower': 550,
        'following': 23,
        'snippets': 52
      },
      {
        'name': 'Mike',
        'image': 'https://robohash.org/68.186.255.198.png',
        'follower': 10,
        'following': 123,
        'snippets': 12
      },
      {
        'name': 'Tim',
        'image': 'https://robohash.org/18.146.255.198.png',
        'follower': 70,
        'following': 23,
        'snippets': 42
      },
      {
        'name': 'Jorge',
        'image': 'https://robohash.org/63.186.255.198.png',
        'follower': 40,
        'following': 74,
        'snippets': 567
      },
      {
        'name': 'Luke',
        'image': 'https://robohash.org/68.186.155.198.png',
        'follower': 550,
        'following': 23,
        'snippets': 52
      }
    ]
  })
})

function customViewFormatter (data) {
  var template = $('#profileTemplate').html()
  var view = ''
  $.each(data, function (i, row) {
    view += template.replace('%NAME%', row.name)
      .replace('%IMAGE%', row.image)
      .replace('%FOLLOWER%', row.follower)
      .replace('%FOLLOWING%', row.following)
      .replace('%SNIPPETS%', row.snippets);
  })

  return `<div class="row mx-0">${view}</div>`
}