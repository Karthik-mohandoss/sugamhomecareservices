<?php
/**
 * Sugam Home Care Services - Form Enquiry & Lead Dispatcher
 * Sends new enquiries to admin email(s) via PHP mail()
 * and logs to a secure local file as a permanent backup.
 */

header('Content-Type: application/json; charset=UTF-8');
date_default_timezone_set('Asia/Kolkata');

// Security & anti-abuse checks
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
    exit;
}

// Read JSON input or fallback to $_POST
$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if (!is_array($data) || empty($data)) {
    $data = $_POST;
}

// Extract and sanitize fields
$fullName = isset($data['fullName']) ? trim(strip_tags($data['fullName'])) : '';
$phone    = isset($data['phone']) ? trim(preg_replace('/[^0-9+]/', '', $data['phone'])) : '';
$service  = isset($data['service']) ? trim(strip_tags($data['service'])) : 'General Home Care Enquiry';
$pageUrl  = isset($data['pageUrl']) ? trim(strip_tags($data['pageUrl'])) : '/';
$leadId   = isset($data['id']) ? trim(strip_tags($data['id'])) : 'LEAD-' . time();
$utm      = isset($data['utm']) && is_array($data['utm']) ? $data['utm'] : [];

$utmSource   = isset($utm['utm_source']) ? trim(strip_tags($utm['utm_source'])) : 'direct';
$utmMedium   = isset($utm['utm_medium']) ? trim(strip_tags($utm['utm_medium'])) : '';
$utmCampaign = isset($utm['utm_campaign']) ? trim(strip_tags($utm['utm_campaign'])) : '';
$gclid       = isset($utm['gclid']) ? trim(strip_tags($utm['gclid'])) : '';

// Validation
if (empty($fullName)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Full name is required']);
    exit;
}

if (empty($phone) || strlen($phone) < 10) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Valid phone number is required']);
    exit;
}

$timestamp = date('d M Y, h:i A T');
$clientIp  = $_SERVER['REMOTE_ADDR'] ?? 'Unknown';

// Recipients
$primaryEmail   = 'akrithmarketer@gmail.com';
$secondaryEmail = 'care@sugamhomecareservices.in';

// Quick WhatsApp link for admin to click and chat with customer
$cleanPhoneForWa = preg_replace('/[^0-9]/', '', $phone);
if (strlen($cleanPhoneForWa) === 10) {
    $cleanPhoneForWa = '91' . $cleanPhoneForWa;
}
$waDirectLink = "https://wa.me/{$cleanPhoneForWa}?text=" . urlencode("Hello {$fullName}, greetings from Sugam Home Care Services. We received your enquiry for {$service}.");

// Construct HTML Email
$subject = "🏥 New Lead: {$service} - {$fullName} ({$phone})";

