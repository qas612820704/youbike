<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="/static/jquery-jsonview/dist/jquery.jsonview.css">
  <title>YouBike Data</title>
</head>
<body>
  <div id="json-view">

  </div>
  <script src="/static/jquery/dist/jquery.min.js"></script>
  <script src="/static/jquery-jsonview/dist/jquery.jsonview.js"></script>
  <script>
    $.getJSON('/{{json_file}}', function(json) {
      $('#json-view').JSONView(json);
    })
  </script>
</body>
</html>
