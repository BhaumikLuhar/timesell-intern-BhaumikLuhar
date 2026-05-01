from task3_ai.parser import format_explanation

# Mock explanation
mock_explanation = {
    'summary': 'Your portfolio has a good balance with 40% in fixed deposits, providing stability. However, 20% in NIFTY50 and 30% in gold add moderate growth potential.',
    'good': 'Strong cash reserves of 10% and diversification across asset classes reduces risk.',
    'improve': 'Consider reducing gold allocation from 30% to 20% and increasing equity exposure for better long-term growth.',
    'verdict': 'Conservative'
}

print(format_explanation(mock_explanation))

# Test error case
error_explanation = {
    'error': 'Gemini API quota exceeded'
}

print(format_explanation(error_explanation))
