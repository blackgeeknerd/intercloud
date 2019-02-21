 var deleteBut = function()
{
   var parent = document.getElementsByClassName("tes");
   var child = document.getElementById("demo");
   console.log('delete');
   parent.removeChild(child);
   //child.parentNode.removeChild(child);
   console.log('deleted');
}

