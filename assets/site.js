/* Deep Orbit Network — le seul script du site.
 *
 * Amelioration progressive, jamais dependance.
 *
 * La premiere chose que fait ce script est de poser `js` sur <html>, et
 * TOUT le repli du menu est conditionne a cette classe dans la feuille de
 * style. La raison est simple : sans JavaScript, rien ne peut rouvrir un
 * menu replie, et un menu replie qui ne s'ouvre pas n'est pas une
 * degradation, c'est une navigation perdue. Tant que la classe n'est pas
 * la, le menu s'affiche en liste et le bouton reste cache.
 *
 * Le formulaire, lui, reste soumis a la validation native du navigateur.
 * Et le pied de page liste les treize pages sur chaque page, donc meme un
 * script a moitie charge laisse le site entierement navigable.
 *
 * Aucune requete reseau. Aucun cookie. Aucun stockage.
 */
(function () {
  "use strict";

  var doc = document;
  doc.documentElement.className += (doc.documentElement.className ? " " : "")
    + "js";
  var fr = (doc.documentElement.getAttribute("lang") || "fr") === "fr";

  function txt(a, b) { return fr ? a : b; }

  /* ------------------------------------------------------------ menu */
  var burger = doc.querySelector(".burger");
  var nav = doc.getElementById("nav");

  if (burger && nav) {
    burger.addEventListener("click", function () {
      var ouvert = nav.classList.toggle("ouvert");
      burger.setAttribute("aria-expanded", ouvert ? "true" : "false");
    });

    /* Au-dessus du point de bascule le menu est toujours visible, et
     * `aria-expanded` doit alors dire la verite : laisser "false" sur un
     * menu affiche annonce un etat replie a qui ecoute la page. */
    var mq = window.matchMedia("(min-width:1061px)");
    function accorde() {
      if (mq.matches) {
        nav.classList.remove("ouvert");
        burger.setAttribute("aria-expanded", "true");
      } else {
        burger.setAttribute("aria-expanded",
          nav.classList.contains("ouvert") ? "true" : "false");
      }
    }
    if (mq.addEventListener) mq.addEventListener("change", accorde);
    else if (mq.addListener) mq.addListener(accorde);
    accorde();

    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("ouvert")) {
        nav.classList.remove("ouvert");
        burger.setAttribute("aria-expanded", "false");
        burger.focus();
      }
    });
  }

  /* ------------------------------------------------------ formulaire */
  var form = doc.querySelector(".formulaire");
  if (!form) return;

  var boite = form.querySelector(".err");
  var liste = boite ? boite.querySelector("ul") : null;
  var etat = form.querySelector(".etat");

  function etiquette(ch) {
    var lab = form.querySelector('label[for="' + ch.id + '"]');
    if (lab) return lab.textContent.trim();
    var w = ch.closest(".champ-c");
    return w ? w.textContent.trim() : ch.name;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var champs = form.querySelectorAll("input, select, textarea");
    var fautifs = [];
    var i, ch;

    for (i = 0; i < champs.length; i++) {
      ch = champs[i];
      var enveloppe = ch.closest(".champ") || ch.closest(".champ-c");
      if (enveloppe) enveloppe.classList.remove("faux");
      ch.removeAttribute("aria-invalid");
      if (!ch.checkValidity()) {
        fautifs.push(ch);
        if (enveloppe) enveloppe.classList.add("faux");
        ch.setAttribute("aria-invalid", "true");
      }
    }

    if (liste) liste.innerHTML = "";

    if (fautifs.length) {
      if (etat) etat.textContent = "";
      for (i = 0; i < fautifs.length; i++) {
        var li = doc.createElement("li");
        var a = doc.createElement("a");
        a.href = "#" + fautifs[i].id;
        a.textContent = etiquette(fautifs[i]);
        /* Le lien ne se contente pas de sauter a l'ancre : il DONNE LE
         * FOCUS au champ. Sauter fait defiler, ce qui suffit a qui voit
         * la page et ne sert a rien a qui navigue au clavier. */
        (function (cible) {
          a.addEventListener("click", function (ev) {
            ev.preventDefault();
            cible.focus();
          });
        }(fautifs[i]));
        li.appendChild(a);
        if (liste) liste.appendChild(li);
      }
      if (boite) {
        boite.hidden = false;
        boite.setAttribute("tabindex", "-1");
        boite.focus();
      }
      return;
    }

    if (boite) boite.hidden = true;

    /* Le formulaire est complet et valide. Il ne part nulle part, et le
     * message le dit sans detour : il n'y a ni domaine, ni adresse
     * professionnelle, ni destinataire. On ne propose AUCUN numero ni
     * AUCUNE adresse de repli — il n'en existe pas, et en inventer un
     * serait exactement la faute que tout le reste du site evite. */
    if (etat) {
      etat.textContent = txt(
        "Formulaire valide, et rien n'a été envoyé. La " +
        "plateforme n'a pas encore de destinataire : ni domaine, ni " +
        "adresse professionnelle. Ce message existe pour montrer le " +
        "comportement du formulaire, pas pour faire croire qu'un " +
        "message est parti.",
        "Form valid, and nothing has been sent. The platform has no " +
        "recipient yet: no domain, no professional address. This " +
        "message exists to show how the form behaves, not to make you " +
        "believe a message went out.");
    }
  });
}());