$htmlBody = "
<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; color: #222; }
    .card { background: #ffffff; max-width: 600px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.08); border: 1px solid #e5e9f0; }
    .header { background: #0f2b48; color: #ffffff; padding: 24px; text-align: center; }
    .header h1 { margin: 0; font-size: 22px; font-weight: 700; }
    .header p { margin: 6px 0 0 0; font-size: 14px; opacity: 0.85; }
    .content { padding: 24px; }
    .badge { display: inline-block; background: #e0f2fe; color: #0369a1; padding: 4px 12px; border-radius: 9999px; font-size: 13px; font-weight: 600; margin-bottom: 16px; }
    .lead-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    .lead-table td { padding: 12px 14px; border-bottom: 1px solid #f1f5f9; font-size: 15px; }
    .lead-table td.label { font-weight: 600; color: #475569; width: 38%; }
    .lead-table td.value { color: #0f172a; font-weight: 500; }
    .btn-group { text-align: center; margin: 24px 0 10px 0; }
    .btn { display: inline-block; padding: 12px 22px; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 14px; margin: 5px; }
    .btn-call { background: #0f2b48; color: #ffffff !important; }
    .btn-wa { background: #25d366; color: #ffffff !important; }
    .footer { background: #f8fafc; padding: 16px; font-size: 12px; color: #64748b; text-align: center; border-top: 1px solid #e2e8f0; }
  </style>
</head>
<body>
  <div class='card'>
    <div class='header'>
      <h1>Sugam Home Care Services</h1>
      <p>New Website Lead Notification</p>
    </div>
    <div class='content'>
      <span class='badge'>Lead ID: {$leadId}</span>
      
      <table class='lead-table'>
        <tr>
          <td class='label'>Customer Name:</td>
          <td class='value'><strong>{$fullName}</strong></td>
        </tr>
        <tr>
          <td class='label'>Phone Number:</td>
          <td class='value'><a href='tel:{$phone}' style='color:#0f2b48; font-weight:700;'>{$phone}</a></td>
        </tr>
        <tr>
          <td class='label'>Service Required:</td>
          <td class='value' style='color:#0f2b48; font-weight:700;'>{$service}</td>
        </tr>
        <tr>
          <td class='label'>Received At:</td>
          <td class='value'>{$timestamp}</td>
        </tr>
        <tr>
          <td class='label'>Page URL:</td>
          <td class='value'><a href='https://sugamhomecareservices.in{$pageUrl}' target='_blank'>{$pageUrl}</a></td>
        </tr>
        <tr>
          <td class='label'>Campaign Details:</td>
          <td class='value'>Source: <code>{$utmSource}</code>" . (!empty($utmMedium) ? " | Medium: <code>{$utmMedium}</code>" : "") . (!empty($utmCampaign) ? " | Campaign: <code>{$utmCampaign}</code>" : "") . (!empty($gclid) ? " | GCLID: <code>{$gclid}</code>" : "") . "</td>
        </tr>
      </table>

      <div class='btn-group'>
        <a href='tel:{$phone}' class='btn btn-call'>📞 Call Customer Now</a>
        <a href='{$waDirectLink}' class='btn btn-wa' target='_blank'>💬 Open in WhatsApp</a>
      </div>
    </div>
    <div class='footer'>
      Enquiry received from sugamhomecareservices.in &bull; Client IP: {$clientIp}
    </div>
  </div>
</body>
</html>
";

// Plain text alternative
$plainText = "🏥 Sugam Home Care Services - New Lead Enquiry\n\n";
$plainText .= "Customer Name: " . $fullName . "\n";
$plainText .= "Phone: " . $phone . "\n";
$plainText .= "Service Required: " . $service . "\n";
$plainText .= "Date/Time: " . $timestamp . "\n";
$plainText .= "Page URL: " . $pageUrl . "\n";
$plainText .= "Campaign Source: " . $utmSource . " " . $utmCampaign . "\n\n";
$plainText .= "Call: tel:" . $phone . "\n";
$plainText .= "WhatsApp: " . $waDirectLink . "\n";

// Headers
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-type: text/html; charset=UTF-8\r\n";
$headers .= "From: Sugam Home Care <noreply@sugamhomecareservices.in>\r\n";
$headers .= "Reply-To: Sugam Care <care@sugamhomecareservices.in>\r\n";
$headers .= "Cc: " . $secondaryEmail . "\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

// 1. Send Email
$mailSent = @mail($primaryEmail, $subject, $htmlBody, $headers);

// 2. Permanent Server-side Backup Log (JSON lines)
$logEntry = [
    'id'        => $leadId,
    'timestamp' => $timestamp,
    'fullName'  => $fullName,
    'phone'     => $phone,
    'service'   => $service,
    'pageUrl'   => $pageUrl,
    'utm'       => $utm,
    'ip'        => $clientIp,
    'mailSent'  => $mailSent
];

$logFile = __DIR__ . '/.enquiries_backup.jsonl';
@file_put_contents($logFile, json_encode($logEntry) . "\n", FILE_APPEND | LOCK_EX);

// Response
echo json_encode([
    'success'  => true,
    'message'  => 'Enquiry successfully submitted and dispatched',
    'leadId'   => $leadId,
    'mailSent' => $mailSent
]);
