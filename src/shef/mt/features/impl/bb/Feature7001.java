/**
 * 
 */
package shef.mt.features.impl.bb;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;

import shef.mt.features.impl.Feature;
import shef.mt.features.util.Sentence;
import shef.mt.tools.Giza;

/**
 * proportion of unigrams aligned with >=0.5 probability in giza1  
 * 
 * @author Chris Hokamp 
 */
public class Feature7001 extends Feature {

	/* (non-Javadoc)
	 * @see wlv.mt.features.impl.Feature#run(wlv.mt.features.util.Sentence, wlv.mt.features.util.Sentence)
	 */
	
	public Feature7001(){
		setIndex(7001);
		setDescription("proportion of unigrams aligned with >=0.5 probability in giza1");
        HashSet<String> res = new HashSet<String>();
		res.add("Giza");
		setResources(res);
	}
	
	// utility method
	private boolean containsWithThreshold(HashMap<String,Float> testMap, Float threshold) {
		if (threshold > 1) {
			return false;
		}
		Iterator<Map.Entry<String,Float>> it = testMap.entrySet().iterator();
        Map.Entry<String, Float> entry;
		while(it.hasNext()) {
			entry = it.next();
			if (entry.getValue() >= threshold) {
				return true;
			}
		}
		return false;
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
