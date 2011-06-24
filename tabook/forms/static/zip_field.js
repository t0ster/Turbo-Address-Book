(function($) {
  // Validates zip fields
  // Call `zip_validator.validate()` to validate
  var zip_validator = new function () {
    this.validate = function() {
      var valid = true;
      $(".zipfield").each(function(index, element) {
        var ul = $(element).parent().parent();
        if (!all_child_fields_are_empty(ul)) {
          $(element).parent().find(".fielderror").remove();
          if (!validate_zip_field(element)) {
            valid = false;
            $(element).parent().append('<span class="fielderror">Invalid ZIP Code</span>');
          }
        }
      });
      return valid;
    };

    var validate_zip_field = function(element) {
      if (!(valid_zip_codes.indexOf(element.value) == -1))
        return true;
      return false;
    };

    var all_child_fields_are_empty = function(element) {
      var empty = true;
      $(element).find("input").each(function(index, _element) {
        if (_element.value)
          empty = false;
      });
      return empty;
    };

    var valid_zip_codes = ["35801", "35802", "35803", "35804", "35805", "35806", "35807", "35808", "35809", "35810", "35811", "35812", "35813", "35814", "35815", "99501", "99502", "99503", "99504", "99505", "99506", "99507", "99508", "99509", "99510", "99511", "99512", "99513", "99514", "99515", "99516", "99517", "99518", "99519", "99520", "99521", "99522", "99523", "85001", "85002", "85003", "85004", "85005", "85006", "85007", "85008", "85009", "85010", "85011", "85012", "85013", "85014", "85015", "85016", "85017", "85018", "85019", "85020", "85021", "85022", "85023", "85024", "85025", "85026", "85027", "85028", "85029", "85030", "85031", "85032", "85033", "85034", "85035", "85036", "85037", "85038", "85039", "85040", "85041", "85042", "85043", "85044", "85045", "85046", "85047", "85048", "85049", "85050", "85051", "85052", "85053", "85054", "72201", "72202", "72203", "72204", "72205", "72206", "72207", "72208", "72209", "72210", "72211", "72212", "72213", "72214", "72215", "72216", "94203", "94204", "94205", "94206", "94207", "94208", "90001", "90002", "90003", "90004", "90005", "90006", "90007", "90008", "90009", "90010", "90011", "90012", "90013", "90014", "90015", "90016", "90017", "90018", "90019", "90020", "90021", "90022", "90023", "90024", "90025", "90026", "90027", "90028", "90029", "90030", "90031", "90032", "90033", "90034", "90035", "90036", "90037", "90038", "90039", "90040", "90041", "90042", "90043", "90044", "90045", "90046", "90047", "90048", "90049", "90050", "90051", "90052", "90053", "90054", "90055", "90056", "90057", "90058", "90059", "90060", "90061", "90062", "90063", "90064", "90065", "90066", "90067", "90068", "90069", "90070", "90071", "90072", "90073", "90074", "90075", "90076", "90077", "90078", "90079", "90080", "90081", "90082", "90083", "90084", "90085", "90086", "90087", "90088", "90209", "90210", "90211", "90212", "80201", "80202", "80203", "80204", "80205", "80206", "80207", "80208", "80209", "80210", "80211", "80212", "80213", "80214", "80215", "80216", "80217", "80218", "80219", "80220", "80221", "80222", "80223", "80224", "80225", "80226", "80227", "80228", "80229", "80230", "80231", "80232", "80233", "80234", "80235", "80236", "80237", "80238", "6101", "6102", "6103", "6104", "6105", "6106", "6107", "6108", "6109", "6110", "6111", "19901", "19902", "19903", "19904", "20001", "20002", "20003", "20004", "20005", "20006", "20007", "20008", "20009", "20010", "20011", "20012", "20013", "20014", "20015", "20016", "20017", "20018", "20019", "32501", "32502", "32503", "32504", "32505", "32506", "32507", "32508", "33124", "33125", "33126", "33127", "33128", "33129", "33130", "33131", "33132", "33133", "33134", "33135", "33136", "33137", "33138", "33139", "33140", "33141", "33142", "33143", "33144", "33145", "33146", "33147", "33148", "33149", "33150", "33151", "33152", "33153", "33154", "33155", "33156", "33157", "33158", "33159", "33160", "33161", "33162", "33163", "33164", "33165", "33166", "33167", "33168", "33169", "33170", "33171", "33172", "33173", "33174", "33175", "33176", "33177", "33178", "33179", "33180", "33181", "33182", "33183", "33184", "33185", "33186", "33187", "33188", "33189", "32801", "32802", "32803", "32804", "32805", "32806", "32807", "32808", "32809", "32810", "32811", "32812", "32813", "32814", "32815", "32816", "32817", "32818", "32819", "32820", "32821", "32822", "32823", "32824", "32825", "32826", "32827", "32828", "32829", "32830", "32831", "32832", "32833", "32834", "32835", "32836", "30301", "30302", "30303", "30304", "30305", "30306", "30307", "30308", "30309", "30310", "30311", "30312", "30313", "30314", "30315", "30316", "30317", "30318", "30319", "30320", "30321", "30322", "30323", "30324", "30325", "30326", "30327", "30328", "30329", "30330", "30331", "30332", "30333", "30334", "30335", "30336", "30337", "30338", "30339", "30340", "30341", "30342", "30343", "30344", "30345", "30346", "30347", "30348", "30349", "30350", "30351", "30352", "30353", "30354", "30355", "30356", "30357", "30358", "30359", "30360", "30361", "30362", "30363", "30364", "30365", "30366", "30367", "30368", "30369", "30370", "30371", "30372", "30373", "30374", "30375", "30376", "30377", "30378", "30379", "30380", "96801", "96802", "96803", "96804", "96805", "96806", "96807", "96808", "96809", "96810", "96811", "96812", "96813", "96814", "96815", "96816", "96817", "96818", "96819", "96820", "96821", "96822", "96823", "96824", "96825", "96826", "96827", "96828", "96829", "83254", "60601", "60602", "60603", "60604", "60605", "60606", "60607", "60608", "60609", "60610", "60611", "60612", "60613", "60614", "60615", "60616", "60617", "60618", "60619", "60620", "60621", "60622", "60623", "60624", "60625", "60626", "60627", "60628", "60629", "60630", "60631", "60632", "60633", "60634", "60635", "60636", "60637", "60638", "60639", "60640", "62701", "62702", "62703", "62704", "62705", "62706", "62707", "62708", "46201", "46202", "46203", "46204", "46205", "46206", "46207", "46208", "52801", "52802", "52803", "52804", "52805", "52806", "52807", "52808", "50301", "50302", "50303", "50304", "50305", "50306", "50307", "50308", "50309", "50310", "50311", "50312", "50313", "50314", "50315", "50316", "50317", "50318", "50319", "50320", "50321", "50322", "67201", "67202", "67203", "67204", "67205", "67206", "67207", "67208", "67209", "67210", "67211", "67212", "67213", "67214", "67215", "67216", "67217", "67218", "67219", "67220", "41701", "41702", "70112", "70113", "70114", "70115", "70116", "70117", "70118", "4032", "4033", "21201", "21202", "21203", "21204", "21205", "21206", "21207", "21208", "21209", "21210", "21211", "21212", "21213", "21214", "21215", "21216", "21217", "21218", "21219", "21220", "21221", "21222", "21223", "21224", "21225", "21226", "21227", "21228", "21229", "21230", "21231", "21232", "21233", "21234", "21235", "21236", "2101", "2102", "2103", "2104", "2105", "2106", "2107", "2108", "2109", "2110", "2111", "2112", "2113", "2114", "2115", "2116", "2117", "2118", "2119", "2120", "2121", "2122", "2123", "2124", "2125", "2126", "2127", "2128", "2129", "2130", "2131", "2132", "2133", "2134", "2135", "2136", "49036", "49734", "49735", "55801", "55802", "55803", "55804", "55805", "55806", "55807", "39530", "39531", "39532", "39533", "39534", "63101", "63102", "63103", "63104", "63105", "63106", "63107", "63108", "63109", "63110", "63111", "63112", "63113", "63114", "63115", "63116", "63117", "63118", "63119", "63120", "63121", "63122", "63123", "63124", "63125", "63126", "63127", "63128", "63129", "63130", "63131", "63132", "63133", "63134", "63135", "63136", "63137", "63138", "63139", "63140", "59044", "68901", "68902", "89501", "89502", "89503", "89504", "89505", "89506", "89507", "89508", "89509", "89510", "89511", "89512", "3217", "7039", "87500", "87501", "87502", "87503", "87504", "87505", "10001", "10002", "10003", "10004", "10005", "10006", "10007", "10008", "10009", "10010", "10011", "10012", "10013", "10014", "10015", "10016", "10017", "10018", "10019", "10020", "10021", "10022", "10023", "10024", "10025", "10026", "10027", "10028", "10029", "10030", "10031", "10032", "10033", "10034", "10035", "10036", "10037", "10038", "10039", "10040", "10041", "10042", "10043", "10044", "10045", "10046", "10047", "27565", "58282", "44101", "44102", "44103", "44104", "44105", "44106", "44107", "44108", "44109", "44110", "44111", "44112", "44113", "44114", "44115", "44116", "44117", "44118", "44119", "44120", "44121", "44122", "44123", "44124", "44125", "44126", "44127", "44128", "44129", "44130", "44131", "44132", "44133", "44134", "44135", "44136", "44137", "44138", "44139", "44140", "44141", "44142", "44143", "44144", "44145", "44146", "44147", "44148", "44149", "44150", "44151", "44152", "44153", "44154", "44155", "44156", "44157", "44158", "44159", "44160", "44161", "44162", "44163", "44164", "44165", "44166", "44167", "44168", "44169", "44170", "44171", "44172", "44173", "44174", "44175", "44176", "44177", "44178", "74101", "74102", "74103", "74104", "74105", "74106", "74107", "74108", "74109", "97201", "97202", "97203", "97204", "97205", "97206", "97207", "97208", "97209", "97210", "97211", "97212", "97213", "97214", "97215", "97216", "97217", "97218", "97219", "97220", "97221", "97222", "97223", "97224", "15201", "15202", "15203", "15204", "15205", "15206", "15207", "15208", "15209", "15210", "15211", "15212", "15213", "15214", "15215", "15216", "15217", "15218", "15219", "15220", "15221", "15222", "15223", "15224", "15225", "15226", "15227", "15228", "15229", "15230", "15231", "15232", "15233", "15234", "15235", "15236", "15237", "15238", "15239", "15240", "15241", "15242", "15243", "2840", "2841", "29020", "57401", "57402", "37201", "37202", "37203", "37204", "37205", "37206", "37207", "37208", "37209", "37210", "37211", "37212", "37213", "37214", "37215", "37216", "37217", "37218", "37219", "37220", "37221", "78701", "78702", "78703", "78704", "84321", "84322", "5751", "24517", "98004", "98005", "98006", "98007", "98008", "25813", "53201", "53202", "53203", "53204", "53205", "53206", "53207", "53208", "53209", "53210", "53211", "53212", "53213", "53214", "53215", "53216", "53217", "53218", "53219", "53220", "53221", "53222", "53223", "53224", "53225", "53226", "53227", "82941", "94043", "48104", "21244", "60106"];
  };


  $(document).ready(function() {
    $("#card_form").submit(function(e) {
      return zip_validator.validate();
    });
  });
})(jQuery);