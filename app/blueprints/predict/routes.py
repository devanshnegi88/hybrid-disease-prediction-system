from flask import request, jsonify
from . import predict_bp

from app.services.predictor_service import predict_disease
from app.services.psychology_engine import compute_psychology_score
from app.services.decision_layer import decide_condition
from app.services.guidance_engine import build_guidance_with_gemini
from app.services.hospital_finder import find_hospitals_for_disease


@predict_bp.route("/predict", methods=["POST"])
def api_predict():
    try:
        # data = request.get_json(force=True)


        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        symptoms_text = data.get("symptoms", "")
        city = data.get("city", "Dehradun")

        stress = data.get("stress", "Low")
        anxiety = data.get("anxiety", "Low")
        sleep = data.get("sleep", "Normal")

        ml_out = predict_disease(symptoms_text)
        psy = compute_psychology_score(stress, anxiety, sleep)

        condition = decide_condition(
            confidence=ml_out.get("confidence", 0.0),
            top3=ml_out.get("top3", []),
            psychology_impact=psy.get("impact", 0.0)
        )

        hospitals = []
        guidance = ""

        if condition == "HIGH_CONFIDENCE":
            hospitals = find_hospitals_for_disease(ml_out.get("prediction", "Unknown"), city)
        else:
            guidance = build_guidance_with_gemini(condition, symptoms_text, ml_out, psy)

        return jsonify({
            "condition": condition,
            "ml": ml_out,
            "psychology": psy,
            "hospitals": hospitals,
            "guidance": guidance
        })
    
    except Exception as e:
        import traceback
        print(f"API Error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            "error": str(e),
            "message": "An error occurred while processing your prediction. Please try again."
        }), 400
