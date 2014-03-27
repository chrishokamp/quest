package shef.mt.features.impl.bb;

import shef.mt.features.impl.Feature;

/**
 * Stopword + POS LM perplexity  
 * 
 * @author Chris Hokamp 
 */


// Working:
// 1- map the target sentence to the POS + STOPWORD representation
// 2- to process a sentence, get the POS and check if the original token is a stopword or not
// 

// 3- understand runNGramPPL()
// in NGramExec.java, this is their command: String execProcess = path + "ngram -lm " + lmFile + " -order ? -debug 1 -ppl " + inputFile + " > " + outputFile;
//  

public class Feature7300 extends Feature {

	public Feature7300(){
		setIndex(7300);
		setDescription("");
//        HashSet<String> res = new HashSet<String>();
//		res.add("Giza");
//		setResources(res);
	}
	
	// for each token in source, check if there is a token in target which aligns with a high probability
	public void run(Sentence source, Sentence target) {
		System.out.println("running feature 7001");
		float defaultThreshold = 0.33f;
		
        float noTokens = source.getNoTokens();
        String[] tokens = source.getTokens();
        float numAlignments = 0;
        float ratioValue;
        for (String word : tokens) {
        	// WORKING: check if the alignments is null
            HashMap alignmentMap = Giza.getTranslationMap(word);
            if (alignmentMap != null) {
            	if (containsWithThreshold(alignmentMap, defaultThreshold)) {
            		numAlignments += 1;
            	}
            }
        }

        if (numAlignments == 0) {
            setValue(0);
        } else {
            setValue(numAlignments / noTokens);
        }
	}
	
	

}
