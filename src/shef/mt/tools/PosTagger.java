package shef.mt.tools;

import java.util.HashSet;
import java.util.Set;

import shef.mt.util.Logger;

/**
 * Base class for part-of-speech tagger wrappers
 *
 * @author Catalina Hallett
 *
 */
public class PosTagger extends Resource {

    String name = "";
    String path = "";
    String lang;
    
    Set<String> stopset;

    String[] args = null;
    String input;
    String output;
    static String XPOS = ".XPOS";
    public static String[] NounTags = {"NN", "NNS", "NP", "NPS", "NAM", "NOM", "PER", "NMON", "NMEA"};
    public static String[] VerbTags = {
        "VVD", "VV", "VVZ", "VVN", "VHP", "VB", "VBG", "VBD", "VBN", "VBP", "VBZ",
        "VER:cond", "VER:futu", "VER:impe", "VER:impf", "VER:infi", "VER:pper",
        "VER:ppre", "VER:pres", "VER:simp", "VER:subi", "VER:subp", "VCLIger", "VCLIinf",
        "VCLIfin", "VEadj", "VEfin", "VEger", "VEinf", "VHadj", "VHfin",
        "VHger", "VHinf", "VLadj", "VLfin", "VLger", "VLinf", "VMadj", "VMfin",
        "VMger", "VMinf", "VSadj", "VSfin", "VSger", "VSinf"};

    public static String[] getNounTags() {
        return NounTags;
    }

    public static void setNounTags(String[] nounTags) {
        NounTags = nounTags;
    }

    public static String[] getVerbTags() {
        return VerbTags;
    }

    public static void setVerbTags(String[] verbTags) {
        VerbTags = verbTags;
    }

    public static String[] getAdditionalTags() {
        return AdditionalTags;
    }

    public static void setAdditionalTags(String[] additionalTags) {
        AdditionalTags = additionalTags;
    }

    public static String[] getPronTags() {
        return PronTags;
    }

    public static void setPronTags(String[] pronTags) {
        PronTags = pronTags;
    }
    public static String[] AdditionalTags = {"JJ", "JJR", "JJS", "RB", "RBR", "RBS", "ADJ", "ADV"};
    public static String[] PronTags = {"PP", "PRP", "PPX"};
    static boolean alwaysRun;

    public String run() {
        return "";
    }

    ;



