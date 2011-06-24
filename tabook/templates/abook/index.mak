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
        <label>Search by phone number
        <input type="text" name="phone_number" />
        </label>
        <input type="submit" value="Search">
      </form>
    </div>

    <a href='${url("/abook/new")}' class="add_link">Add Card</a>
      ${tmpl_context.table}
  </div>
  <div style="clear:both;"/>
</div>
