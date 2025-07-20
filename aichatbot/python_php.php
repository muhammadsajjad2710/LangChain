<?php
$pythonScript = __DIR__ . "/new.py";
$jsonFile = __DIR__ . "/output.json";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["convert"])) {
        // Check if the audio file exists
        $audioFile = "D:/Artificial Intelligence/Lang chain/sampleaudio.mp4";
        if (!file_exists($audioFile)) {
            echo "<p style='color:red;'>Error: Please first upload the audio file.</p>";
        } else {
            // Run Python script
            $command = escapeshellcmd("python \"$pythonScript\"");
            shell_exec($command);
            echo "<p style='color:green;'>Speech converted successfully. JSON file created.</p>";
        }
    }

    if (isset($_POST["read_json"])) {
        if (!file_exists($jsonFile)) {
            echo "<p style='color:red;'>Error: JSON file not found. Please convert speech first.</p>";
        } else {
            $jsonData = file_get_contents($jsonFile);
            $data = json_decode($jsonData, true);
            
            if ($data) {
                echo "<b>Transcribed Text:</b> <pre>" . htmlspecialchars($data['transcribed_text']) . "</pre>";
                echo "<b>ChatGPT Response:</b> <pre>" . htmlspecialchars($data['chatgpt_response']) . "</pre>";
            } else {
                echo "<p style='color:red;'>Error: Could not read JSON data.</p>";
            }
        }
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Speech to Text</title>
</head>
<body>
    <h2>Speech to Text Conversion</h2>

    <form method="post">
        <button type="submit" name="convert">Convert Speech to Text</button>
        <button type="submit" name="read_json">Read JSON Data</button>
    </form>
</body>
</html>