	public PosTagger() {
        super(null);
        Logger.log("***********Initiating PosTagger***************");

	    // Working - hardcode this for testing - change to load language-specific stoplists
//	    String[] stoplist = {"I","a","about","an","are","as","at","be","by","com","for","from","how","in","is","it","of","on","or","that","the","this","to","was","what","when","where","who","will","with","the","www"};
	    // String[] stoplist = {"I","a","about","an","are","as","at","be","by","com","for","from","how","in","is","it","of","on","or","that","the","this","to","was","what","when","where","who","will","with","the","www"};
        
        // German
//	    String[] stoplist = {"aber", "Aber", "als", "Als", "am", "Am", "an", "An", "auch", "Auch", "auf", "Auf", "aus", "Aus", "bei", "Bei", "bin", "Bin", "bis", "Bis", "bist", "Bist", "da", "Da", "dadurch", "Dadurch", "daher", "Daher", "darum", "Darum", "das", "Das", "daß", "Daß", "dass", "Dass", "dein", "Dein", "deine", "Deine", "dem", "Dem", "den", "Den", "der", "Der", "des", "Des", "dessen", "Dessen", "deshalb", "Deshalb", "die", "Die", "dies", "Dies", "dieser", "Dieser", "dieses", "Dieses", "doch", "Doch", "dort", "Dort", "du", "Du", "durch", "Durch", "ein", "Ein", "eine", "Eine", "einem", "Einem", "einen", "Einen", "einer", "Einer", "eines", "Eines", "er", "Er", "es", "Es", "euer", "Euer", "eure", "Eure", "für", "Für", "hatte", "Hatte", "hatten", "Hatten", "hattest", "Hattest", "hattet", "Hattet", "hier", "Hier", "hinter", "Hinter", "ich", "Ich", "ihr", "Ihr", "ihre", "Ihre", "im", "Im", "in", "In", "ist", "Ist", "ja", "Ja", "jede", "Jede", "jedem", "Jedem", "jeden", "Jeden", "jeder", "Jeder", "jedes", "Jedes", "jener", "Jener", "jenes", "Jenes", "jetzt", "Jetzt", "kann", "Kann", "kannst", "Kannst", "können", "Können", "könnt", "Könnt", "machen", "Machen", "mein", "Mein", "meine", "Meine", "mit", "Mit", "muß", "Muß", "mußt", "Mußt", "musst", "Musst", "müssen", "Müssen", "müßt", "Müßt", "nach", "Nach", "nachdem", "Nachdem", "nein", "Nein", "nicht", "Nicht", "nun", "Nun", "oder", "Oder", "seid", "Seid", "sein", "Sein", "seine", "Seine", "sich", "Sich", "sie", "Sie", "sind", "Sind", "soll", "Soll", "sollen", "Sollen", "sollst", "Sollst", "sollt", "Sollt", "sonst", "Sonst", "soweit", "Soweit", "sowie", "Sowie", "und", "Und", "unser", "Unser", "unsere", "Unsere", "unter", "Unter", "vom", "Vom", "von", "Von", "vor", "Vor", "wann", "Wann", "warum", "Warum", "was", "Was", "weiter", "Weiter", "weitere", "Weitere", "wenn", "Wenn", "wer", "Wer", "werde", "Werde", "werden", "Werden", "werdet", "Werdet", "weshalb", "Weshalb", "wie", "Wie", "wieder", "Wieder", "wieso", "Wieso", "wir", "Wir", "wird", "Wird", "wirst", "Wirst", "wo", "Wo", "woher", "Woher", "wohin", "Wohin", "zu", "Zu", "zum", "Zum", "zur", "Zur", "über", "Über"};
        
        // Spanish
        String[] stoplist = {"algún", "Algún", "alguna", "Alguna", "algunas", "Algunas", "alguno", "Alguno", "algunos", "Algunos", "ambos", "Ambos", "ampleamos", "Ampleamos", "ante", "Ante", "antes", "Antes", "aquel", "Aquel", "aquellas", "Aquellas", "aquellos", "Aquellos", "aqui", "Aqui", "arriba", "Arriba", "atras", "Atras", "bajo", "Bajo", "bastante", "Bastante", "bien", "Bien", "cada", "Cada", "cierta", "Cierta", "ciertas", "Ciertas", "cierto", "Cierto", "ciertos", "Ciertos", "como", "Como", "con", "Con", "conseguimos", "Conseguimos", "conseguir", "Conseguir", "consigo", "Consigo", "consigue", "Consigue", "consiguen", "Consiguen", "consigues", "Consigues", "cual", "Cual", "cuando", "Cuando", "dentro", "Dentro", "desde", "Desde", "donde", "Donde", "dos", "Dos", "el", "El", "ellas", "Ellas", "ellos", "Ellos", "empleais", "Empleais", "emplean", "Emplean", "emplear", "Emplear", "empleas", "Empleas", "empleo", "Empleo", "en", "En", "encima", "Encima", "entonces", "Entonces", "entre", "Entre", "era", "Era", "eramos", "Eramos", "eran", "Eran", "eras", "Eras", "eres", "Eres", "es", "Es", "esta", "Esta", "estaba", "Estaba", "estado", "Estado", "estais", "Estais", "estamos", "Estamos", "estan", "Estan", "estoy", "Estoy", "fin", "Fin", "fue", "Fue", "fueron", "Fueron", "fui", "Fui", "fuimos", "Fuimos", "gueno", "Gueno", "ha", "Ha", "hace", "Hace", "haceis", "Haceis", "hacemos", "Hacemos", "hacen", "Hacen", "hacer", "Hacer", "haces", "Haces", "hago", "Hago", "incluso", "Incluso", "intenta", "Intenta", "intentais", "Intentais", "intentamos", "Intentamos", "intentan", "Intentan", "intentar", "Intentar", "intentas", "Intentas", "intento", "Intento", "ir", "Ir", "la", "La", "largo", "Largo", "las", "Las", "lo", "Lo", "los", "Los", "mientras", "Mientras", "mio", "Mio", "modo", "Modo", "muchos", "Muchos", "muy", "Muy", "nos", "Nos", "nosotros", "Nosotros", "otro", "Otro", "para", "Para", "pero", "Pero", "podeis", "Podeis", "podemos", "Podemos", "poder", "Poder", "podria", "Podria", "podriais", "Podriais", "podriamos", "Podriamos", "podrian", "Podrian", "podrias", "Podrias", "por", "Por", "por qué", "Por qué", "porque", "Porque", "primero", "Primero", "puede", "Puede", "pueden", "Pueden", "puedo", "Puedo", "quien", "Quien", "sabe", "Sabe", "sabeis", "Sabeis", "sabemos", "Sabemos", "saben", "Saben", "saber", "Saber", "sabes", "Sabes", "ser", "Ser", "si", "Si", "siendo", "Siendo", "sin", "Sin", "sobre", "Sobre", "sois", "Sois", "solamente", "Solamente", "solo", "Solo", "somos", "Somos", "soy", "Soy", "su", "Su", "sus", "Sus", "también", "También", "teneis", "Teneis", "tenemos", "Tenemos", "tener", "Tener", "tengo", "Tengo", "tiempo", "Tiempo", "tiene", "Tiene", "tienen", "Tienen", "todo", "Todo", "trabaja", "Trabaja", "trabajais", "Trabajais", "trabajamos", "Trabajamos", "trabajan", "Trabajan", "trabajar", "Trabajar", "trabajas", "Trabajas", "trabajo", "Trabajo", "tras", "Tras", "tuyo", "Tuyo", "ultimo", "Ultimo", "un", "Un", "una", "Una", "unas", "Unas", "uno", "Uno", "unos", "Unos", "usa", "Usa", "usais", "Usais", "usamos", "Usamos", "usan", "Usan", "usar", "Usar", "usas", "Usas", "uso", "Uso", "va", "Va", "vais", "Vais", "valor", "Valor", "vamos", "Vamos", "van", "Van", "vaya", "Vaya", "verdad", "Verdad", "verdadera", "Verdadera", "verdadero", "Verdadero", "vosotras", "Vosotras", "vosotros", "Vosotros", "voy", "Voy", "yo", "Yo"};
	    stopset = new HashSet<String>();
	    for (String s: stoplist) {
	    	stopset.add(s);
	    }
    }

