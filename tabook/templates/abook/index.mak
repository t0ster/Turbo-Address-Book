<%inherit file="local:templates.master"/>

<%def name="title()">
  Address Book - Cards
</%def>

<%def name="extra_head()">
  <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/toscawidgets/resources/tw.forms/static/grid.css')}" />
</%def>

<div id="main_content">
  <div style="float:left; width:80%">
    <h1 style="margin-top:1px;">Listing Cards</h1>

    <div style="margin:1ex 0; width:90%">
      <form>
        <input type="text" />
        <input type="submit" value="Search">
      </form>
    </div>

    <div style="margin:1ex 0; width:90%">
      <a href='${url("/abook/new")}' class="add_link">New record</a>
    </div>

    <div class="crud_table" style="height:50%; width:90%">
      <table class="grid">
         <thead>
            <tr>
              <th class="col_0">actions</th>
              <th class="col_1">name</th>
              <th class="col_2">email address</th>
            </tr>
          </thead>
          <tbody>
            <tr class="even">
              <td class="col_0">
                <div><div><a class="edit_link" href="1/edit" style="text-decoration:none">edit</a></div><div><form method="POST" action="1" class="button-to"><input type="hidden" name="_method" value="DELETE" /><input class="delete-button" onclick="return confirm('Are you sure?');" value="delete" type="submit" style="background-color: transparent; float:left; border:0; color: #286571; display: inline; margin: 0; padding: 0;"/></form></div></div>
              </td>
              <td class="col_1">Larry Smith</td>
              <td class="col_2">larryr@somedomain.com</td>
            </tr>
          </tbody>
      </table>
    </div>
  </div>
</div>
<div style="clear:both;"/>
