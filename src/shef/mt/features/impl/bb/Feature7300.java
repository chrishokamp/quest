package shef.mt.features.impl.bb;

import java.util.HashSet;

import shef.mt.features.impl.Feature;
import shef.mt.features.util.Sentence;

/**
 * Stopword + POS LM perplexity  
 * 
 * @author Chris Hokamp 
 */


// Working:
// 1- map the target sentence to the POS + STOPWORD representation
// 2- to process a sentence, get the POS and check if the original token is a stopword or not
// 

// in NGramExec.java, this is their command: String execProcess = path + "ngram -lm " + lmFile + " -order ? -debug 1 -ppl " + inputFile + " > " + outputFile;
// --- what is their output file?

//   - they are writing the raw ngram output to the perplexity file in NGramExec.java



public class Feature7300 extends Feature {

	public Feature7300(){
		setIndex(7300);
		setDescription("log probability of the target pos+stopword representation");
        HashSet<String> res = new HashSet<String>();
		res.add("stopposlogprob");
		setResources(res);
	}

	@Override
	public void run(Sentence source, Sentence target) {
        setValue((Float) target.getValue("stopposlogprob"));
    }

}