    public void setParameters(String lang, String tagName, String exePath, String input, String output) {
        Logger.log("PosTagger parameters: type=" + lang + " name:" + tagName);
        Logger.log("Executable: " + exePath);
        Logger.log("Input: " + input);
        Logger.log("Output: " + output);
        name = tagName;
        path = exePath;
        this.lang = lang;
        this.input = input;
        this.output = output;
    }
    
    // Chris - added for POS + Stopword
//    public void setStoplist(String stoplist) {
//        Logger.log("PosTagger:  loading stoplist: " + stoplist);
//        // TODO: load from file (currently hardcoded)
//        this.stoplist = stoplist;
//    }

    public PosTagger(String lang, String tagName, String exePath, String input, String output, ResourceProcessor posProc) {
        super(posProc);
        name = tagName;
        path = exePath;
        this.lang = lang;
        this.input = input;
        this.output = output;

    }

    public static void ForceRun(boolean value) {
        alwaysRun = value;
    }

    public static boolean isVerb(String tag) {
        // 07/03/2012: Reimplemented by Mariano
        return tag.length() > 0 ? (tag.charAt(0) == 'V') : false;

//                for (String crtTag:VerbTags)
//			if (tag.equals(crtTag))
//				return true;
//		return false;
    }

    public static boolean isNoun(String tag) {
        // 07/03/2012: Reimplemented by Mariano
        return tag.length() > 0 ? (tag.charAt(0) == 'N') : false;
//                for (String crtTag:NounTags)
//			if (tag.equals(crtTag))
//				return true;
//		return false;
    }

    public static boolean isAdditional(String tag) {
        for (String crtTag : AdditionalTags) {
            if (tag.equals(crtTag)) {
                return true;
            }
        }
        return false;
    }

    public static boolean isPronoun(String tag) {
        for (String crtTag : PronTags) {
            if (tag.equals(crtTag)) {
                return true;
            }
        }
        return false;
    }

    public static String getXPOS() {
        return XPOS;
    }
}
