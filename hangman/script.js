function oppdaterHangmanBilde() {
    let bilde = document.getElementById("hangmanImg");
    let bildenr = Math.min(6 - gjenværendeForsøk, 6); // Sørger for at vi ikke får et for høyt bildetall
    bilde.src = `images/hangman${bildenr}.png`;
  }
  
  function gjettBokstav() {
    let inpGjett = document.getElementById("letterInput");
    let bokstav = inpGjett.value.toLowerCase();
  
    // Sjekker om input er en gyldig bokstav
    if (!/^[a-zæøå]$/.test(bokstav)) {
      inpGjett.value = ""; // Tømmer feltet
      return;
    }
    if (hemmeligOrdBokstaver.includes(bokstav)) {
      for (let i = 0; i < hemmeligOrdBokstaver.length; i++) {
        if (bokstav === hemmeligOrdBokstaver[i]) {
          riktigGjetninger[i] = bokstav;
        }
      }
      document.getElementById("wordDisplay").textContent =
        riktigGjetninger.join(" ");
    } else {
      if (!Feilgjetninger.includes(bokstav)) {
        Feilgjetninger.push(bokstav);
        gjenværendeForsøk--;
        oppdaterHangmanBilde();
        document.getElementById("wrongLetters").textContent =
          "Feilgjetninger: " + Feilgjetninger.join(", ");
        document.getElementById("remainingAttempts").textContent =
          "Forsøk igjen: " + gjenværendeForsøk;
      }
    }
  
    if (gjenværendeForsøk === 0) {
      alert(`Du tapte! Ordet var ${hemmeligOrd}`);
      inpGjett.value = ""; // Tømmer feltet etter avsluttet spill
      return;
    }
    if (!riktigGjetninger.includes("_")) {
      alert("Gratulerer, du vant!");
      inpGjett.value = ""; // Tømmer feltet etter avsluttet spill
      return;
    }
  
    inpGjett.value = ""; // Tømmer feltet etter hver gjetning
    inpGjett.focus(); // Setter fokus tilbake til input-feltet
  }
  
  // Ingen endringer nedenfor denne linjen er nødvendig
  let ordliste = [
    "javascript", "html", "css", "programmering", "webutvikling", "algoritme", "database", "frontend",
    "backend", "fullstack", "rammeverk", "bibliotek", "nettverk", "server", "klient", "funksjon",
    "variabel", "objekt", "array", "boolean", "nodejs", "react", "angular", "vue", "python", "java",
    "php", "swift", "kotlin", "typescript", "ruby", "bash", "linux", "windows", "macos", "firewall",
    "nettleser", "kode", "fil", "kompilator", "syntaks", "operatør", "klasse", "instans", "rekursjon",
    "iterasjon", "json", "xml", "api", "rest", "graphql", "datablad", "datakryptering", "dekkfunksjon",
    "ifelse", "loop", "forwhile", "databasekall", "query", "sql", "nosql", "mongo", "cassandra", "redis",
    "docker", "kubernetes", "orm", "mvc", "tcpip", "udp", "http", "https", "dns", "devops", "scrum",
    "agil", "programvare", "hardware", "sky", "datasenter", "maskinlæring", "nevralt", "modul", "pakke",
    "jsonapi", "asynkron", "synkron", "heap", "stack", "minne", "prosessor", "brannmur", "sikkerhet",
    "autentisering", "autorisasjon", "brukergrensesnitt", "design", "ux", "ui", "cookie", "sesjon",
    "kapsling", "arv", "polymorfi", "virtualisering", "kjernemodul", "kloning", "git", "bitbucket",
    "github", "merge", "pullrequest", "build", "testing", "integrasjon", "deployment"
  ];
  
  let tilfeldigIndex = Math.floor(Math.random() * ordliste.length);
  let hemmeligOrd = ordliste[tilfeldigIndex];
  let Feilgjetninger = [];
  let gjenværendeForsøk = 6;
  let hemmeligOrdBokstaver = hemmeligOrd.split("");
  let riktigGjetninger = Array(hemmeligOrdBokstaver.length).fill("_");
  
  document.getElementById("wordDisplay").textContent = riktigGjetninger.join(" ");
  document.getElementById("guessButton").addEventListener("click", gjettBokstav);
  document
    .getElementById("letterInput")
    .addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
        gjettBokstav();
      }
    });
  