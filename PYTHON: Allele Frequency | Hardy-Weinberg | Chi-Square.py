import scipy.stats as stats

def hardy_weinberg_test(observed_counts):
    standardized_counts = {}
    for genotype, count in observed_counts.items():
        alleles = sorted(genotype.split('/'))
        standardized_genotype = f'{alleles[0]}/{alleles[1]}'
        if standardized_genotype in standardized_counts:
            standardized_counts[standardized_genotype] += count
        else:
            standardized_counts[standardized_genotype] = count

    counts = standardized_counts
    alleles = ['*1', '*2', '*3', '*17']
    total_individuals = sum(counts.values())
    total_alleles = 2 * total_individuals
    allele_counts = {allele: 0 for allele in alleles}

    for genotype, count in counts.items():
        allele1, allele2 = genotype.split('/')
        allele_counts[allele1] += count
        allele_counts[allele2] += count

    allele_frequencies = {allele: count / total_alleles for allele, count in allele_counts.items()}
    expected_counts = {}
    for allele1 in alleles:
        for allele2 in alleles:
            if allele1 <= allele2:
                freq1 = allele_frequencies[allele1]
                freq2 = allele_frequencies[allele2]
                if allele1 == allele2:
                    expected_counts[f'{allele1}/{allele2}'] = (freq1 ** 2) * total_individuals
                else:
                    expected_counts[f'{allele1}/{allele2}'] = 2 * freq1 * freq2 * total_individuals
    
    observed = [counts.get(genotype, 0) for genotype in expected_counts.keys() if expected_counts[genotype] > 0]
    expected = [expected_counts[genotype] for genotype in expected_counts.keys() if expected_counts[genotype] > 0]

    if len(observed) == 0 or len(expected) == 0:
        chi2, p_value = float('nan'), float('nan')
    else:
        chi2, p_value = stats.chisquare(observed, expected)

    alpha = 0.05
    if p_value < alpha:
        interpretation = "Significant difference from Hardy-Weinberg equilibrium (Reject H0)"
    else:
        interpretation = "No significant difference from Hardy-Weinberg equilibrium (Fail to reject H0)"

    results = {
        'Allele frequencies': allele_frequencies,
        'Expected counts': expected_counts,
        'Chi-square test': {'Chi2 value': chi2, 'p-value': p_value},
        'Interpretation': interpretation
    }

    return results

example_counts = {
    '*1/*1': 68, '*1/*2': 29, '*1/*3': 0, '*2/*2': 0, '*2/*3': 0,
    '*1/*17': 36, '*2/*17': 7, '*3/*17': 0, '*17/*17': 6, '*3/*3': 0
}
results = hardy_weinberg_test(example_counts)

results
