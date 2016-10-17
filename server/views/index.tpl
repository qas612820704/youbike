<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>YouBike Data</title>
</head>
<body>
  <ul>
    % for json in json_list:
      <li>
        <a href="/{{json}}/">{{json}}</a>
        <span>&nbsp;&nbsp;&nbsp;</span>
        <a href="/{{json}}.json"><i>(view source json)</i></a>
      </li>
    % end
  </ul>
</body>
</html>
