/**
 *
 */
package shef.mt.features.impl.bb;

import shef.mt.tools.Giza2;
import java.util.HashSet;
import java.util.StringTokenizer;

import shef.mt.features.impl.Feature;
import shef.mt.features.util.Sentence;
import shef.mt.tools.FileModel;
import shef.mt.tools.Giza;

/**
 * average number of translations per source word in the sentence (threshold in
 * giza2: prob > 0.5) weighted by the frequency of each word in the source
 * corpus
 *
 * @author Catalina Hallett
 *
 *
 */
public class Feature1029 extends Feature {

    final static Float probThresh = 0.05f;

    public Feature1029() {
        setIndex("1029");
        setDescription("average number of translations per source word in the sentence (threshold in giza2: prob > 0.5) weighted by the frequency of each word in the source corpus");
        HashSet res = new HashSet<String>();
        res.add("Giza2");
        res.add("Freq");
        setResources(res);
    }

    /* (non-Javadoc)
     * @see wlv.mt.features.util.Feature#run(wlv.mt.features.util.Sentence, wlv.mt.features.util.Sentence)
     */
    @Override
    public void run(Sentence source, Sentence target) {
        float noTokens = source.getNoTokens();

        float probSum = 0;

        String[] tokens = source.getTokens();
        for (String word : tokens) {
            probSum += Giza2.getWordProbabilityCount(word, probThresh) * FileModel.getFrequency(word);
        }

        float result = probSum / noTokens;

        setValue(result);
    }
}
