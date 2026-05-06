import json

from chain import build_chain

def main():
    chain = build_chain()

    cv = open("data/cv.txt").read()
    job = open("data/job.txt").read()

    result = chain.invoke({
        "cv": cv,
        "job_ad": job
    })

 # Convert Pydantic object -> dict
    data = result.model_dump()

    # Save to file
    with open("./data/cv2.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Saved to cv.json")

if __name__ == "__main__":
    main()
